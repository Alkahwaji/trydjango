from django.contrib import admin

# Register your models here.
from .models import Product #import class or model name from models


admin.site.register(Product)