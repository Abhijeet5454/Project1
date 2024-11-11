function verifyDuplicate() {
    // Get the values from the input fields
    var newTech = document.getElementById('newTech').value;

    // Create a data object to send
    // var data = { newTech: newTech , age: 30};

    // Use the Fetch API to send data asynchronously
    fetch('/verifyDuplicate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newTech) // Send the data as JSON
    })
    .then(response => response.json()) // Parse the JSON response
    .then(data => {
        // Display success message
        document.getElementById('response').innerText = 'Data submitted successfully: ' + JSON.stringify(data);
    })
    .catch(error => {
        // Display error message
        document.getElementById('response').innerText = 'Error submitting data: ' + error;
    });
}

let blockCounter = 0;
function addCustomBlock() {
    const customBlockName = document.getElementById("customBlockName").value.trim();

    if (!customBlockName){
        alert("Enter Block Name");
        return;
    }

    blockCounter++;
            
    // Create a new div for the custom field
    const newBlockDiv = document.createElement("div");
    newBlockDiv.classList.add("form-group");
    newBlockDiv.id = `customBlock${blockCounter}`;

    // Create the label for the new field
    const newLabel = document.createElement("label");
    newLabel.textContent = `${customBlockName}:`;
    newLabel.htmlFor = `customBlock${blockCounter}`;

    // Create the input for the new field
    const newInput = document.createElement("input");
    newInput.type = "text";
    newInput.id = `customBlock${blockCounter}`;
    newInput.name = customBlockName; // Use the custom field name as the input name
    newInput.placeholder = `Enter value for ${customBlockName}`;
    newInput.required = true;

    const removeButton = document.createElement("button");
    removeButton.id = `block${blockCounter}`
    removeButton.type = "button";
    removeButton.textContent = "Remove";
    removeButton.onclick = () => removeCustomField(newBlockDiv.id);

    // Append the label, input, and remove button to the div
    newBlockDiv.appendChild(newLabel);
    newBlockDiv.appendChild(newInput);
    newBlockDiv.appendChild(removeButton);
    // Append the new field div to the custom fields container
    document.getElementById("customBlockContainer").appendChild(newBlockDiv);

    // Clear the custom field name input
    document.getElementById("customBlockName").value = '';
}

// Function to remove a custom field
function removeCustomField(blockid) {
    const fieldToRemove = document.getElementById(blockid);
    if (fieldToRemove) {
        fieldToRemove.remove();
        blockCounter--;
    }
}