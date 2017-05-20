from django.core.mail import send_mail
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from mysite.forms import ContactForm

import datetime

def contact(request):
	#form = ContactForm()
	#return render(request, 'contact_form.html', {'form': form})
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			send_mail(
				cd['subject'],
				cd['message'],
				cd.get('email', 'noreply@example.com'),
				['siteowner@example.com'],
			)
			return HttpResponseRedirect('/contact/thanks/')
	else:
		form = ContactForm(
			initial={'subject': 'I love your site!'}
		)
	return render(request, 'contact_form.html', {'form': form})

def hello(request):
	return HttpResponse('Hello, world!')

def current_datetime(request):
	now = datetime.datetime.now()
	return render(request, 'current_datetime.html', {'current_date': now})

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	return render(request, 'hours_ahead.html', {'hour_offset': offset, 'next_time': dt})

def display_meta(request):
	values = request.META.items()
	html = []
	for k, v in sorted(values):
		html.append(('<tr><td>{}</td><td>{}</td></tr>').format(k, v))
	return HttpResponse(('<table>{}</table>').format('\n'.join(html)))
