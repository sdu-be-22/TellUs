const id = JSON.parse(document.getElementById('json-username').textContent);
const message_username = JSON.parse(document.getElementById('json-message-username').textContent);

const socket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/'
    + id
    + '/'
);

socket.onopen = function(e){
    console.log("CONNECTION ESTABLISHED");
};

socket.onclose = function(e){
    console.log("CONNECTION LOST");
};

socket.onerror = function(e){
    console.log("ERROR OCCURED");
};

socket.onmessage = function(e){
    const data = JSON.parse(e.data);
    if(data.username == message_username){
        document.querySelector('#chat-body').innerHTML += `<tr>
                                                                <td>
                                                                <p class="chat-body_message_right">${data.message}</p>
                                                                </td>
                                                            </tr>`;
    }else{
        document.querySelector('#chat-body').innerHTML += `<tr>
                                                                <td>
                                                                <p class="chat-body_message_left">${data.message}</p>
                                                                </td>
                                                            </tr>`;
    }
};

document.querySelector('#chat-message-submit').onclick = function(e){
    const message_input = document.querySelector('#message_input');
    const message = message_input.value;

    socket.send(JSON.stringify({
        'message':message,
        'username':message_username
    }));

    message_input.value = '';
};

document.querySelector("#message_input").addEventListener("keypress", (e) => {
    if(e.keyCode  === 13) {

      
            const message_input = document.querySelector('#message_input');
            const message = message_input.value;
        
            socket.send(JSON.stringify({
                'message':message,
                'username':message_username
            }));
        
            message_input.value = '';
        
    }
});


function scrollToBottom() {
    const objDiv = document.querySelector('.message-table-scroll');
    objDiv.scrollTop = objDiv.scrollHeight;
}

scrollToBottom();