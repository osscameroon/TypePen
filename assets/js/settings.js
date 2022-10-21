const pathBtn = document.getElementById("filepathbtn");
const pathInput = document.getElementById("path-input");
const saveBtn = document.getElementById("save-settings");
const infoBox = document.getElementById("info-box")

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

window.addEventListener("pywebviewready", function () {
	pywebview.api.load_settings().then((resp) => {
		let items = resp;

		// Set save location
		document.querySelector("#path-input").value = items["save_location"]

		// toggle autosave options from the settings file
		if (items["autosave"] === "true") {
		    document.querySelector('input[id="autosave-on"]').checked = true;
		} else {
		    document.querySelector('input[id="autosave-off"]').checked = true;
		}
	});
});

pathBtn.addEventListener('click', openFiles)
function openFiles() {
    pywebview.api.settings_path().then(response => {
		if (response) {
			pathInput.value = response;
		}
    });
}


saveBtn.addEventListener('click', () => {

	// Save settings for file path

	const folderPathInput = document.getElementById("path-input");

	pywebview.api.save_settings({"save_location": folderPathInput.value})
	
	// Save autosave settings button

	const radioOptions = document.querySelectorAll('input[name="autosave"]');
	let selectedValue;
	for (const ro of radioOptions) {
		if (ro.checked) {
			selectedValue = ro.value;
			break;
		}
	}
	switch (selectedValue) {
		case "on":
			pywebview.api.save_settings({"autosave": "true"})
			break;
		case "off":
			pywebview.api.save_settings({"autosave": "true"});
			break;
		case undefined:
			break;
	}


	// Notify the user and then remove the message after 2 sec
	async function addRemoveText() {
		infoBox.innerText = "[Settings Saved]";
		await sleep(2000);
		infoBox.innerText = "";
	}
	
	addRemoveText();
})