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

**To Note**: The below mentioned bugs occured early in the development stage before refactoring was done. Therefore, some of the function names and provided images do not correspond to the final code.

### Fixed bugs
**Gunicorn and pyca/cryptography warnings in Github**
- I received an email from Github warning that I have gunicorn and cryptography vulnerabilities (see image). 
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
The delete button of the CRUD part of the website did not submit the user request when the button was being clicked. 
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

### Unfixed bugs
**Back button in the browser**
- Upon booking the tutorial slot the user is redirected to another page with a confirmation message showing up confirming the booking has been made.
- However,if the user clicks the backwards browser button, they are taken back to the tutorial booking page where they can click on the book button again. The functionality is in place to prevent making a repeat booking, but the page information indicating that the tutorial has been booked already only renders after the modal window is closed. 
    -  This is to be addressed at the next development stage.


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