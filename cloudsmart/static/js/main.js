// generate dynamic year for copyright
const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// Equalize Heights of Card Divs
const maxHeight = 0;
const cardBodyDiv = document.querySelector('card-body');

// Toggle Search Form
const form = document.getElementById('showcase');
form.style.display = "none";
const searchButton = document.getElementById('search-btn');
searchButton.addEventListener('click', function() {
    form.style.display = form.style.display == "none" ? "block" : "none";
});


// Toggle Card/Table View
const tableDiv = document.getElementById('table-view');
const cardDiv = document.getElementById('card-view');
const btnTable = document.getElementById('btn-table');
const btnCard = document.getElementById('btn-card');
const searchBtn = document.getElementById('search-btn');
btnCard.addEventListener('click', function() {
    if (cardDiv.style.display === "none" || cardDiv.style.display === "") {
      tableDiv.style.display = "none";
      cardDiv.style.display = "block";
      searchBtn.style.display = "block";
    }
});
btnTable.addEventListener('click', function() {
    if (tableDiv.style.display === "none" || tableDiv.style.display === "") {
        cardDiv.style.display = "none";
        tableDiv.style.display = "block";
        searchBtn.style.display = "none";
    }
});
