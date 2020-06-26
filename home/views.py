from django.shortcuts import render, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from home.models import EventPage
from django.core.mail import send_mail
import requests
from EventsForU import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from_email = settings.EMAIL_HOST_USER

# Create your views here.

def index(request):
    events = EventPage.objects.all()
    return render(request, 'index.html',{'events': events})

def login(request):
    if request.method== 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            messages.info(request,"Successfully logged in!")
            return redirect('home')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    else:
        return render(request,'login.html')

def signup(request):
    if request.method == 'POST':                                              #fetching the data from form
        username = request.POST["username"]
        firstname = request.POST["firstname"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(email=email).exists():
            messages.info(request,'Email already in use')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname)
            user.save()
            messages.info(request,'Successfully Registered')
            return redirect('home')
    else:    
        return render(request, "register.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('textbox')
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
                'secret': 'settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY',
                'response': recaptcha_response
            }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        
        if result['success']:
                contact = Contact(name = name, email = email, phone = phone, desc = desc)
                contact.save()
                messages.success(request, 'Your response has been sent! You will soon be recieving an email containing all the details')
                event = EventPage.objects.get(id=desc)
                context = {
                    "name": name,
                    "phone": phone,
                    "event": event.title,
                    "location": event.location,
                    "desc": event.desc
                }
                message = render_to_string('email/registration_complete_email.html', context)
                send_mail('Registration Completed | EventsForU',  strip_tags(message) , from_email, [email], fail_silently=False, html_message=message)
                return redirect('home')
        else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                return redirect('contact')
    else:    
        return render(request, "contact.html")

def logout(request):
    auth.logout(request)
    return redirect('/')