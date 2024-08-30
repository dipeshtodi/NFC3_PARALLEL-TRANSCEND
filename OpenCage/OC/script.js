const shelters = [
    { name: "The Society for The Prevention of Cruelty to Animals", address: "Nr Mahatma Gandhi Hospital, Dr Ss Ra Parel, Opp Md College, Mumbai, Maharashtra 400012" },
    { name: "Bai Sakarbai Dinshaw Petit Hospital for Animals", address: "Dr. S. S. Rau Road, Mumbai, Maharashtra 400012" },
    { name: "Animal Matter to Me", address: "B-601, Building Number 1, Blue Meadows, Off Jvlr Road Shyam Nagar, Jogeshwari East 400, Mumbai, Maharashtra 400060" },
    { name: "Bombay Animal Rescue", address: "B-403, Kanti Apts, Mount Mary Road, Bandra West, Mumbai, Maharashtra 400050" },
    { name: "Animal Rescue & Shelter Foundation", address: "R-3/8A Parth CHS LTD, Poonam Nagar Plot NO. 175, Mmrda Colony, Mumbai, Maharashtra 400093" },
    { name: "YODA Centre", address: "3, Swami Vivekanand Road, Mahim Koliwada, Mahim West" }
];

const map = L.map('map').setView([19.076, 72.8777], 13); // Center the map on Mumbai

// Add a tile layer to the map
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

function loadShelters() {
    shelters.forEach(shelter => {
        fetch(`https://api.opencagedata.com/geocode/v1/json?q=${encodeURIComponent(shelter.address)}&key=51e897210dab434380b010e9541dbb82`)
            .then(response => response.json())
            .then(data => {
                if (data.results.length > 0) {
                    const location = data.results[0].geometry;
                    const position = [location.lat, location.lng];
                    addMarker(position, shelter.name);
                    addShelterToList(shelter.name, shelter.address, position);
                }
            })
            .catch(error => console.error('Error:', error));
    });
}

function addMarker(position, title) {
    L.marker(position)
        .addTo(map)
        .bindPopup(title)
        .openPopup();
}

function addShelterToList(name, address, position) {
    const listItem = document.createElement("li");
    listItem.innerHTML = `
        <strong>${name}</strong><br>
        ${address}<br>
        <button class="view-button" onclick="focusMarker(${position[0]}, ${position[1]})">View on Map</button>
        <button class="connect-button" onclick="connectToShelter('${name}')">Connect</button>
    `;
    document.getElementById("shelter-list-items").appendChild(listItem);
}

function focusMarker(lat, lng) {
    map.setView([lat, lng], 15);
}

function connectToShelter(name) {
    // Open the owner's email or contact form
    window.location.href = `mailto:owner@example.com?subject=Inquiry about ${name}`;
}

// Initialize the map with shelters
document.addEventListener('DOMContentLoaded', loadShelters);
