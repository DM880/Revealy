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

            // keep bottom page on added contetn
            window.scrollTo(0,document.body.scrollHeight);

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
            const current_room = JSON.parse(document.getElementById('current_room').textContent);
            chatSocket.send(JSON.stringify({
                'message': message,
                'username': username,
                'current_room': current_room
            }));
            messageInputDom.value = '';

        };


// change css style
document.body.style.background = 'none';
document.body.style.backgroundColor = "#2B2B2B";
document.querySelector('.header').style.backgroundColor = "white";

// change header to home (instead of chat)
var url_href_header = document.getElementById('home');

// add href to Chat header
url_href_header.setAttribute("href", url_chat);

//Scroll bottom page on refresh
window.scrollTo(0,document.body.scrollHeight);
