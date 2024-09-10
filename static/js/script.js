// /* Functionality for Booking modal */
// function showBookingModal() {
//     let bookingEvent = new bootstrap.Modal(document.getElementById('bookingModal'));
//     bookingEvent.show();
// }
// // Event listener to trigger the modal when button is clicked
// document.getElementById('bookButton').addEventListener('click', function () {
//     showBookingModal();
// });


/* Functionality for delete Booking modal */
document.addEventListener('DOMContentLoaded', function () {
    console.log("DOM fully loaded and parsed.");
    function showDeleteBookingModal() {
        console.log("Show Delete Booking Modal triggered.");
        let deletebookingEvent = new bootstrap.Modal(document.getElementById('deletebookingModal'));
        deletebookingEvent.show();
    }

    // Event listener to trigger the modal when button is clicked
    let deleteButtons = document.querySelectorAll('.deleteButton');
    console.log("Found", deleteButtons.length, "delete buttons.");
    deleteButtons.forEach(button => {
        button.addEventListener('click', function () {
            console.log("Delete button clicked");
            showDeleteBookingModal();
        });
    })
});

