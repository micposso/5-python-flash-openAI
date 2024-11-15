# create a flask app
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['API_KEY'] = os.getenv('API_KEY')

    OpenAI.api_key = app.config['API_KEY']

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/answer', methods=['POST', 'GET'])
    def answer():
        if request.method == 'POST':
            question = request.form['question']
            answer = OpenAI.Completion.create(
                engine="davinci",
                prompt=question,
                max_tokens=100
            )
            return jsonify({'answer': answer.choices[0].text})
        return render_template('index.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)