// Add console.log to check to see if our code is working.
console.log("working");

// Create the map object with a center and zoom level.

// We create the tile layer that will be the background of our map.
let streets = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    accessToken: API_KEY
});

// We create the tile layer that will be the background of our map.
let satelliteStreets = L.tileLayer('https://api.mapbox.com/styles/v1/mapbox/satellite-streets-v11/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    accessToken: API_KEY
});

// Create a base layer that holds both maps.
let baseMaps = {
    "Streets": streets,
    "Satellite": satelliteStreets
  };

  //Create the map object with ceenter, zoom level and default layer. 

  let map = L.map('mapid', {
    center: [39.5, -98.5],
    zoom: 3, 
    layers: [streets]
  });

  L.control.layers(baseMaps).addTo(map)
let earthdata = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"

// Retrieve the earthquake GeoJSON data.
  d3.json(earthdata).then(function(data) { 

  console.log("test")

    // Creating a GeoJSON layer with the retrieved data.
    L.geoJSON(data).addTo(map);
  });
  

  
  

