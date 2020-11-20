from django.shortcuts import render
from .models import Product
from .forms import ProductionForm, PureDjangoForm


# Create your views here.


def pure_django_form(request):
	my_form = PureDjangoForm()
	if request.method == 'POST':
		my_form = PureDjangoForm(request.POST)
		if my_form.is_valid():
			print(my_form.cleaned_data)
			Product.objects.create(**my_form.cleaned_data)
			my_form = PureDjangoForm()
		else:
			print(my_form.errors)
	context = {
		'form' : my_form,
	}
	return render(request, 'PureDjangoForm.html',context)



def html_form(request):
	print(request.GET['q'])
	print(request.POST)
	context = {}

	return render(request, 'form_page.html',{})


def product_create_views(request):
	form = ProductionForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductionForm()
	context = {
		'form':form,
	}
	return render(request, 'create_forms.html',context)


def product_detail_views(request):
	obj = Product.objects.get (id=1)
	context = {
		'title' : obj.title,
		'summary' : obj.summary,
		'price' : obj.price,
	}
	return render(request, 'details.html',context)