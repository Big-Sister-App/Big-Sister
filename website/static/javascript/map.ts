/**
 * Gathers a list of reports from the JSON file of reports
 */
function getJson(): void {
    fetch('../databases/geocoded_data.json')
        .then(response => response.text())
        .then(jsonString => {
            const reports: any = JSON.parse(jsonString);
            // Use the 'reports' variable as needed
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
