document.querySelector('#room-name').onclick = function(e) {
    var roomName = document.querySelector('#room-name').value;
    window.location.pathname = '/chats/' + roomName + '/';
};
