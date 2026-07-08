document.getElementById("send-btn").addEventListener("click", () => {
    let userInput = document.getElementById("user-input").value.trim();
    if (userInput === "") return;
  
    let chatBox = document.getElementById("chat-box")
    let userDiv = document.createElement("div")
  
    userDiv.className = "user-msg";
    userDiv.textContent = userInput;
    chatBox.appendChild(userDiv);
  
    document.getElementById("user-input").value = "";
  
    fetch("/get_answer", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({question: userInput})
    })
    .then(response => response.json())
    .then(data => {
      let botDiv = document.createElement("div");
      botDiv.className = "bot-msg";
      botDiv.innerHTML = marked.parse(data.answer);
      chatBox.appendChild(botDiv);
      chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => {
      let botDiv = document.createElement("div");
      botDiv.className = "bot-msg error";
      botDiv.innerHTML = "Couldn't connect, try again later.";
      chatBox.appendChild(botDiv);
      chatBox.scrollTop = chatBox.scrollHeight;
      console.error("Fetch error: ", error);
    });
  });
  
  document.getElementById("user-input").addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
      document.getElementById("send-btn").click();
    }
  });
  
  document.getElementById("user-input").focus();