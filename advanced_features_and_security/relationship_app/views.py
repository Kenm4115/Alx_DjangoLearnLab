from .forms import BookForm  # Assuming you have created a form for the Book model
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .models import Library
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView
from django.shortcuts import render
from .models import Book  # Import the Book model


def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get all books in this library
        context['books'] = self.object.books.all()
        return context


# Registration view

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('home')  # Redirect to a homepage or other view
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# Helper functions to check user role

def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'


def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'


def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Admin view


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view


@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


# Add Book View

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a list of books or relevant page
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

# Edit Book View


@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})

# Delete Book View


@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'relationship_app/delete_book.html', {'book': book})

# Create view for adding a new book


class AddBookView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'relationship_app/add_book.html'
    success_url = reverse_lazy('list_books')

# Update view for editing an existing book


class EditBookView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'relationship_app/edit_book.html'
    success_url = reverse_lazy('list_books')
