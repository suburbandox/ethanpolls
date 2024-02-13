 const message = document.getElementById("message")
 const sendMessage = document.getElementById("sendMessage")
 const chats = document.getElementById("chats")

async function reloadChats() {
    let response = await fetch('/chat/chats')
    let json = await response.json()
    let  chats2  = json.chats
    let html = chats2.map(chat => `<div>${chat}</div>`).join('\n')
    chats.innerHTML = html

  }
  function handleSubmit() {
    const text = message.value
    fetch(`/chat/create?message=${text}`)
    message.value= ""
  }
    sendMessage.onclick = handleSubmit
    message.onkeydown = function(evt) {
        if (evt.key === 'Enter') {
            handleSubmit()
        }
    }

  setInterval(() => {
    console.log(new Date())
    reloadChats()
  }, 2000)

// const red = document.getElementById("red")
// chatinput.onkeydown=function(evt){
//     console.log(evt.key)
//     red.innerHTML = chatinput.value
//     if(evt.key === "Enter"){
//         chat()
//         chatinput.value=""
//     }
// }
// function chat(){
//     const text = document.createElement("div");
//     text.innerText =`${username.value}: ${chatinput.value}`
//     text.classList.add("textbox")
//     messeges.appendChild(text)
// }

// const room = document.createElement("div");
// room.style.backgroundColor=color(roo.monster)
// room.classList.add("room")
// roomRepeater.appendChild(room);
// });