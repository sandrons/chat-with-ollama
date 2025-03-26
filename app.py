import pytesseract
import fitz  # PyMuPDF for PDFs
from PIL import Image
from flask import Flask, render_template, request, jsonify
import ollama
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

MODEL_NAME = "llama3.1:8b"  # Change this to "llama3:8b" to swap models

# Set the Tesseract path (for Windows users)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file using PyMuPDF."""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text") + "\n"
    return text.strip()

def extract_text_from_image(image_path):
    """Extracts text from an image using OCR (Tesseract)."""
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text.strip()

def load_text_file(filepath):
    """Load text from .txt, .pdf, or image files."""
    try:
        if filepath.endswith(".txt"):
            with open(filepath, "r", encoding="utf-8") as file:
                return file.read()
        elif filepath.endswith(".pdf"):
            return extract_text_from_pdf(filepath)
        elif filepath.endswith((".jpg", ".jpeg", ".png")):
            return extract_text_from_image(filepath)
        else:
            return None  # Unsupported file type
    except Exception as e:
        return f"Error reading file: {str(e)}"

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

    # Allow .txt, .pdf, .jpg, .png
    if not (file.filename.endswith((".txt", ".pdf", ".jpg", ".jpeg", ".png"))):
        return jsonify({"error": "Only .txt, .pdf, .jpg, and .png files are allowed!"}), 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    text = load_text_file(filepath)
    if text is None:
        return jsonify({"error": "Unsupported file type"}), 400

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
