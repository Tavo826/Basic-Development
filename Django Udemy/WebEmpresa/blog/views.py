from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.

def blog(request):
    
    posts = Post.objects.all()    
    return render(request, 'blog/blog.html', {'posts': posts})

#Clasificando las categorías
def category(request, category_id):
    
    #Busca el id o lanza la excepción 404
    category = get_object_or_404(Category, id=category_id)
    #Recuperando las entradas
    #posts = Post.objects.filter(categories=category)

    return render(request, 'blog/category.html', {'category': category})