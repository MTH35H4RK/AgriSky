// script.js

document.addEventListener("DOMContentLoaded", function() {
    // Select the Watch Now buttons
    var watchNowButtons = document.querySelectorAll('.OPSS');
  
    // Attach click event listener to each button
    watchNowButtons.forEach(function(button) {
      button.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default action of the button
  
        // Show the modal
        $('#exampleModal').modal('show');
      });
    });
  
    // Select the close button inside the modal
    var closeButton = document.querySelector('.modal-close');
  
    // Attach click event listener to the close button
    closeButton.addEventListener('click', function() {
      // Hide the modal when close button is clicked
      $('#exampleModal').modal('hide');
    });
  });
  