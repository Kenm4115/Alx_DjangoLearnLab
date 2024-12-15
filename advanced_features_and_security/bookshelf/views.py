# from django.shortcuts import render

from .forms import ExampleForm  # Import your form class
from .forms import ExampleForm
from django.shortcuts import render, redirect
from django.shortcuts import render
from .models import Book  # Ensure you have a `Book` model in your app
from django import forms
from .models import Post
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to my book store.")

# Create your views here.

# Permission checks ensure that only users with appropriate permissions can access this view


@permission_required('myapp.can_view', raise_exception=True)
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'myapp/post_list.html', {'posts': posts})


@permission_required('myapp.can_create', raise_exception=True)
def post_create(request):
    if request.method == 'POST':
        # Handle post creation logic
        pass
    return render(request, 'myapp/post_form.html')


@permission_required('myapp.can_edit', raise_exception=True)
def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        # Handle post editing logic
        pass
    return render(request, 'myapp/post_form.html', {'post': post})


@permission_required('myapp.can_delete', raise_exception=True)
def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return render('post_list')


def search_posts(request):
    query = request.GET.get('q', '')
    results = Post.objects.filter(title__icontains=query)
    return render(request, 'search_results.html', {'results': results})


def my_view(request):
    response = HttpResponse("Content")
    response['Content-Security-Policy'] = "default-src 'self'"
    return response


def book_list(request):
    """
    Displays a list of books.
    """
    books = Book.objects.all()  # Query all books from the database
    context = {
        'books': books,
    }
    return render(request, 'bookshelf/book_list.html', context)


def add_book(request):
    """
    View to handle the creation of a new book.
    """
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            # Replace with the appropriate redirect
            return redirect('book_list')
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/add_book.html', {'form': form})


def form_example_view(request):
    """
    A view to render the example form.
    """
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            # Optional success page
            return render(request, 'bookshelf/success.html')
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})
