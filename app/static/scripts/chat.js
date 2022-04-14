document.getElementById("submit").addEventListener("click", submitClick)

function submitClick(){
    const messageInputDom = document.querySelector('#input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'type' : 'message',
        'message': message,
        'username': 'Covid-Chatbot',
    }));
    messageInputDom.value = '';
}

document.querySelector('#input').focus();
document.querySelector('#input').onkeyup = function (e) {
    if (e.keyCode === 13) { // enter, return
        document.querySelector('#submit').click();
    }
};

var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";

const chatSocket = new WebSocket(
ws_scheme + "://" +
window.location.host +
'/chat'+
'/ws/socket' 
);

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    console.log('Data: ', data)
    document.querySelector('#chat-text').value += (data.username + ': ' + data.message + " " + '\n')
    document.querySelector('#chat-text').value += ("Covid-Chatbot" + ': ' + data.response + " " + '\n')
}

chatSocket.onclose = function (e) {
    console.error('Chat socket suddenly closed?');
}