

from django.shortcuts import render
from first_site.models import PostModel

def homepage(request):
    showall = PostModel.objects.all()
    return render(request, 'index.html', {'data': showall})

