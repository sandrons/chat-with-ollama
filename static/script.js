document.addEventListener("DOMContentLoaded", () => {
    const fileInput = document.getElementById("fileInput");
    const chatBox = document.getElementById("chatbox");
    const inputField = document.getElementById("userInput");
    const sendButton = document.getElementById("sendChat");
    const uploadButton = document.getElementById("uploadButton");

    function uploadFile() {
    let fileInput = document.getElementById("fileInput");
    if (fileInput.files.length === 0) {
        alert("Please select a file.");
        return;
    }

    let file = fileInput.files[0];
    let allowedExtensions = [".txt", ".pdf", ".jpg", ".jpeg", ".png"];

    if (!allowedExtensions.some(ext => file.name.endsWith(ext))) {
        alert("Only .txt, .pdf, .jpg, and .png files are allowed!");
        return;
    }

    let formData = new FormData();
    formData.append("file", file);

    fetch("/upload", { method: "POST", body: formData })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                alert(data.error);
            } else {
                document.getElementById("fileContent").textContent = data.content;
            }
        })
        .catch(error => console.error("Error:", error));
    }


    function sendMessage() {
        let userMessage = inputField.value.trim();
        let context = document.getElementById("fileContent").textContent;

        if (userMessage === "") return; // Prevent sending empty messages

        // Add user message to chatbox
        let userMessageElement = document.createElement("p");
        userMessageElement.classList.add("user");
        userMessageElement.innerHTML = `<b>You:</b> ${userMessage}`;
        chatBox.appendChild(userMessageElement);

        // Clear input field immediately after adding the message
        inputField.value = "";
        inputField.focus();

        // Scroll chat to latest message
        chatBox.scrollTop = chatBox.scrollHeight;

        fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: userMessage, context: context })
        })
        .then(response => response.json())
        .then(data => {
            let aiMessage = document.createElement("p");
            aiMessage.classList.add("ai");
            aiMessage.innerHTML = `<b>AI:</b> ${data.response}`;
            chatBox.appendChild(aiMessage);

            // Scroll chat to latest AI response
            chatBox.scrollTop = chatBox.scrollHeight;
        })
        .catch(error => console.error("Error:", error));
    }

    // Ensure the "Send" button works
    if (sendButton) {
        sendButton.addEventListener("click", sendMessage);
    }

    // Ensure "Enter" key works
    if (inputField) {
        inputField.addEventListener("keydown", function (event) {
            if (event.key === "Enter") {
                event.preventDefault(); // Prevent new lines
                sendMessage();
            }
        });
    }

    // Ensure the "Upload" button works
    if (uploadButton) {
        uploadButton.addEventListener("click", uploadFile);
    }
});
