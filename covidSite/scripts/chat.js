document.querySelector('#submit').onclick = function (e) {
    const messageInputDom = document.querySelector('#input');
    const message = messageInputDom.value;
    chatSocket.send(JSON.stringify({
        'message': message,
        'username': "Me",
    }));
    messageInputDom.value = '';
};


const chatSocket = new WebSocket(
    'ws://' +
    window.location.host +
    '/ws/chat/' +
    '/'
);

chatSocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    console.log(data)
    let currentDate = new Date();
    let hours = currentDate.getHours();
    hours = (hours % 12) || 12;
    let time = hours + ":" + currentDate.getMinutes();
    document.querySelector('#chat-text').value += ("Me" + ': ' + data.message + '\n')
}