const chatinput = document.getElementById("chatinput")
const messeges = document.getElementById("messeges")
const username = document.getElementById("username")

const red = document.getElementById("red")
chatinput.onkeydown=function(evt){
    console.log(evt.key)
    red.innerHTML = chatinput.value
    if(evt.key === "Enter"){
        chat()
        chatinput.value=""
    }
}
function chat(){
    const text = document.createElement("div");
    text.innerText =`${username.value}: ${chatinput.value}`
    text.classList.add("textbox")
    messeges.appendChild(text)
}

// const room = document.createElement("div");
// room.style.backgroundColor=color(roo.monster)
// room.classList.add("room")
// roomRepeater.appendChild(room);
// });