from django import forms
from manager.models import Book,Reviews


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["book_isbn","book_title","book_author","book_image","book_desc","book_genre_id"]

class RatingForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ["review","rating"]
        widgets = {
            'review': forms.Textarea(attrs={'cols': 40, 'rows': 7}),
        }
        
        
