# 🦙 Chat with Ollama  

**Flask Ollama Chat** is a web application built with **Flask, Ollama, and Llama 3.1 8B**, allowing users to **upload files (text, PDFs, images)**, extract their content, and chat with an AI assistant about the extracted text.  

The app runs **entirely locally**, ensuring complete **privacy and data security**—**no data ever leaves your device**.  

---

## 🚀 Features  

✅ **File Upload**: Upload **.txt, .pdf, .jpg, .png** files and extract text automatically.  
✅ **OCR Support**: Uses **Tesseract OCR** to extract text from **images (JPEG, PNG)**.  
✅ **PDF Processing**: Extracts text from **PDFs** with **PyMuPDF**.  
✅ **Interactive AI Chat**: Discuss extracted text with an AI model powered by **Llama 3.1 8B** via Ollama.  
✅ **100% Local**: Runs **entirely on your machine**—**no cloud, no tracking, full privacy**.  
✅ **Easy Model Switching**: Swap AI models **easily** by changing one line of code.  

---

## 🛠️ Requirements  

- **Python** with **Flask** for the backend  
- **Ollama** for running the **Llama 3.1 8B AI model** locally  
- **HTML, CSS, JavaScript** for the frontend  
- **PyMuPDF** for **PDF text extraction**  
- **Tesseract OCR** for **image text extraction**  

---

## 📥 Install & Run  

### 1️⃣ Clone the repository  
```
git clone https://github.com/yourusername/flask-ollama-chat.git
cd flask-ollama-chat
```
### 2️⃣ Install dependencies
```
pip install flask ollama pymupdf pytesseract pillow
```
### 3️⃣ Download the Llama model
```
ollama pull llama3.1:8b
```
### 4️⃣ (Optional) Install Tesseract OCR (for image text extraction)
- macOS/Linux:
```
brew install tesseract
```
- Windows
   - Download from Tesseract's official site
   - Set the path in app.py
```
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```
### 5️⃣ Run the Flask app
```
python app.py
```
### 6️⃣ Access the web app
Open your browser and go to:
👉 http://127.0.0.1:5000/

---
## ⚙️ Customization
You can easily switch between different Ollama Llama models (e.g., llama3:8b, llama3.1:8b) by modifying the MODEL_NAME in app.py:
```
MODEL_NAME = "llama3.1:8b"  # Change to "llama3:8b" for a different model
```
## 🤝 Contributing
Want to improve the project?
✅ Bug fixes
✅ Feature requests
✅ UI/UX improvements

Contributions are welcome! 🚀 Fork the repo, make changes, and open a pull request.





