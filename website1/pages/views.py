from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs): #*args, **kwargs
	print (*args,**kwargs)
	print (request.user)#return the user (authetication) >> loged in
	return  HttpResponse("<h1> Hello World</h1>" )#string of HTML code

def contact_view(request, *args, **kwargs):
	#return HttpResponse("<h1> Contact page </h1> ")
	context = {} #dictionary
	return render(request, 'contact.html', context)

def about_view(request,*args, **kwargs):
	return render(request, 'about.html', {})

def social_view(request, *args, **kwargs):
	context = {
		'text':'hi, this is my text',
		'number' : 123,
		'my_list' : [123,222,654],
		'my_html':"<h1>HTMl text: Hello World</h1>"
	}
	return render(request, 'social.html', context)