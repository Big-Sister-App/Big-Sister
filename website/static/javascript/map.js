const { json } = require("stream/consumers");


/**
 * Gets a list of reports from the JSON file of reports
 */
function getJson() {
    fetch('../databases/sample.json')
        .then(response => response.text())
        .then(jsonString => {
            const reports = JSON.parse(jsonString)
        })
        .catch(error => {
            console.error('Error:', error);
        });
}


