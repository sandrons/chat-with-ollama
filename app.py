from flask import Flask, render_template, request, jsonify
import ollama
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

MODEL_NAME = "llama3.1:8b"  # Change this to "llama3:8b" to swap models

def load_text_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    text = load_text_file(filepath)
    return jsonify({"filename": file.filename, "content": text})

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    context = data.get("context", "")
    
    response = ollama.chat(model=MODEL_NAME, messages=[
        {"role": "system", "content": "You are an AI assistant helping to discuss the given text."},
        {"role": "user", "content": context},
        {"role": "user", "content": user_message}
    ])
    
    return jsonify({"response": response["message"]["content"]})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
