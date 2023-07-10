/* eslint-disable no-unused-vars */
let map;

/**
 * Initializes a Google Map and adds reports to it
 * @return {void}
 */
async function initMap() {
  const boston = {lat: 42.360, lng: -71.059};
  const {Map} = await google.maps.importLibrary('maps');

  // Centering Map around Boston, MA
  map = new Map(
      document.getElementById('googleMap'),
      {
        zoom: 12,
        center: boston,
        mapId: 'DEMO_MAP_ID', // figure out what this should be
      },
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
      .then((response) => response.text())
      .then((jsonString) => {
        const reports = JSON.parse(jsonString);
        return reports;
      })
      .catch((error) => {
        console.error('Error:', error);
      });
}

/**
 * Creates a marker from the given report and adds it to the given map. A
 * popup is also created with the marker to display the description of the
 * report.
 * @param {any} report - a report
 * @param {Map} map - a Google Map
 * @return {void}
 */
async function createMarker(report, map) {
  const {AdvancedMarkerElement} = await google.maps.importLibrary('marker');
  const locs = report['gcAddress'].split(',');
  const position = {lat: parseFloat(locs[0]), lng: parseFloat(locs[1])};

  // marker
  const markerDesign = await customizeMarker(report);
  const marker = new AdvancedMarkerElement({
    map: map,
    position: position,
    title: report['typeOfReport'],
    content: markerDesign.element,
  });
  // info window
  const infoWindow = new google.maps.InfoWindow({});
  marker.addListener('click', function() {
    infoWindow.setContent(reportToString(report));
    infoWindow.open(map, marker);
  });
}

/**
 * Formats a report as a multi-line string to be displayed to an end-user
 * @param {any} report - the report to format
 * @return {str}
 */
function reportToString(report) {
  const reportType = report['typeOfReport'];
  const reportDesc = report['reportDesc'];
  const reportLoc = report['location'];
  const reportDate = report['date'];

  const reportString = `
    <span style="font-weight: bold;">${reportType}</span>
    <br>
    ${reportDate}
    <br>
    ${reportLoc}
    <hr>
    ${reportDesc}
  `;

  return reportString;
}

// TODO: replace this with custom icons from @alaatamam and @raabyo when made
/**
 * Customizes the colors of a marker depending on the type of report it
 * represents.
 * @param {any} report - the report the marker is based on
 * @return {PinElement} - an element containing the desired customizations
 */
async function customizeMarker(report) {
  const {PinElement} = await google.maps.importLibrary('marker');
  const reportType = report['typeOfReport'];
  let customMarker;

  switch (reportType) {
    case 'Verbal Harassment':
      customMarker = new PinElement({
        background: '#9387ff',
      });
      break;
    case 'Physical Harrassment':
      customMarker = new PinElement({
        background: '#f3ff87',
      });
      break;
    case 'Sexual Assault':
      customMarker = new PinElement({
        background: '#ff9c62',
      });
      break;
    default:
      customMarker = new PinElement({
        background: '#ff8d87',
      });
  }
  return customMarker;
}
