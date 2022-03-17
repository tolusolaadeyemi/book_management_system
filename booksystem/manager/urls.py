from django.urls import path
from manager import views 

app_name = 'manager'

urlpatterns = [
   path('dashboard/',views.index, name='index'),
   path('user_list/',views.user_list, name='user_list'),
   path('add_user/',views.add_user, name='add_user'),
   path('add_book/',views.add_book,name='add_book'),
   path('update_book/<str:pk>/',views.update_book,name='update_book'),
   path('update_user/<str:pk>/',views.update_user,name='update_user'),
   path('delete_book/<str:pk>/',views.delete_book,name='delete_book'),
   path('delete_user/<str:pk>/',views.delete_user,name='delete_user'),
   path('delete_rating/<str:pk>/',views.delete_rating,name='delete_rating'),
]