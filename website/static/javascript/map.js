/* eslint-disable no-unused-vars */
let map;
const DEFAULT_CENTER = {lat: 42.360, lng: -71.059};
const DEFAULT_ZOOM = 12; // eventually let user decide this based on dropdown
const REPORT_ZOOM = 15;

/**
 * Initializes a Google Map and adds reports to it
 * @return {void}
 */
async function initMap() {
  const {Map} = await google.maps.importLibrary('maps');

  // Centering Map around Boston, MA
  map = new Map(
      document.getElementById('googleMap'),
      {
        zoom: DEFAULT_ZOOM,
        center: DEFAULT_CENTER,
        mapId: 'DEMO_MAP_ID', // figure out what this should be
        gestureHandling: 'cooperative',
      },
  );

  const reports = await getJson();
  for (const report of reports) {
    createMarker(report, map);
  }
}


/**
 * Gathers a list of reports from the JSON file of reports
 * @return {any[]} the list of reports
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
 * Creates a marker from the given report and adds it to the given map.
 * @param {any} report - the report to create a marker from
 * @param {Map} map - the Google Map to add the marker to
 * @return {void}
 */
async function createMarker(report, map) {
  const {AdvancedMarkerElement} = await google.maps.importLibrary('marker');
  const reportLocation = getReportLocation(report);
  // marker
  const markerDesign = await customizeMarker(report);
  const marker = new AdvancedMarkerElement({
    map: map,
    position: reportLocation,
    title: report['typeOfReport'],
    content: markerDesign.element,
  });
  createInfoWindow(map, marker, report);
}


/**
 * Creates an InfoWindow (similar to a popup) to be opened when the given marker
 * is clicked with details of the given report.
 * @param {Map} map - the map the marker is located on
 * @param {any} marker - the marker to add the window to
 * @param {report} report - the details to include in the window
 * @return {void}
 */
async function createInfoWindow(map, marker, report) {
  const infoWindow = new google.maps.InfoWindow({});
  // close -- zoom out
  infoWindow.addListener('closeclick', function() {
    recenterAndZoom(map, DEFAULT_CENTER, DEFAULT_ZOOM);
  });
  // open -- zoom in
  marker.addListener('click', function() {
    recenterAndZoom(map, getReportLocation(report), REPORT_ZOOM);
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
 * @return {PinElement} an pin element containing the desired customizations
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
    case 'Physical Harassment':
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


/**
 * Changes the center and zoom of the given map, based on the location of
 * the report.
 * @param {Map} map - the google map to be recentered and zoomed
 * @param {any} newCenter - the position of the new map center
 * @param {int} newZoom - the amount the map should be zoomed
 * @return {void}
 */
function recenterAndZoom(map, newCenter, newZoom) {
  // TODO: figure this out
  // const zoomAnimations = {
  //   easing: google.maps.Animation.DROP,
  // };

  map.setCenter(newCenter);
  map.setZoom(newZoom);
  return map;
}


/**
 * Gets the location of a report (in lat/long format).
 * @param {report} report - the report to get the location from
 * @return {any} the location of the report
 */
function getReportLocation(report) {
  const locs = report['gcAddress'].split(',');
  const position = {lat: parseFloat(locs[0]), lng: parseFloat(locs[1])};
  return position;
}
