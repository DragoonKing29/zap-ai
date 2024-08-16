let map;

function initMap(lat, lon) {
    if (!map) {
        map = L.map('map').setView([lat, lon], 10);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
        }).addTo(map);
    } else {
        map.setView([lat, lon], 10);
    }

    L.marker([lat, lon]).addTo(map);
}

function getWeather() {
    const location = document.getElementById("weather-location").value;
    fetch(`/weather/${location}`)
        .then(response => response.json())
        .then(data => {
            const weatherDetails = `
                Location: ${data.name}<br>
                Temperature: ${data.main.temp}°C<br>
                Humidity: ${data.main.humidity}%<br>
                Wind Speed: ${data.wind.speed} m/s<br>
                Description: ${data.weather[0].description}
            `;
            document.getElementById("weather-details").innerHTML = weatherDetails;

            const lat = data.coord.lat;
            const lon = data.coord.lon;
            initMap(lat, lon);
        });
}
