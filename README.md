![logo1](static/img/logo1.png)
### An Event Registration Website made using the Django Framework
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/check-it-out.svg)](https://forthebadge.com)
### Deployed on Heroku
![Heroku](http://heroku-badge.herokuapp.com/?app=eventzforu&style=flat&svg=1)
Check out the [website](https://eventzforu.herokuapp.com/)
# Features of the website
**v0.0**
> 1. The admin can dynamically add the events. The date, time, image(based on the title given) and the unique id will be generated on its own. the admin has to give a title, header, basic description, location, organizer details and tags related to the event.
>
> 2. The participant can view the upcoming events and then fill the form in the Particpants page to register for a particular event
>
> 3. The participant can only fill the Participants form when he/she is logged in.
>
**What's new in v0.1**
> 1. User can now login with their Google or GitHub accounts.
>
> 2. A new logo added in the Navbar
>
> 3. Font size of text in navbar and footer increased for better viewing
>
**What's new in v0.3**
>1. Added reCAPTCHA in the participant form.
>
>2. Sending an email as soon as the form is filled.
>
>3. Improvements in the UI of the HomePage.
>
>4. Search bar added in the HomePage.
>
>5. Tags, Location, Organizer details added for each event.
>
**Future plans**
> Integrate payment option using Stripe or PayTM
>
> Add ML
>
> Better profile page for the users
# Installation
### 1. Install python
> https://realpython.com/installing-python/
### 2. Clone this repo into your local machine 
> git clone https://github.com/AdityaAshvin/EventsForU.git
### 3. Install django
> pip install django
### 4. Install required dependencies
> pip install -r requirements.txt
### 5. Final Step
> go to the directory where manage.py is located and run the following command
>
>> python manage.py runserver
# Screenshots
### v0.0
### HomePage when the User is logged in
![homepage1](screenshots/ss5.JPG)
![homepage2](screenshots/HomePage2.JPG)
### HomePage when the User is not logged in
![homepage3](screenshots/ss1.JPG)
### Participant Page when the user is logged in
![Participantpage1](screenshots/ParticipantPage1.JPG)
![Participantpage2](screenshots/participantPageSS.JPG)
### ParticipantPage when the User is not logged in
![Participantpage2](screenshots/ss2.JPG)
### v0.1
### HomePage when the User is logged in
![homepage4](screenshots/HomePage4.JPG)
![homepage5](screenshots/HomePage6.JPG)
### Login Page
![login](screenshots/Login.JPG)
### SignUp Page
![signup](screenshots/Register.JPG)
### v0.3
### Tags, Location added
![tags](screenshots/0.3_1.JPG)
### Search Bar
![search](screenshots/0.3_2.JPG)
### reCAPTCHA
![recaptcha](screenshots/participantPageSS.JPG)
### Registration Completed email
![email](screenshots/0.3_4.JPG)
![Django](https://img.shields.io/badge/Made%20with-Django-brightgreen?style=for-the-badge&logo=django)
### This UI of the website is built with the help of
> [Bootstrap](https://getbootstrap.com/)
>
> [FontAwesome](http://fontawesome.io/)
>
> [Unsplash API](https://unsplash.com/developers)
### Logo made using
> [LogoMaker](https://www.freelogodesign.org/)
