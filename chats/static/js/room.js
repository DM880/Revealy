const roomName = JSON.parse(document.getElementById('room-name').textContent);

        var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";

        const chatSocket = new WebSocket(
            ws_scheme
            + '://'
            + window.location.host
            + '/chats/'
            + roomName
            + '/'
        );


        chatSocket.onmessage = function(e) {
            const data = JSON.parse(e.data);
            document.querySelector('#chat-log').innerHTML += '<div class="mess-log" id="chat-log">' + (data.message + '\n') + '</div>';
        };


        chatSocket.onclose = function(e) {
            console.error('Chat socket closed unexpectedly');
        };

        document.querySelector('#chat-message-input').focus();
        document.querySelector('#chat-message-input').onkeyup = function(e) {
            if (e.keyCode === 13) {  // enter, return
                document.querySelector('#chat-message-submit').click();
            }
        };

        document.querySelector('#chat-message-submit').onclick = function(e) {
            const messageInputDom = document.querySelector('#chat-message-input');
            const message = messageInputDom.value;
            const username = JSON.parse(document.getElementById('username').textContent);
            chatSocket.send(JSON.stringify({
                'message': message,
                'username': username,
            }));
            messageInputDom.value = '';
        };


document.body.style.background = 'none';
document.body.style.backgroundColor = "white";
document.querySelector('.header').style.backgroundColor = "black";
// document.querySelector('#home').innerText = "Chats";
var url_href_header = document.getElementById('home');
url_href_header.setAttribute("href", url_chat);