from django.db import models
from accounts.models import User

class Genre(models.Model):
    genre_id = models.IntegerField(primary_key=True,auto_created=True)
    genre_name = models.CharField(max_length=50)

    
    def __str__(self):
        return self.genre_name


class Book(models.Model):
    book_isbn = models.IntegerField(primary_key=True,auto_created=True)
    book_title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=1000)
    book_image = models.CharField(max_length=550)
    book_desc = models.TextField()
    book_genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
   

    def __str__(self):
        return self.book_title

    # def display_genre(self):
    #     """Create a string for the Genre. This is required to display genre in Admin."""
    #     return ', '.join(Genre.genre_name for book_genre_id in self.genre_name.all()[:3])

    # display_genre.short_description = 'Genre'

class Reviews(models.Model):
    review=models.CharField(max_length=100,default="")
    book_id =models.ForeignKey('Book',on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    CHOICES = (
        ('0', '0'),
        ('.5', '.5'),
        ('1', '1'),
        ('1.5', '1.5'),
        ('2', '2'),
        ('2.5', '2.5'),
        ('3', '3'),
        ('3.5', '3.5'),
        ('4', '4'),
        ('4.5', '4.5'),
        ('5', '5'),
    )
 
    rating=models.CharField(max_length=3, choices=CHOICES, default='2')
    review_date = models.DateTimeField(auto_now_add=True)