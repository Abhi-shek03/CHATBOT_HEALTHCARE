document.addEventListener("DOMContentLoaded", function () {
  var chatContainer = document.getElementsByClassName("msger-chat")[0];

  document.getElementById("send").addEventListener("click", function (event) {
    event.preventDefault(); // prevent the form from submitting
    var input = document.getElementById("input").value;
    console.log("Input value:", input);

    // Add user message to chat
    var html_You = `<div class="msg right-msg">
        <div class="msg-img"
          style="background-image: url(https://w7.pngwing.com/pngs/527/663/png-transparent-logo-person-user-person-icon-rectangle-photography-computer-wallpaper-thumbnail.png)">
        </div>
        <div class="msg-bubble">
          <div class="msg-info">
            <div class="msg-info-name">You</div>
            <div class="msg-info-time"></div>
          </div>
          <div class="msg-text">
            ${input}
          </div>
        </div>
      </div>`;
    chatContainer.innerHTML += html_You;

    // Send message to bot and add bot response to chat
    fetch(`/chatbot_bot/${input}`).then(function (response) {
      response.json().then(function (data) {
        console.log(data["reply"]);
        var html = `<div class="msg left-msg">
            <div class="msg-img"
              style="background-image: url(https://www.techopedia.com/wp-content/uploads/2023/03/6e13a6b3-28b6-454a-bef3-92d3d5529007.jpeg)">
            </div>
            <div class="msg-bubble">
              <div class="msg-info">
                <div class="msg-info-name">BOT</div>
              </div>
              <div class="msg-text">
                ${data.reply}
              </div>           
            </div>
          </div>`;
        chatContainer.innerHTML += html;
        document.getElementById("input").value = "";

        // Scroll to bottom of chat
        chatContainer.scrollTop = chatContainer.scrollHeight;
      });
    });
  });
});
