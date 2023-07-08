/**
 * Gathers a list of reports from the JSON file of reports
 */
function getJson() {
    fetch('../databases/geocoded_data.json')
        .then(function (response) { return response.text(); })
        .then(function (jsonString) {
        var reports = JSON.parse(jsonString);
        // TODO: call addMarker function here on each element in the list
    })
        .catch(function (error) {
        console.error('Error:', error);
    });
}