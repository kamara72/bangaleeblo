from django.shortcuts import render, redirect
from .models import Contact, Contactme
from django.http import HttpResponse


# Create your views here.

def home(request):
	cnt = Contact.objects.all().order_by('-id')
	return render(request, 'mysite/index.html', {'contacts': cnt})


def about(request):
	return render(request, 'mysite/about.html')


def contact(request):
	if request.method == 'POST':
		fname_v = request.POST.get('fname')
		email_v = request.POST.get('mail')
		message_v = request.POST.get('message')

		c = Contactme(fullname = fname_v, email = email_v, message = message_v)
		c.save()
		return render(request, 'mysite/thanks.html')

	else:
		return render(request, 'mysite/contact.html')


def portfolio(request):
	return render(request, 'mysite/portfolio.html')

def admin_login(request):
	return redirect('http://127.0.0.1:8000/admin/login/?next=/admin/')