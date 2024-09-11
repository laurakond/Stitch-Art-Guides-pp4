// /* Functionality for Booking modal */
// function showBookingModal() {
//     let bookingEvent = new bootstrap.Modal(document.getElementById('bookingModal'));
//     bookingEvent.show();
// }
// // Event listener to trigger the modal when button is clicked
// document.getElementById('bookButton').addEventListener('click', function () {
//     showBookingModal();
// });

// This part of the code was adjusted with the help of Tutor support from Code Institute
document.addEventListener('DOMContentLoaded', function () {
    // Get all delete buttons on template
    const deleteButtons = document.getElementsByClassName("deleteButton");

    // Iterate through all delete buttons on template
    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            // Get associated booking ID
            let bookingId = e.target.getAttribute("data-booking_id");
            // Get the submit delete button elements
            const deleteConfirm = document.getElementById(`deleteConfirm-${bookingId}`);
            console.log('bookingId: ', bookingId);
            console.log("Show Delete Booking Modal triggered.");

            // Get associated Delete modal
            let deleteBookingEvent = new bootstrap.Modal(document.getElementById(`deletebookingModal-${bookingId}`));
            console.log('deletebookingEvent: ', deleteBookingEvent)

            deleteConfirm.href = `delete_booking/${bookingId}`;

            // Show associated Delete modal
            deleteBookingEvent.show();
        });
    }
});


