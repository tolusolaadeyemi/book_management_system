from django.urls import path
from users import views 

app_name = 'users'

urlpatterns = [
    path('homepage/',views.homepage, name='homepage'),
    path('index/',views.index, name='index'),
    path('book/<str:pk>/', views.book_detail, name='book_detail'),
    path('user_list/',views.user_list, name='user_list'),
    path('add_user/',views.add_user, name='add_user'),
    path('add_book/',views.add_book,name='add_book'),
    path('update_book/<str:pk>/',views.update_book,name='update_book'),
    path('update_user/<str:pk>/',views.update_user,name='update_user'),
    path('delete_book/<str:pk>/',views.delete_book,name='delete_book'),
    path('rate_book/<str:pk>/',views.rate_book,name='rate_book'),
]