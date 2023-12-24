// Example POST method implementation:
async function postData(url = "", data = {}) {
    // Default options are marked with *
    const response = await fetch(url, {
      method: "POST", // *GET, POST, PUT, DELETE, etc.
      mode: "cors", // no-cors, *cors, same-origin
      cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
      credentials: "same-origin", // include, *same-origin, omit
      headers: {
        "Content-Type": "application/json",
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
      redirect: "follow", // manual, *follow, error
      referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
      body: JSON.stringify(data), // body data type must match "Content-Type" header
    });
    return response.json(); // parses JSON response into native JavaScript objects
  }
sendButton.addEventListener('click',async()=>{
    alert('Hey, you clicked!')
    questionInput=document.getElementById('questionInput').value;
    document.getElementById("questionInput").value="";

    document.querySelector(".right2").style.display="block";
    document.querySelector(".right1").style.display="none";

    question1.innerHTML=questionInput;
    question2.innerHTML=questionInput;
    //get the answer and populate it!
    let result=await postData("/api",{"question":questionInput})
    solution.innerHTML=result.answer

})