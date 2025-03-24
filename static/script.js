function uploadFile() {
    let fileInput = document.getElementById("fileInput");
    if (fileInput.files.length === 0) {
        alert("Please select a file.");
        return;
    }

    let formData = new FormData();
    formData.append("file", fileInput.files[0]);

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
    let userInput = document.getElementById("userInput").value;
    let chatbox = document.getElementById("chatbox");
    let context = document.getElementById("fileContent").textContent;

    if (userInput.trim() === "") return;

    chatbox.innerHTML += `<p><b>You:</b> ${userInput}</p>`;

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput, context: context })
    })
    .then(response => response.json())
    .then(data => {
        chatbox.innerHTML += `<p><b>AI:</b> ${data.response}</p>`;
        document.getElementById("userInput").value = "";
    })
    .catch(error => console.error("Error:", error));
}
