from django.shortcuts import render
from main.models import *
# Create your views here.
def indexHandler(request):
    content = Content.objects.all()
    name = Name.objects.all()
    return render(request, 'index.html', {'content': content, 'name': name, })