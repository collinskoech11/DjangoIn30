from django.shortcuts import render

# Create your views here.

# CRUD - create retreive update delete

# list all the posts

def post_list_view(request):
    post_objects = Post.objects.all()
    context = {
        'post_objects': post_objects
    }
    return render(request, "index.html", context)