document.getElementById("submit").addEventListener("click", submitClick)

function submitClick(){
    const messageInputDom = document.querySelector('#input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'type' : 'message',
        'message': message,
        'username': 'Me',
    }));
    messageInputDom.value = '';
}

document.getElementById("input").addEventListener("keyup", function(event) {
     if (event.keycode === 13) {
         event.preventDefault();
         document.getElementById("submit").addEventListener("click", submitClick)
         document.getElementById("submit").click();
     }
});

const chatSocket = new WebSocket(
'ws://' +
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