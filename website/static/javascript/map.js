function initMap() {
    const myLatLng = { lat: 42.3397873, lng: -71.0880919};
    const map = new google.maps.Map(document.getElementById("googleMap"), {
      zoom: 4,
      center: myLatLng,
    });
  
    new google.maps.Marker({
      position: myLatLng,
      map,
      title: "Hello World!",
    });
  }
  
  window.initMap = initMap;