# Testing for Once Upon a Time 
By Laura Kondrataite

## Contents

[Testing](#testing)

- [W3C Validator testing](#w3c-validator-testing)
- [JS Hint testing](#js-hint-testing)
- [PEP8 Linter validation](#pep8-linter-validation)
- [User input validation](#user-input-validation)
- [Bugs](#bugs)
	- [Fixed bugs](#fixed-bugs)
	- [Unfixed bugs](#unfixed-bugs)
- [Lighthouse](#lighthouse-testing)
- [User stories testing](#user-stories-testing)
- [Accessibility](#accessibility)
- [Browser testing](#browser-testing)
- [Responsiveness testing](#responsiveness-testing)
- [User testing](#user-testing)
- [Manual testing](#manual-testing)

## Testing

### W3C Validator Testing
All files were put through W3C Markup Validation Service & W3C CSS Valisation Service. Images as per below:
- **W3C Markup**:
    <details>
    <summary></summary>

    ![username-validation]()
    </details>

    <details>
    <summary></summary>

    ![username-validation]()
    </details>

    <details>
    <summary></summary>

    ![username-validation]()
    </details>

    <details>
    <summary></summary>

    ![username-validation]()
    </details>

- **W3C CSS**:
    <details>
    <summary></summary>

    ![username-validation]()
    </details>

### JS Hint Testing

### PEP8 Linter validation
The code was run past CI Python Linter program throughout the development stage of the application and once the code was finalised. The final results for all python files returned without any errors as per images below:

[Return to Table of Contents](#contents)


### User input validation

There are several user inputs throughout the application, therefore, validating data was crucial for the functionality of the application. 
- Each part of user input was tested during and after the development stage.
- The below screenshots display all viable entries and responses to incorrect data.

    <details>
    <summary></summary>

    ![username-validation]()
    </details>

    <details>
    <summary></summary>

    ![username-validation]()
    </details>

    <details>
    <summary></summary>

    ![username-validation]()
    </details>

    <details>
    <summary></summary>

    ![username-validation]()
    </details>

[Return to Table of Contents](#contents)

## Bugs

**To Note**: The below mentioned bugs occured early in the development stage before refactoring was done. Therefore, some of the function names and provided images may not correspond to the final code.

### Fixed bugs
**Gunicorn and pyca/cryptography warnings in Github**
- I received a warning from Github that I have Gunicorn and cryptography vulnerabilities (see image). 
- After receiving the second warning I managed to get John from Tutor support to help me out. 
- With his encouragement, I uninstalled and re-installed the two dependencies and ensured that the changes have not affected the functionality of the website in the locally and once deployed.

![add image here]()

**url path <slug:slug>/<int:id> not rendering**
<details>
<summary></summary>

![username-validation]()
</details>

- I received the above error when trying to render a url path for each individual tutorial booking.
- This part of the code proved tricky as I was not familiar with JavaSript's Full Calendar functionality. 
    -  I had help from Tim Nelson (mentioned in the acknowledgements) on how to make the code work as majority of the resources that I found were using jQuery syntax.
    - I managed to make the path work by implementing Full Calendar's extendedProps property. This allowed me to access deeper dependencies within my set models. 

<details>
<summary>Correct code</summary>

```
let eventId = info.event.id;
let eventSlug = info.event.extendedProps.slug;
let eventUrl = `/book-a-tutorial/${eventSlug}/${eventId}/`;
location.href = eventUrl;
```

</details>

**Rendering User specific bookings**
- Upon initial set up of My bookings page, when trying to render user specific tutorial bookings, I received the following error:

```
MultipleObjectsReturned at /booked_tutorials/
get() returned more than one Booking -- it returned 3!
```

- The code that caused the error was:
```
def my_tutorials(request):
    """
    function that displays booked tutorial page.
    """
    queryset = Booking.objects.all()
    booking = get_object_or_404(queryset)

    return render(
        request,
        'home/my_tutorials.html',
        {"booking": booking,}
         )
```

- Upon reading Django documentation on user, I realised that I needed to target each user information through user authentication. The below code has fixed the issue:

```
def my_tutorials(request):
    """
    function that displays booked tutorial page.
    """
    bookings = Booking.objects.filter(user=request.user)

    return render(
        request,
        'home/my_tutorials.html',
        {"bookings": bookings,}
         )
```

**Error pages not rendering**
- In order to render the error pages, I had to adjust the settings.py code from

```
TEMPLATES = [
    {'BACKEND': 
    'django.template.backends.django.DjangoTemplates',
    'DIRS': [TEMPLATES_DIR],
    ...
    }]
```
to 

```
TEMPLATES = [
    {'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        os.path.join(BASE_DIR, "templates"),
        os.path.join(BASE_DIR, "templates", "allauth"),
        ],
        ...
        }]
```
- I references a couple of Code Institute July 2024 Hackathon projects in order to make the code work. Notably: 
    - [United Events](https://github.com/hannahro15/July24Hackathon-United-Events/blob/main/united/settings.py) project

**Delete booking button not working**
- The delete button of the CRUD part of the website did not submit the user request when the button was being clicked. 
- I managed to resolve this by removing ```request.method == "POST"``` from the if statement and altering the code to the following:
    ```
    @login_required
    def delete_booking(request, booking_id):
    """
    Function that deletes the tutorial booking.
    """
    
    booking = get_object_or_404(Booking, pk=booking_id)
    if booking.user == request.user: 
        booking.delete()
        messages.add_message(request, messages.SUCCESS, 'Booking deleted')
        return redirect('booked_tutorials')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own bookings.')
        return redirect('booked_tutorials')
    ```

**Uncaught TypeError: cannot read properties of null**
I was getting the following error when on the My Tutorials page. 

![properties of null]()
The code that was throwing an error was this:
```
    /* Functionality for Booking modal on book_a_tutorial.html */
    function showBookingModal() {
        let bookingEvent = new bootstrap.Modal(document.getElementById('bookingModal'));
        bookingEvent.show();
    }
    // Event listener to trigger the modal when button is clicked
    let bookButton = document.getElementById('bookButton');
    bookButton.addEventListener('click', function () {
        showBookingModal();
    });
```
- This error was referring to an element that was being used for a differerent button/modal on the book_a_tutorial.html page. 

- I adjusted the code logic by including the if clause as suggested in the Stackoverflow chat thread: [Cannot read property 'addEventListener' of null](https://stackoverflow.com/questions/26107125/cannot-read-property-addeventlistener-of-null).
    -  This video has was also helpful to refresh my memory on the how/where to place my code so that it is being rendered properly: https://www.youtube.com/watch?v=yCWMRYCfpfE

```
 /* Functionality for Booking modal in book_a_tutorial.html */
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
```

**Delete booking id instance not showing properly in the url**

- I noticed that when hovering over each delete button inside the Delete Modal, the instance url was displaying ‘#’ instead of the id number:

![booked_tutorials/#]()
- I adjusted the anchor tag’s id with a `session.id` in my_tutorials.html:
    - ``` <a id="deleteConfirm-{{ session.id }}" href="#" class="btn btn-danger">Delete booking</a> ```
- Inside script.js, I adapted the syntax of the `deleteBookingEvent` element to the `const deleteConfirm = document.getElementById(deleteConfirm-${bookingId});`:
    - This ensured that the server was showing the individual tutorial booking instance.
    ![correct booking instance]()

**Conditional message filtering**
- When testing different message prompts based on booked tutorials when editing the booking, a wrong message was appearing when only the same tutorial title booking was available. The message that was being prompted was “Pick another date or choose a different tutorial.”
- This happened because there was an error in filtering other_tutorials query set. I was getting the test tutorial query set inside other_tutorials when I shouldn’t have.
- To fix it I added exclude() method to other_tutorials queryset:
    ```other_tutorials = TutorialDate.objects.filter(
        booking__isnull=True,
        tutorial_date__gte=date_now
        ).exclude(tutorial=tutorial)```

**Error messages for unauthorised access not displaying**
- When testing defensive programming, some of the error messages were not showing up where expected and were only redirecting to an appropriate page. 

    - I resolved this by removing @login_required decorator and applying user.is_authenticated to allow the messages appear where required.
- Once that was resolved, I noticed that some of the error messages were appearing where they were not meant to. 
    - To solve this, I moved the authentication code up within the view functions in order to ensure that the check is carried out first thing when the view loads.
    
    ![Incorrect error rendering]()

    ![fixed code placement image]()

**Favicon not rendering**
- Upon upload of all files, the favicon was not properly rendering when the the website was loaded. 
    - I resolved this issue by removing the type attribute from the tags. I found the solution on [Stack Overflow](https://stackoverflow.com/questions/66918079/favicon-not-loading-in-django#:~:text=I%20had%20the%20same%20problem.,tags%2C%20the%20favicon%20started%20working) channel.

**Comparing the current time to event time**
- I wanted to compare the user’s current time and date with the tutorial’s set time and date. My initial code was only comparing the dates excluding the hours. Therefore, any tutorial that was clicked on on the current day, even when the time of the tutorial has passed, it would not prompt the expired event modal
    - I managed to resolve this by removing the `today.setHours(0, 0, 0, 0);` from the eventClick function, the code directly compared the current date and time with the event’s date and time. 

    <details>
    <summary>I found the following resources helpful to accomplish this:</summary>

    - [Freecodecamp: javascript date comparison](https://www.freecodecamp.org/news/javascript-date-comparison-how-to-compare-dates-in-js/)
    - [MDN web docs: Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)
    - [Geek for Geeks JavaScript Date comparison](https://www.geeksforgeeks.org/compare-two-dates-using-javascript/)
    - [Freecodecamp: compare two dates in javascript](https://www.freecodecamp.org/news/compare-two-dates-in-javascript/#:~:text=In%20JavaScript%2C%20you%20can%20use%20comparison%20operators%20like,to%20their%20respective%20corresponding%20timestamps)
    - [StackOverflow: compare string with todays date in javascript](https://stackoverflow.com/questions/15063670/compare-string-with-todays-date-in-javascript)
    ![username-validation]()
    </details>

        

**Field ‘id’ expected a number but got SimpleLazyObject**

- I received this error when trying to check if /my-tutorials/ url path was accessible to annonymous users. Upon quick research, I realised that I needed to alter my request in views.py by adding a user specific id, and also apply @login_required above the my_tutorials function.
    - This seems to have worked.

    ![id expected a number error image]()
    <details>
        <summary>I found the following resources useful:</summary>
        
    - [Stackoverflow: typerror field id expected a number but got django contrib auth](https://stackoverflow.com/questions/62966136/typeerror-field-id-expected-a-number-but-got-django-contrib-auth-models-anon)
    
    </details>
    
**Empty Past Tutorials list in My Bookings page:**
- When working on My Bookings page, I noticed that the template was not rendering appropriate information where needed. I tried checking if the upcoming_sessions and past_sessions lists were coming back with correct information.
- After running the print statements (code1) I realised that past_sessions list was not being populated. 
    <details>
            <summary>Error code</summary>

        @login_required
        def my_tutorials(request):
            """
            Function that displays booked tutorial page.
            """
            bookings = Booking.objects.filter(user=request.user.id)
            current_datetime = datetime.now()
            past_sessions = []
            upcoming_sessions = []

            for booking in bookings:
                event_datetime = datetime.combine(
                    booking.tutorial_date.tutorial_date, 
                    booking.tutorial_date.start_time
                    )
                print(f"Booking: {booking.tutorial_date.tutorial.title} - Event Date: {event_datetime} - Current Date: {current_datetime}")
            if event_datetime > current_datetime:
                upcoming_sessions.append(booking)
            elif event_datetime < current_datetime:
                past_sessions.append(booking)
                
                
            print("Upcoming Sessions:", upcoming_sessions)
            print("Past Sessions:", past_sessions)

            return render(
                request,
                'home/my_tutorials.html',
                {"past_sessions": past_sessions,
                "upcoming_sessions": upcoming_sessions,
                }
                )    

    </details>

- Going through the code, I noticed that I was appending to appropriate list outside of the for statement. I moved the if statement inside the for statement and the issue was resolved.

    <details>
            <summary>Fixed code</summary>


        @login_required
        def my_tutorials(request):
            """
            Function that displays booked tutorial page.
            """
            bookings = Booking.objects.filter(user=request.user.id)
            current_datetime = datetime.now()
            past_sessions = []
            upcoming_sessions = []

            for booking in bookings:
                event_datetime = datetime.combine(
                    booking.tutorial_date.tutorial_date, 
                    booking.tutorial_date.start_time
                    )
                print(f"Booking: {booking.tutorial_date.tutorial.title} - Event Date: {event_datetime} - Current Date: {current_datetime}")
                if event_datetime > current_datetime:
                    upcoming_sessions.append(booking)
                elif event_datetime < current_datetime:
                    past_sessions.append(booking)
                
                
            print("Upcoming Sessions:", upcoming_sessions)
            print("Past Sessions:", past_sessions)

            return render(
                request,
                'home/my_tutorials.html',
                {"past_sessions": past_sessions,
                "upcoming_sessions": upcoming_sessions,
                }
                )   

    </details>

**Cannot book booked events(book_a_tutorial) - calendar view:**
- I was trying to implement functionality for the already booked events to not be accessible/not to be bookable. 
- I managed to make the “already booked” modal appear by adjusting the JS code in book_tutorial.html, but the modal was popping up for all future events despite them being booked or not. I realised that I was not displaying/applying the logic of a booked event correctly.
- I finally managed to resolve this by applying django translator yesno string literals passed to tags and filters. The following resources helped to understand and make the code work:
    - [Stackoverflow: django template boolean variable](https://stackoverflow.com/questions/12395579/my-django-template-boolean-variable-isnt-working-as-expected-in-javascript)
    - [Django docs - translators](https://docs.djangoproject.com/en/dev/ref/templates/builtins/#yesno)

**Filter Tutorial dates that are not booked by anyone**
- I realised that the code was showing future tuturials that have been booked by other users. If the user where to select the already booked tutorial from the drop down, then there would be a double booking from two different users. I amended the code by applying __isnull=False for filtering future_tutorials.
- Instead of looking at excluding the logged in user’s booking, this way I looked for any Tutorial dates that have a booking and excluded them from the filtered result. Thus only Tutorial dates that don’t have a booking related to them were given back in the form drop down.

code filtering all future tutorials:

```
future_tutorials = TutorialDate.objects.filter(
            tutorial_date__gte=current_date
            ).exclude(booking__user=self.user)
```

code filtering future tutorials that are available/not booked:

```
future_tutorials = TutorialDate.objects.filter(
            tutorial_date__gte=current_date
            ).exclude(booking__isnull=False)
```

**Reappearing horizontal scroll bar**
- When creating the About page, I noticed that the page sometimes has a horizontal scroll bar. After having numerous attempts at altering the style, I realised that the body was set to width: 100dvw.
    - I fixed the issue by changing the width to 100%.

**Grid layout error**
- I noticed the grid layout for upcoming tutorials in My Bookings page was not working properly. 
    <details>
    <summary>delete booking modal error image</summary>

    ![delete booking modal error](documentation/images/error_images/my-tutorials-error.png)
    </details>

    - I realised that the layout was being affected by the modal which was nested inside the for loop. 
    - After isolating elements one by one, I realised that the issue was caused by the form tag surrounding the modal, I have removed. 
    <details>
    <summary>delete booking modal fixed image</summary>

    ![fixed delete booking modal](documentation/images/error_images/my-tutorials-fixed.png)
    </details>

**Django alert messages rendering without colour**
- Upon testing the functionality of the colours I noticed that they are not displaying any color.
    - I solved the problem by including `alert-{{ message.tags }}` to the code. I found the solution on [Stackoverflow](https://stackoverflow.com/questions/55202684/does-bootstrap-django-error-message-has-no-red-color).

### Unfixed bugs
**Back button in the browser**
- Upon booking the tutorial slot the user is redirected to another page with a confirmation message showing up confirming the booking has been made.
- However,if the user clicks the backwards browser button, they are taken back to the tutorial booking page where they can click on the book button again. The functionality is in place to prevent making a repeat booking, but the page information indicating that the tutorial has been booked already only renders after the modal window is closed. 
    -  This is to be addressed at the next development stage.

**Cut off Tutorial title in the Calendar view**
- I noticed that the tutorial title is cutting off in the Calendar view if it is over a certain lenght.
    - After searching for a solution I was able to make the event title show in a second row. The code used for this was found on [Stackoverflow](https://stackoverflow.com/questions/33406697/fullcalendar-v2-event-title-cut-off-in-month-view):
    ```
    .fc-daygrid-event .fc-event-title {
        white-space: normal;
        text-overflow: ellipsis;
        max-height:20px;
  }
  .fc-daygrid-event:hover .fc-event-title {
        max-height:none !important;
  }
    ```
    - However, this makes the whole calendar view jump. This will be addressed at the next development stage.

[Return to Table of Contents](#contents)

### Lighthouse testing

[Return to Table of Contents](#contents)

### User stories testing

[Return to Table of Contents](#contents)

### Accessibility

[Return to Table of Contents](#contents)

### Browser testing

[Return to Table of Contents](#contents)

### Responsiveness testing

[Return to Table of Contents](#contents)

### User testing


[Return to Table of Contents](#contents)

### Manual testing
After the development stage of the application, I went through each feature ensuring that the website is working as intended.



[Return to Table of Contents](#contents)

[Return to the main README.md](README.md)