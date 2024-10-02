function submitData() {
    // Get the values from the input fields
    var newTech = document.getElementById('newTech').value;

    // Create a data object to send
    var data = { newTech: newTech , age: 30};

    // Use the Fetch API to send data asynchronously
    fetch('/submit_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data) // Send the data as JSON
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