from django import forms
from .models import Book  # Ensure Book model exists in models.py


class ExampleForm(forms.ModelForm):
    """
    Example form for creating or editing a Book instance.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'description']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_title(self):
        """
        Example of a custom validation method for the title field.
        """
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError("Title is required.")
        if len(title) < 3:
            raise forms.ValidationError(
                "Title must be at least 3 characters long.")
        return title
