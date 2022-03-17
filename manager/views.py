from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.decorators import login_required
from accounts.models import User
from accounts.forms import AddUserForm
from booksystem.filters import BookFilter
from users.forms import RatingForm
from .models import Book,Reviews
from .forms import AddBookForm

@login_required
def index(request):
    all_books = Book.objects.all()
    myFilter = BookFilter(request.GET,queryset=all_books)
    all_books = myFilter.qs
    context = {
        'all_books':all_books,
        'myFilter':myFilter,
    }
    return render(request, 'manager/dashboard.html',context=context)

@login_required
def book_detail(request,pk):
    if request.user.is_authenticated:
        try:
            book = Book.objects.get(book_isbn=pk)
            reviews = Reviews.objects.filter(book_id=pk)
            form = RatingForm()
        except Book.DoesNotExist:
            raise Http404('Book does not exist')
        return render(request, 'manager/book_detail.html', context={'book': book,'reviews':reviews,'form':form})
    else:
        return redirect('accounts:login')

@login_required
def user_list(request):
    all_users = User.objects.all()
    context = {
        'all_users':all_users,
    }
    return render(request, 'manager/userboard.html',context=context)


@login_required
def add_book(request):
    if not request.user.is_superuser:
        return redirect('frontend:index')
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Book Added Succesfully')
            return redirect('manager:index')
        else:
            messages.error(request,"Unable to Add Book")
            return redirect('manager:index')
    else:
        form = AddBookForm()
        return render(request,'manager/addbook.html',{'form':form})

@login_required
def add_user(request):
    if not request.user.is_superuser:
        return redirect('frontend:index')
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User Added Succesfully')
            return redirect('manager:user_list')
        else:
            messages.error(request,"Unable to Add User")
            return redirect('manager:user_list')
    else:
        form = AddUserForm()
        return render(request,'manager/adduser.html',{'form':form})

@login_required
def update_book(request,pk):
    if not request.user.is_superuser:
        return redirect('frontend:index')
    bookobj = Book.objects.get(book_isbn=pk)
    form = AddBookForm(instance=bookobj)
    if request.method == 'POST':
        form = AddBookForm(data=request.POST,instance=bookobj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            messages.success(request,'Book Updated Succesfully')
            return redirect('manager:index')
        else:
            messages.error(request,"Unable to Update Book")
            return redirect('manager:index')
    else:
        return render(request,'manager/updatebook.html',{'form':form})

@login_required
def update_user(request,pk):
    if not request.user.is_superuser:
        return redirect('frontend:index')
    userobj = User.objects.get(id=pk)
    form = AddUserForm(instance=userobj)
    if request.method == 'POST':
        form = AddUserForm(data=request.POST,instance=userobj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            messages.success(request,'User Updated Succesfully')
            return redirect('manager:user_list')
        else:
            messages.error(request,"Unable to Update User")
            return redirect('manager:user_list')
    else:
        return render(request,'manager/updateuser.html',{'form':form})

@login_required
def delete_book(request, pk):
    if not request.user.is_superuser:
        return redirect('frontend:index')
    bookobj = Book.objects.get(book_isbn=pk)
    context = {'book':bookobj}
    if request.method == 'POST':
        bookobj.delete()
        messages.success(request,f'{bookobj.book_title} Removed Succesfully')
        return redirect('manager:index')
    else:
        return render(request,'manager/deletebook.html',context=context)


@login_required
def delete_user(request, pk):
    if not request.user.is_superuser:
        return redirect('frontend:index')
    userobj = User.objects.get(id=pk)
    context = {'userobj':userobj}
    if request.method == 'POST':
        userobj.delete()
        messages.success(request,f'{userobj.first_name} Removed Succesfully')
        return redirect('manager:user_list')
    else:
        return render(request,'manager/deleteuser.html',context=context)

@login_required
def delete_rating(request,pk):
    if not request.user.is_superuser:
        return redirect('frontend:index')
    ratingobj = Reviews.objects.get(id=pk)
    context = {'ratingobj':ratingobj}
    if request.method == 'POST':
        ratingobj.delete()
        messages.success(request,'Review Removed Succesfully')
        return redirect('manager:index')
    else:
        return render(request,'manager/deleterating.html',context=context)





