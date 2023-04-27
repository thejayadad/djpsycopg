

from django.shortcuts import render
from first_site.models import PostModel
from django.contrib import messages

def homepage(request):
    showall = PostModel.objects.all()
    return render(request, 'index.html', {'data': showall})



def insertpost(request): 
    if request.method == "POST":
        if request.POST.get('title') and request.POST.get('body'):
            savepost = PostModel()
            savepost.title = request.POST.get('title')
            savepost.body = request.POST.get('body')
            savepost.save()
            messages.success(request, "Post Saved!")
            return render(request, 'create.html')
        
    else:
        return render(request, 'create.html')
    

    