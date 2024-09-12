from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def home():
    return 'Welcome to the Children Story App!'

@app.route('/generate_story', methods=['POST'])
def generate_story():
    data = request.json
    prompt = data.get('prompt', '')

    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=500
        )
        story = response.choices[0].text.strip()
        return jsonify({'story': story})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/recommend_story', methods=['GET'])
def recommend_story():
    # Dummy recommendations for demonstration
    recommendations = [
        'The Magic Tree House',
        'Charlotte\'s Web',
        'Alice in Wonderland',
        'The Little Prince'
    ]
    return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    app.run(debug=True)
