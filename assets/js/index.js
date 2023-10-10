const fileBox = document.getElementById("filebox");
const editBtn = document.getElementById("edit-button");
const openBtn = document.getElementById("open-files");
const buttons = document.querySelectorAll(".buttons");
const closeBtn = document.getElementById('close-btn');
const minBtn = document.getElementById('min-btn');
const settingsBtn = document.getElementById('settings-btn')
const darkModeBtn = document.getElementById('darkmode');
const textFormatButtons = document.querySelectorAll('.btn');
const titleInput = document.getElementById('title-input');
const textBox = document.getElementById('text-box');
// const 

// Loading animation
// I want the class to be removed when the animation stops(Synchronously)

function sleep(ms) {
	return new Promise(resolve => setTimeout(resolve, ms))
}

async function startAnimation() {
	// set timer to 2.5 seconds for both animation and sleep time (2.5 +2.5 = 5sec)

	setTimeout(function () {
		document.getElementById("loader").style.display = "none";
		document.getElementById("main").style.display = "block";
	}, 2500)
	await sleep(2500);

	// remove the class to balance the styling of the page

	document.getElementById("main-animate").classList.remove("main-container");
  	console.log(document.getElementById("main-animate").classList);
}

startAnimation()


// Add an event listeners to each of the buttons
if (textFormatButtons) {
	textFormatButtons.forEach(button => {
		button.addEventListener('click', (e) => {
			buttonUtilities(e);
		})
	})
}

// add button clicks when the page loads
if (textFormatButtons) {
	textFormatButtons.forEach(button => {
		button.addEventListener('click', () => {
			switch (button.textContent.toUpperCase()) {
				case "B":
				document.execCommand("bold");
				break;
				case "I":
				document.execCommand("italic");
				break;
				case "U":
				document.execCommand("underline");
				break;
  			}
		})
		
	})
}



// Enable dark mode
darkModeBtn.addEventListener('click', (e) => {
	if (e.target.textContent.toLowerCase() === "dark mode") {
		e.target.innerText = "Light Mode";
		// Overide default stylings
		document.body.classList.add("dark-mode");
		darkModeBtn.classList.add("d-btn");
		titleInput.classList.add("d-input");
		textBox.classList.add("d-text-content");
	} else {
		e.target.innerText = "Dark Mode";
		document.body.classList.remove("dark-mode");
		darkModeBtn.classList.remove("d-btn");
		titleInput.classList.remove("d-input");
		textBox.classList.remove("d-text-content")
  	}

})

// Button Utilities
function buttonUtilities(e) {
    const btnClassList = e.target.classList;
	if (btnClassList.contains("active")){
		btnClassList.remove("active")
	} else {
		btnClassList.toggle("active")
	}
}

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

// button functions
function newWindow() {
  pywebview.api.new_window().then(response => !response && alert("You can't open more than 2 TypePen windows!"));
}

function openFiles() {
  pywebview.api.open_file().then( (response) => {
    pywebview.api.open_file_window(response)
  })
}

function openSettings() {
	pywebview.api.settings_window();
}

// window functions
function exitWindow() {
  pywebview.api.close_window();
}

function minimizeWindow() {
  pywebview.api.minimize_window();
}



saveBtn.addEventListener("click", function () {
  let fileName = prompt("Enter File Name ");
  if (fileName) {
    let textInfo = textConts.innerHTML;
    pywebview.api.save_file(fileName, textInfo).then((response) => {
      if (response == "Saved") {
        alert("File Saved Succesfully");
      } else {
        alert("Something went wrong");
      }
    });
  }
});
