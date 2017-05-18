from django.http import Http404, HttpResponse
import datetime

def hello(request):
	return HttpResponse('Hello, world!')

def current_datetime(request):
	now = datetime.datetime.now()
	html = '<html><h1>It is now {now}</h1></html>'.format(now=now)
	return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = '<html><h1>In {offset} hour(s), it will be {dt}.</h1></html>'.format(offset=offset, dt=dt)
	return HttpResponse(html)
