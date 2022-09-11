const fileBox = document.getElementById("filebox");
const editBtn = document.getElementById("edit-button");
const openBtn = document.getElementById("open-files");
const buttons = document.querySelectorAll(".buttons");

setTimeout(function () {
  document.getElementById("loader").style.display = "none";
  document.getElementById("main").style.display = "block";
}, 100);


buttons.forEach((button) => {
  button.addEventListener('click', () => {
    let usersChoice = prompt("Are you sure you want to delete this file? (Y/N)")

    if (usersChoice.toUpperCase() == "Y") {
      pywebview.api.delete_file(button.parentElement.getAttribute("filename-data")).then((response) => {
        if (response == "Deleted"){
          alert('File deleted Successfully')
          location.reload()
        } else {
          alert('An unexpected error occured')
        }
      })
    }
  })
})

openBtn.addEventListener('click', (e) =>{
  pywebview.api.open_file().then( (response) => {
    console.log(response)
    // place_text(response);
    window.location.assign('/new/' + response[0])
  })
})

function place_text(content) {
  let textBox = document.querySelector(".text-content");
  if (textBox) {
    textBox.innerHTML = response;
  }
}
