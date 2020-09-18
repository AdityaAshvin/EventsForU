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
        
        if username is not None and password is not None:
            if user is not None:
                auth.login(request, user)
                messages.info(request,"Successfully logged in!")
                return redirect('home')
            else:
                messages.info(request,"invalid credentials")
                return redirect('home')
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
            return redirect('home')
        elif User.objects.filter(username=username).exists():
            messages.info(request,'Username already in use')
            return redirect('home')
        else:
            user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname)
            user.save()
            messages.info(request,'Successfully Registered. You can now login to your account.')
            return redirect('home')
    else:    
        return render(request, "login.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('textbox')
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        
        if result['success']:
                contact = Contact(name = name, email = email, phone = phone, desc = desc)
                contact.save()
                messages.success(request, 'Your response has been sent! You will soon be recieving an email containing all the details. If you cannot find the email in your inbox, check the bulk or the junk folders.')
                event = EventPage.objects.get(id=desc)
                context = {
                    "name": name,
                    "phone": phone,
                    "event": event.title,
                    "location": event.location,
                    "desc": event.desc,
                    "organizer": event.organizer
                }
                message = render_to_string('email/registration_complete_email.html', context)
                send_mail('Registration Completed | EventsForU',  strip_tags(message) , 'adityaashvin02@gmail.com', [email], fail_silently=False, html_message=message)
                return redirect('home')
        else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')
                return redirect('contact')
    else:    
        return render(request, "contact.html")

def eventpage(request,id):
        events = EventPage.objects.filter(id=id).first()
        return render(request, 'eventpage.html',{'events': events})

def logout(request):
    auth.logout(request)
    return redirect('/')