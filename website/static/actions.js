// User profile toggle
let subMenu = document.getElementById('subMenu');

function toggleUserProfile(){
    subMenu.classList.toggle("open-menu");
}

// sidebar active hover click
$(".sidebar ul li").on('click', function(){
    $(".sidebar ul li.active").removeClass('active');
    $(this).addClass('active');
});


// toggle for sidebar hamburger menu
$('.open-btn').on('click', function(){
        $('.sidebar').addClass('active');
    });

$('.close-btn').on('click', function(){
    $('.sidebar').removeClass('active');
});


// Add slideDown animation to dropdown when expanding.
$('.dropdown').on('show.bs.dropdown', function() {
    $(this).find('.dropdown-menu').first().stop(true, true).slideDown();
});

// Add slideUp animation to dropdown when collapsing.
$('.dropdown').on('hide.bs.dropdown', function() {
    $(this).find('.dropdown-menu').first().stop(true, true).slideUp();
});


// display selected merchant on the dropdown button
$("#selected-merchant a").on('click', function(){
    let selectedMerchant = $(this).text();
    $("#display-selected-merchant").text(selectedMerchant);
});

// display selected date range on the dropdown button
$("#selected-date a").on('click', function(){
    let selectedDate = $(this).text();
    $("#display-selected-date").text(selectedDate);
});

// display the selected date range on the transactions line graph card
$("#selected-date a").on('click', function(){
    let transactionsInTheLast = "Transactions in the ";
    let selectedDate = $(this).text();
    $("#card-title-display").text(transactionsInTheLast + selectedDate);
});