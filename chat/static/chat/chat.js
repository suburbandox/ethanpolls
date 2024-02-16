 const message = document.getElementById("message")
 const sendMessage = document.getElementById("sendMessage")
 const chats = document.getElementById("chats")
 const nickname = document.getElementById("nickname")
 let myname = "anonymous"
async function reloadChats() {
  let response = await fetch('/chat/chats')
  let json = await response.json()
  let chats2 = json.chats//.reverse()
  console.log(chats)
  console.log(chats2)
  console.log(myname)
    //let html = chats2.map(chat => `<div>${chat}</div>`).join('\n')
  //   let html = chats2.map( unhax)
  // chats.innerHTML = html
  chats.innerHTML = ''
  chats2.forEach(chat => {
    console.log(55)
    const listItem = document.createElement("div");
    listItem.classList.add("chat")
    listItem.innerText = chat;
    chats.appendChild(listItem);
  });

}
function unhax(chat){
  let c = chat.innerText
  return c
}
  function handleSubmit() {
    const text =myname.toString()+": "+ message.value
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
    function namechange(){
      //console.log(myname)
      myname = nickname.value
    }

  setInterval(() => {
    //console.log(new Date())
    reloadChats()
  }, 2000)

