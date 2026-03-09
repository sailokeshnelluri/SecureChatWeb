var socket = io();

var typingTimer;

function sendMsg(){

    var input = document.getElementById("msg");
    var msg = input.value;

    if(msg.trim()==="") return;

    socket.send(msg);

    var messages = document.getElementById("messages");

    messages.innerHTML += `
    <div class="message sent">
        ${msg}
        <span class="time">now ✓</span>
    </div>
    `;

    input.value="";

    messages.scrollTop = messages.scrollHeight;

}

socket.on("message", function(msg){

    var messages = document.getElementById("messages");

    messages.innerHTML += `
    <div class="message received">
        ${msg}
        <span class="time">now</span>
    </div>
    `;

    messages.scrollTop = messages.scrollHeight;

});

document.getElementById("msg").addEventListener("keypress", function(e){

    if(e.key === "Enter"){
        e.preventDefault();
        sendMsg();
    }

});

document.getElementById("msg").addEventListener("input", function(){

    socket.emit("typing");

});

socket.on("typing", function(){

    var typing = document.getElementById("typing");

    typing.innerText="Typing...";

    clearTimeout(typingTimer);

    typingTimer = setTimeout(function(){

        typing.innerText="";

    },2000);

});

function addEmoji(){

    document.getElementById("msg").value += "😀";

}