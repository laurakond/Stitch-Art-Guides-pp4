// /* Functionality for Booking modal */
// function showBookingModal() {
//     let bookingEvent = new bootstrap.Modal(document.getElementById('bookingModal'));
//     bookingEvent.show();
// }
// // Event listener to trigger the modal when button is clicked
// document.getElementById('bookButton').addEventListener('click', function () {
//     showBookingModal();
// });


// GET ALL DELETE BUTTONS ON TEMPLATE
const deleteButtons = document.getElementsByClassName("deleteButton");

// GET THE SUBMIT DELETE BUTTON ELEMENTS
const deleteConfirm = document.getElementById("deleteConfirm");

// ITERATE THROUGH ALL DELETE BUTTONS ON TEMPLATE
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        // GETT ASSOCIATED BOOKING ID
        let bookingId = e.target.getAttribute("data-booking_id");
        console.log('bookingId: ', bookingId)
        console.log("Show Delete Booking Modal triggered.");

        // GET ASSOCIATED MODAL 
        let deletebookingEvent = new bootstrap.Modal(document.getElementById(`deletebookingModal-${bookingId}`));
        console.log('deletebookingEvent: ',deletebookingEvent)
        
        deleteConfirm.href = `delete_booking/${bookingId}`;

        // SHOW ASSOCIATED MODAL
        deletebookingEvent.show();
    });
}

/* Functionality for delete Booking modal */
document.addEventListener('DOMContentLoaded', function () {
    console.log("DOM fully loaded and parsed.");
    // function showDeleteBookingModal(e) {
    //     let bookingId = e.target.getAttribute("data-booking_id");
    //     console.log('bookingId: ', bookingId)
    //     console.log("Show Delete Booking Modal triggered.");
    //     let deletebookingEvent = new bootstrap.Modal(document.getElementById(`deletebookingModal-${bookingId}`));
    //     console.log('deletebookingEvent: ',deletebookingEvent)
    //     deletebookingEvent.show();
    // }

    // Event listener to trigger the modal when button is clicked
    let deleteButtons = document.querySelectorAll('.deleteButton');
    console.log("Found", deleteButtons.length, "delete buttons.");
    deleteButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            console.log("Delete button clicked");
            let bookingId = e.target.getAttribute("data-booking_id");
            deleteConfirm.href = `delete_booking/${bookingId}`;
            // showDeleteBookingModal();
        });
    })
});

