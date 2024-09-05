function showBookingModal() {
    let bookingEvent = new bootstrap.Modal(document.getElementById('bookingModal'));
    bookingEvent.show();
}

// Event listener to trigger the modal when button is clicked

document.getElementById('bookButton').addEventListener('click', function () {
    showBookingModal();
});