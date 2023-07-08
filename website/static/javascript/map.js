let map;

/**
 * Initializes a Google Map and adds reports to it
 * @return {void}
 */
async function initMap() {
  const boston = { lat: 42.360, lng: -71.059 };
  const { Map } = await google.maps.importLibrary("maps");

  // Centering Map around Boston, MA
  map = new Map(
    document.getElementById('googleMap'),
    {
      zoom: 10,
      center: boston,
      mapId: 'DEMO_MAP_ID',
    }
  );

  const reports = await getJson();
  for (const report of reports) {
    createMarker(report, map);
  }
}



/**
 * Gathers a list of reports from the JSON file of reports
 * @return {any[]} reports - the list of reports
 */
function getJson() {
    return fetch('../databases/geocoded_data.json')
        .then(response => response.text())
        .then(jsonString => {
            const reports = JSON.parse(jsonString);
            return reports;
        })
        .catch(error => {
            console.error('Error:', error);
        });
}


/**
 * Creates a marker from the given report and adds it to the given map
 * @param {any} report - a report
 * @param {Map} map - a Google Map
 * @return {void}
 */
async function createMarker(report, map) {
    const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");
    const locs = report['gcAddress'].split(',')
    const position = { lat: parseFloat(locs[0]), lng: parseFloat(locs[1]) }
    const marker = new AdvancedMarkerElement({
        map: map,
        position: position,
        title: report['typeOfReport']
    })
}