# chat-with-ollama
Flask Ollama Chat is a web application built with Flask, Ollama, and Llama 3.1 8B that allows users to upload text files, view their content, and chat with an AI assistant about the uploaded text. The app runs entirely locally, ensuring complete privacy and data security—no data leaves your device.

# Features

- File Upload: Upload .txt files and view their content in the web interface.
- Interactive AI Chat: Discuss the contents of the uploaded text with an AI model powered by Llama 3.1 8B through Ollama.
- 100% Local: Everything runs on your local machine. No external servers or data collection—privacy first.
- Easy Model Switching: Easily switch between models (e.g., Llama 3 or Llama 3.1) by changing one line of code.

# Requirements

-Python with Flask for the backend
-Ollama for running the Llama 3.1 8B AI model locally
-HTML, CSS, JavaScript for the frontend
-Local file storage for uploaded text files

# Install 
1. Clone the repository
   `git clone https://github.com/yourusername/flask-ollama-chat.git
   cd flask-ollama-chat`
2. Install dependencies
   `pip install flask ollama`
3. Download the Llama model
   `ollama pull llama3.1:8b`
4. Run the Flask app
   `python app.py`
5. Access the web app
   Open your browser and go to http://127.0.0.1:5000/ to interact with the app.

# Customization 
You can easily switch between different Ollama Llama models (e.g., llama3:8b, llama3.1:8b) by changing the MODEL_NAME in app.py.
`MODEL_NAME = "llama3.1:8b"  # Change to "llama3:8b" for a different model`

# Contributing 
Feel free to contribute! Whether it’s bug fixes, feature requests, or improvements, contributions are welcome. Please fork this repository, make changes, and open a pull request.



