from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, 'home.html')




def send_message(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        subject = f"New message from {name}"
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        send_mail(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            ['jumannendaki9@gmail.com'],
            fail_silently=False,
        )
        return redirect('home')  # Redirect to homepage after sending
