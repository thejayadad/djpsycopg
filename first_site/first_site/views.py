

from django.shortcuts import render
from first_site.models import post
from django.contrib import messages

def homepage(request):
    showall = post.objects.all()
    return render(request, 'index.html', {'showall': showall})



def insertpost(request): 
    if request.method == "POST":
        if request.POST.get('title') and request.POST.get('content'):
            savepost = post()
            savepost.title = request.POST.get('title')
            savepost.content = request.POST.get('content')
            savepost.save()
            messages.success(request, "Post Saved!")
            return render(request, 'create.html')
        
    else:
        return render(request, 'create.html')
    

