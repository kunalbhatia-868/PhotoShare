from django.shortcuts import redirect, render
from photos import models
# Create your views here.

def gallery(request):
    category=request.GET.get('category')
    if category == None:
        photos=models.Photo.objects.all()
    else:
        photos=models.Photo.objects.filter(category__name=category)    

    categories=models.Category.objects.all()

    context={
    'categories':categories,
    'photos':photos,
    }

    return render(request,"photos/gallery.html",context)

def viewPhoto(request,pk):
    photo=models.Photo.objects.get(id=pk)
    context={
        'photo':photo,
    }
    return render(request,"photos/photo.html",context)


def addPhoto(request):
    categories=models.Category.objects.all()
    if request.method=='POST':
        data=request.POST
        image=request.FILES.get('image') 
        if data['category'] != 'none' :
            category=models.Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category,created=models.Category.objects.get_or_create(name=data['category_new'])
        else:
            category=None

        photo=models.Photo.objects.create(
            description=data['description'],
            category=category,
            image=image
        )
        return redirect('gallery')
        
    context={
    'categories':categories,
    }
    return render(request,"photos/addPhoto.html",context)    