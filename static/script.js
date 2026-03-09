var socket = io();

function sendMsg(){

    var input = document.getElementById("msg");

    var msg = input.value;

    if(msg.trim() === "") return;

    socket.send(msg);

    var messages = document.getElementById("messages");

    messages.innerHTML += `
    <div class="message sent">
        ${msg}
        <span class="time">now</span>
    </div>
    `;

    input.value="";
}

socket.on("message", function(msg){

    var messages = document.getElementById("messages");

    messages.innerHTML += `
    <div class="message received">
        ${msg}
        <span class="time">now</span>
    </div>
    `;

});
