# Stitch Art Guides

![main-image]()

(By Laura Kondrataite)

Are you practicing crafts or simply interested in dipping your toes in the vast world of modern embroidery? Then look no further. Enter the Stitch Art Guides! This website is created with avid stitchers and wondering newbies in mind. 

Art Stich Guides provides a number of various tutorials on how to set up and get started with your first project whether it is a simple cross stitch sampler or a more advanced project. 

All are welcome.

Live site can be found [here](https://stitch-art-guides-pp4-5a679feed1e1.herokuapp.com/).

## Table of Contents

[Design](#design)
- [Target Audience](#target-audience)
- [User Stories](#user-stories)
- [Flowcharts](#flowcharts)
- [Wireframes](#wireframes)
- [Colour palette](#colour-palette)
- [Fonts styles](#font-styles)

[Agile Methodology](#agile-methodology)

[Features](#features)
- [Existing Features](#existing-features)
- [Features Left to Implement](#features-left-to-implement)

[Tools and Technologies](#tools-and-technologies)
- [Languages Used](#languages-used)
- [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)

[Testing](#testing)

[Deployment](#deployment)
- [Github](#github)
    - [How to Fork](#how-to-fork)
    - [How to Clone](#how-to-clone)
- [Heroku](#heroku)

[Credits](#credits)
- [Content](#content)
- [Refactoring](#refactoring)
- [General resources](#general-resources)
- [Acknowledgments](#acknowledgments)
- [Code inspiration](#code-inspiration)

[Return to Table of Contents](#table-of-contents)

## Design
### Target Audience

The primary target audience for the game is:
- persons of any gender aged 16+ who enjoy crafts, 
- first time cross-stitchers,
- anyone looking for guidance on how to progress in their cross-stitch journey. 

No background, geographical location or income has been specified for the target audience. 

### User Stories

As a first time user:

<br>

As a user:

### Flowcharts
I used [Lucidchart](https://lucid.app/) for creating the logic and structure of the game. The flowchart of the project has had to be split into two flowcharts (minimum viable product & future feature) due to limited use of blocks per one chart. Chapter 3 is a future feature. 

- MVP flowchart:

![flowchart-mvp]()

- Future feature flowchart (Chapter 3):

![flowchart-mvp]()

### Wireframes
The following wireframes show the initial idea of how the website would look on three different devices: mobile, tablet/iPad and laptop/desktops. 

They also convey an idea of how the user  navigate between different pages of the website.

<details>
    <summary>Mobile view</summary>

    ![mobile view]()
</details>
<details>
    <summary>Tablet view</summary>

    ![tablet view]()
</details>
<details>
    <summary>Desktop/Laptop view</summary>

    ![desktop view]()
</details>


### Color palette
The following palette was used to ensure the contrast is achieved between main parts of the website:

![color-palette]()

### Font styles
[Google fonts](https://fonts.google.com/) was used to source the fonts for the website. These are:

- font1 - was used as the main content font.
- font2 - was used for the logo and provide accent pieces to the website.

![font screenshots]()

[Return to Table of Contents](#table-of-contents)


## Agile Methodology

[Return to Table of Contents](#table-of-contents)


## Features
### Existing Features

**Landing page**

**The Header**

![header]()

- Featured across all the pages, the Header is fully responsive and presents the user with main pages that are required. To the left of the header you find:
    - The Logo

- To the right of the header the remainder of the pages:
    - Home Page
    - About Page
    - Tutorial List Page
    - Register Page
    - Login Page

- Upon Registration or Log in, the user's log in name and additional two pages are revealed in the header. This creates a sense of personalisation and indicates additional website functionality for the registered users.
    - Book Tutorial Page
    - My Tutorials Page


**The Footer**

![footer]()

- The Footer features social media links for that are related to the website and provides a copyright line indicating that this website was created for educational purposes only. 

**The Landing Page**

![landing page]()

- The Landing page greets the user with a simple design, a brief blurb indicating the purpose of the website, and the main call to action button that leads the user to the Tutorial List page. 

**About page**

![about page]()

- The About page displayes a profile picture of the instructor and provides a brief introduction. A further call to action button is used allowing the user to explore different tutorials that are being offered. 


**Tutorial list**
- If the user chooses to leave the game after reading the instructions, the screen displays "Thank you for playing! see you next time." 
    - The user needs to click on the "Run program" button at the top if they wish to reload the program.

![tutorial list]()

**User authentication**

 <details>
    **<summary>Register</summary>**

    ![register]()
</details>

 <details>
    **<summary>Login</summary>**

    ![login]()
</details>

 <details>
    **<summary>Logout</summary>**

    ![logout]()
</details>

 <details>
    **<summary>Admin panel</summary>**

    ![admin panel]()
</details>


**Tutorial Calendar**
- Once the user data is captured, the screen clears the previous content, and loads the main logo together with the beginning of the story. 
    - The user will see that their provided username is generated within the storyline at the end of the first introduction paragraph. 

![calendar]()

**My Tutorials page**
- Chapter 1 section loads straight after the story introduction. 
- The logo provides a clear indication which area within the game play the user is at. 
- Here the user is prompted to choose between two possible outcomes to proceed with the gameplay. 

![my tutorials]()

**Error pages**

<details>
    **<summary>400 error page</summary>**

    ![400 error page]()
</details>

<details>
    **<summary>403 error page</summary>**

    ![403 error page]()
</details>

<details>
    **<summary>404 error page</summary>**

    ![404 error page]()
</details>

<details>
    **<summary>500 error page</summary>**

    ![500 error page]()
</details>



### Features Left to Implement

- Allow the user to submit a customised tutorial request form. This would allow to address any individual needs of a crafter.  
- Implement comment and review features for each tutorial.
- Develop an in depth user participation and use of the website by providing an ability to share or sell their own craft projects. This includes allowing the user to submit their project photos, titles, author’s name, and so on.
- Filter tutorial drop down menu in the edit tutorial page in order to show just that tutorial's future dates for picking from. Currently this feature is being handled by applying different notificaitons to to the user once they enter edit booking page.

[Return to Table of Contents](#table-of-contents)

## Tools and Technologies
### Languages Used

- This project was created using full stack approach, including Python, Django, HTML, and CSS.
- Markdown language was used for creating the README and TESTING files.

### Frameworks, Libraries and Programs Used

The following resources were used to help implement the website:
- [Lucidchart](https://lucid.app/) for creating flowchart of the game.
- [GitHub](https://github.com/) for creating and storing files and folders of the website.
- **Git** was used for version control.
- **VScode** editor for writing the code.
- [CI Python Linter](https://pep8ci.herokuapp.com/#) for validating and checking my code for best code practices.
- [Heroku](https://www.heroku.com) for accessing and storing my application game.
- [Django](https://www.djangoproject.com/) Python framework for the overall project implementation.
- [Bootstrap](https://getbootstrap.com/) CSS framework that allowed to implement various styled elements, including modals. It was also used for quick and easy styling of the overall website.
- [Whitenoise](https://whitenoise.readthedocs.io/en/stable/index.html) Python library used for handling static files.
- [Django allauth](https://allauth.org/) authentication solution for Django framework used for allowing users to register and login.
- [Django summernote](https://summernote.org/) Javascript library used for providing useful editing tools for Django admin site. 
- I used the following libraries for the project:
    - **Full Calendar** JavaScript calendar open source that allowed to display available tutorial bookings in a calendar view.  
    - **os** library system method allowed to clear the screen for better user experience when displaying the game.

Other libraries and dependencies can be seen in the requirements.txt file. 


 [Return to Table of Contents](#table-of-contents)

## Testing

The game application went through extensive testing during the development and deployement stages. 
- See [TESTING.md](TESTING.md) file for full testing and validation information.

[Return to Table of Contents](#table-of-contents)


## Deployment
This website was deployed using GitHub pages and Heroku website. To deploy the project, follow the steps below:

### Github
1. Login to GitHub and navigate to the main repository page.
2.  Click on the chosen repository [repository-name]().
3. Once inside the repository, click on the "Settings" tab above the repository title displayed around the middle of the page.
4. Select "Pages" tab on the left side navigation menu.
5. In the "Source" section (middle of the screen), select "main" or "master" branch, then "root" folder and click "save" button.
6. The GitHub page site will be deployed.

It might take a few minutes to generate the "live" website link.

The live link to the game can be found [repository name]().

#### How to Fork
To fork the repository in Github:
1. Follow steps 1 & 2 as above. 
2. Once inside the chosen repository, click the "fork" button in the top right corner above the "About section".

#### How to Clone
To clone the repository in Github:
1.  Follow steps 1 & 2 as in the deployment section above.
2.  Click on the "Code" button (often a bright color that stands out) in the top right corner just above the "commits" history. 
    - Select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
3.  Open the terminal in your chosen code editor and change the current working directory to the location you want to use for the cloned directory.
4.  Type 'git clone' into the terminal and then paste the copied link and press enter.

### Heroku
To deploy to the Heroku website, follow the steps below:
1. Navigate to https://www.heroku.com platform website.
2. Create or log in to your account.
3. Once on your dashboard:
    1) if you don't have any projects created yet, there should be a "Create a new app" prompt in the middle of the screen.
    2) if you have some projects already, click on the "New" tab on the top right corner of the screen just below the profile bauble. 
4.  Enter a unique application name for your project and select the region you are based in. Click "create app".
5. Once insde the app, select "Settings" button from the menu in the middle. It's important to edit the "Settings" tab before deploying the project: 
    1. Click on "Reveal Config Vars" and enter the following:
        
        1) if you are using any APIs you will need to copy paste your creds.json details:
            - in the "key" box type "CREDS". 
            - in the "value" box copy the contents of your creds.json file: 
            - click "Add".

        2) type in PORT to the "key" box, and 8000 to the "value" box:
            - click "Add".

    2. Add Buildpacks below Config Vars. Click on "Add buildpack":

        1) First, select Python and click "Add buildpack".
        2) Second, select node.js and click "Add buildpack".
        
        **Note:** Python has to be listed first (at the top) of the two packs.
6. Once step 5 is done, navigate to the "Deploy" tab a the top of the screen to the left of where the Settings tab is located.
7. Click on "Github" icon under "Deployment method", and connect Heroku to your Github account. 
8. Once the accounts are connected you can choose between automatic or manual deployment:

    1) Automatic deplyoment will automatically update your app once you use "git push" command in  your IDE. 

    2) Manual deployment will require you to manually "push" the changes you made in the IDE to the Heroku system.

[Return to Table of Contents](#table-of-contents)

## Credits

### Content

### Refactoring

### General resources:
Whilst working on this project I relied on Django documentation and other resources to deepen my knowledge and gain a better understanding how to build a full-stack website. 

- ERD & flowcharts:
    - [Lucid flowcharts Youtube video](https://www.youtube.com/watch?v=hktyW5Lp0Vo)
    - [Lucid Software database tutorial for beginners](https://www.youtube.com/watch?v=wR0jg0eQsZA)
    - [Decomplexify](https://www.youtube.com/watch?v=GFQaEYEc8_8)
    - [Decomplexify Learn Database normalisation Youtube video](https://www.youtube.com/watch?v=GFQaEYEc8_8)
- Models:
    - [Geeks for Geeks: Django models](https://www.geeksforgeeks.org/django-models/)
    - [MDN web docs: Using models](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models) 
    - [W3Schools Django update model](https://www.w3schools.com/django/django_update_model.php)
    - [Django forum - how do I load multiple models items into a single view](https://forum.djangoproject.com/t/how-do-i-load-multiple-models-items-into-a-single-view/919/2)
- User flows:
    - [Figma user flow kit](https://www.figma.com/community/file/830510773896272856/user-flow-kit)
    - [Creatly common mistales to avoid when creating user flow diagrams](https://creately.com/guides/user-flow-diagram/#common-mistakes-to-avoid-when-creating-user-flow-diagrams)
- I looked at a few resources for calendar view implementation. 

- Restricting authorised access
    - The following chat threads on Stackoverflow were very useful when trying to determine which login restrictions to use for defensive programming:
    - [@login_required and is_authenticated() -- When to use which in Django?](https://stackoverflow.com/questions/22488601/login-required-and-is-authenticated-when-to-use-which-in-django#:~:text=login_required%20is%20applied%20on%20a,is%20logged%20in%20or%20not)
    - [Using the Django authentication system](https://docs.djangoproject.com/en/5.1/topics/auth/default/) was also really helpful for determining what aspects were useful for restricting access. 
- Implementing calendar view for tutorial display:
    - [Real Python: The Python calendar module](https://realpython.com/python-calendar-module/)
    - [Python documentation: calendar](https://docs.python.org/3/library/calendar.html)
    - [Geeks for Geeks Python calendar module](https://www.geeksforgeeks.org/python-calendar-module/)
    - [Codemy Django Wednesdays Youtube tutorial](https://www.youtube.com/watch?v=4EJlrweJE-M)

- Python datetime:
    -  [Python documentation datetime - basic date and time](https://docs.python.org/3/library/datetime.html#format-codes)
    - [Geeks for Geeks Isoformat() method](https://www.geeksforgeeks.org/isoformat-method-of-datetime-class-in-python/)

- Creating Django error pages:
    - [Geek for geeks: Django creating a 404 error page](https://www.geeksforgeeks.org/django-creating-a-404-error-page/?ref=oin_asr1)
    - [Geeks for geeks: handling custom error page](https://www.geeksforgeeks.org/python-django-handling-custom-error-page/)

- Queryset.exists():
    - [Dev community: queryset.exists() more efficient than queryset.count()](https://dev.to/codereviewdoctor/why-queryset-exists-is-more-efficient-than-queryset-count-2f3h)
    - [Django documentation: check if record exists in model](https://forum.djangoproject.com/t/check-if-record-exists-in-model/10712/5)
    - [Reddit: Checking a place is already booked or not based on time](https://www.reddit.com/r/django/comments/1bb6zin/checking_a_place_is_already_booked_or_not_based/)

### Acknowledgments

My thanks go to: 
- My mentors: 
    - [Martina Terlevic](https://github.com/SephTheOverwitch) for helping to come up with initial project idea, giving suggestions for troubleshooting, and providing reassurance when my confidence stumbled (which has happened many a time).
    - [Iuliia Konovalova](https://github.com/IuliiaKonovalova) for helping to find a solution on how to implement parts of CRUD functionality.
- My fellow student, [Vernell Clark](https://github.com/VCGithubCode) for troubleshoot and providing a shoulder to cry on when things got really rough.
- [Tim Nelson](https://github.com/TravelTimN) for the advice on the intricacies of JavaScript Full Calendar & general advice.
- Another fellow student [Declan](https://github.com/Declan444) for helping to understand models and overall morale boost when it was needed.
- Tutor support team for helping out with project set up and other quirky bits. A big shout out goes to:
    - John for assisting to address Gunicorn and pyca/cryptography warnings on Github [more details noted in fixed bugs section in TESTING.md](TESTING.md). 
    - Holly for providing guidance and advice on Whitenoise and staticfiles inner workings.
    - Sarah for helping to troubleshoot delete part of CRUD functionality and find a way how to navigate tutorial editing.
    - Thomas for giving an idea of how to implement CRUD. 

### Code Inspiration
- The project was inspired and based on some parts of Code Institute's I think therefore I blog walkthrough project. 
    -  Credits are also noted within the code.
- The calendar display was inspired by United Events team's [project](https://github.com/hannahro15/July24Hackathon-United-Events) that featured in Code Institute's July hackathon. 


[Return to Table of Contents](#table-of-contents)