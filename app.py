from flask import Flask, render_template, jsonify
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-python', methods=['POST'])
def run_python():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=2)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio).lower()
            return jsonify({'text': text})
        except sr.UnknownValueError:
            return jsonify({'error': 'Google Speech Recognition could not understand audio'})
        except sr.RequestError as e:
            return jsonify({'error': f'Could not request results from Google Speech Recognition service; {e}'})

if __name__ == '__main__':
    app.run(debug=True)
