// generate dynamic year for copyright
const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// Equalize Heights of Card Divs
const maxHeight = 0;
const cardBodyDiv = document.querySelector('card-body');

// Toggle Search Bar, Card/Table View
$(document).ready(function () {
    $("#btn-toggle").click(function () {
        $("#card-view, #table-view, #search-form").toggle();
    });
});

// Timeout for django message
$(document).ready(function () {
    setTimeout(function () {
        $('.alert').fadeOut('slow');
    }, 3000);
});
