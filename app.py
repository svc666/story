from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = 'your_openai_api_key_here'

@app.route('/generate_story', methods=['POST'])
def generate_story():
    data = request.json
    prompt = data.get('prompt', 'Once upon a time...')
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    
    story = response.choices[0].text.strip()
    return jsonify({"story": story})

@app.route('/recommend_story', methods=['GET'])
def recommend_story():
    # Example recommendations
    recommendations = [
        "The Little Prince",
        "Charlotte's Web",
        "Matilda",
        "The Tale of Peter Rabbit"
    ]
    return jsonify({"recommendations": recommendations})

if __name__ == '__main__':
    app.run(debug=True)
