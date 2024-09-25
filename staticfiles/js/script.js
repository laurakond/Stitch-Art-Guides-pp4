document.addEventListener('DOMContentLoaded', function () {

    /* Booking modal for booking a tutorial functionality on book_a_tutorial.html */
    function showBookingModal() {
        let bookingEvent = new bootstrap.Modal(document.getElementById('bookingModal'));
        bookingEvent.show();
    }
    // Event listener to trigger the modal when button is clicked
    let bookButton = document.getElementById('bookButton');
    if (bookButton) {
        bookButton.addEventListener('click', function () {
            showBookingModal();
        });
    }

    /* Code for Edit button functionality in booked_tutorials.html */
    const editButtons = document.getElementsByClassName("editButton");

    for (let button of editButtons) {
        button.addEventListener("click", (e) => {
            // Get associated booking ID
            let bookingId = e.target.getAttribute("data-booking_id");
            // Get the submit delete button elements
            this.location.href = `edit_booking/${bookingId}`;
        });
    }

    /* This part of the code was adjusted with the help of Tutor support from Code Institute.
     Code for Delete booking Modal functionality in booked_tutorials.html. */
    
    // Get all delete buttons on booked_tutorials template
    const deleteButtons = document.getElementsByClassName("deleteButton");

    // Iterate through all delete buttons on template
    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            // Get associated booking ID
            let bookingId = e.target.getAttribute("data-booking_id");
            // Get the submit delete button elements
            const deleteConfirm = document.getElementById(`deleteConfirm-${bookingId}`);

            // Get associated Delete modal
            let deleteBookingEvent = new bootstrap.Modal(document.getElementById(`deletebookingModal-${bookingId}`));
            deleteConfirm.href = `delete_booking/${bookingId}`;

            // Show associated Delete modal
            deleteBookingEvent.show();
        });
    }
});


