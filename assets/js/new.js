const boldBtn = document.getElementById("bold1");
const backBtn = document.getElementById("back");
const italicsBtn = document.getElementById('ita')
const underlineBtn = document.getElementById("underline-btn");
const saveBtn = document.getElementById("save-text");
const textConts = document.querySelector(".text-content");


backBtn.addEventListener("click", (e) => {
  console.log(pywebview.global.saveFile);
})


boldBtn.addEventListener('click', (e)=> {
  document.execCommand('bold')
})

italicsBtn.addEventListener("click", (e) => {
  document.execCommand("italic");
})

underlineBtn.addEventListener("click", (e) => {
  document.execCommand("underline");
})

saveBtn.addEventListener("click", function () {
  let fileName = prompt("Enter File Name ");
  if (fileName) {
    let textInfo = textConts.innerHTML
    pywebview.api.save_file(fileName, textInfo).then((response) => {
      if (response == "Saved") {
        alert("File Saved Succesfully");
      } else {
        alert("Something went wrong");
      }
    });
  } 
})
