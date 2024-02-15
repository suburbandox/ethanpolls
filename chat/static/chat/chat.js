 const message = document.getElementById("message")
 const sendMessage = document.getElementById("sendMessage")
 const chats = document.getElementById("chats")

async function reloadChats() {
    let response = await fetch('/chat/chats')
    let json = await response.json()
    let  chats2  = json.chats//.reverse()
    let html = chats2.map(chat => `<div>${chat}</div>`).join('\n')
    chats.innerHTML = html
  }
  function handleSubmit() {
    const text = message.value
    fetch(`/chat/create?message=${text}`)
    message.value= ""
    const myTimeout = setTimeout(bottom, 2000);
  }
    sendMessage.onclick = handleSubmit
    message.onkeydown = function(evt) {
        if (evt.key === 'Enter') {
            handleSubmit()
        }
    }
    function bottom(){
      chats.scrollTop=chats.scrollHeight
    }

  setInterval(() => {
    //console.log(new Date())
    reloadChats()
  }, 2000)

