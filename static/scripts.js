// Weather Data Fetching
document.getElementById('weather-form').onsubmit = async (e) => {
    e.preventDefault();
    const location = document.getElementById('location').value;
    const response = await fetch(`/weather/${location}`);
    const data = await response.json();
    document.getElementById('weather-result').innerHTML = `Temperature: ${data.temperature} °C, Humidity: ${data.humidity}%, Description: ${data.description}`;
};

// Interactive Map with Leaflet.js
var map = L.map('map').setView([51.505, -0.09], 2); // Default to world view

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 18,
}).addTo(map);

document.getElementById('weather-form').onsubmit = async (e) => {
    e.preventDefault();
    const location = document.getElementById('location').value;
    const response = await fetch(`/weather/${location}`);
    const data = await response.json();

    // Move the map to the weather location
    const lat = data.coord.lat;
    const lon = data.coord.lon;
    map.setView([lat, lon], 10);

    L.marker([lat, lon]).addTo(map)
        .bindPopup(`Weather: ${data.weather[0].description}`)
        .openPopup();
};

// Chat with Zap AI
document.getElementById('chat-form').onsubmit = async (e) => {
    e.preventDefault();
    const userInput = document.getElementById('chat-input').value;
    const response = await fetch('/chat/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userInput })
    });
    const data = await response.json();
    document.getElementById('chat-result').innerHTML = data.response;
};
