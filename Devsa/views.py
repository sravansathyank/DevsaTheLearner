from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings

def send_email(request):
    if request.method == 'POST':
        suggestion = request.POST.get('suggestion')
        attachment = request.FILES.get('attachment')
        recipient_email = 'sravansathyank@gmail.com'  # The recipient email

        # Create an email message
        email = EmailMessage(
            subject="New Suggestion Received",
            body=f"Suggestion: {suggestion}\n\nAttachment is included.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[recipient_email],
        )

        # Attach the file if provided
        if attachment:
            email.attach(attachment.name, attachment.read(), attachment.content_type)

        # Send the email
        try:
            email.send()
            return render(request, 'success.html')  # Redirect to success page
        except Exception as e:
            return render(request, 'error.html', {'error': str(e)})  # Redirect to error page

    return redirect('owners')  # Redirect back to the owners page if method is not POST

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use!")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        messages.success(request, "Account created successfully!")
        return redirect('login')

    return render(request, 'register.html')

@login_required
def quote(request):
    return render(request, 'quote.html')

@login_required
def main(request):
    return render(request, 'main.html')

@login_required
def it_page(request):
    return render(request, 'it.html')

@login_required
def ele_page(request):
    return render(request, 'ele.html')

@login_required
def passive_page(request):
    return render(request, 'passive.html')

@login_required
def quantum_computing_page(request):
    return render(request, 'quantum_computing.html')

@login_required
def block_page(request):
    return render(request, 'block.html')

@login_required
def augmented_page(request):
    return render(request, 'augmented.html')

@login_required
def smart_grids_page(request):
    return render(request, 'smart_grids.html')

@login_required
def robotics_page(request):
    return render(request, 'robotics.html')

@login_required
def certificate_page(request):
    username = request.user.username
    return render(request, 'certificate.html', {'username': username})

@login_required
def awards_page(request):
    return render(request, 'awards.html')

@login_required
def owner_page(request):
    return render(request, 'owners.html')

@login_required
def sources_page(request):
    return render(request, 'sources.html')