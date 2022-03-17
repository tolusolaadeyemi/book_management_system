import datetime
from datetime import datetime, timezone,tzinfo
from django.utils import timezone
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from accounts.models import User
from manager.models import Book,Reviews
from booksystem.filters import BookFilter
from accounts.forms import AddUserForm
from .forms import AddBookForm,RatingForm


now_aware = datetime.now(timezone.utc)
tz_info = now_aware.tzinfo

@login_required
def index(request):
    all_books = Book.objects.all()
    myFilter = BookFilter(request.GET,queryset=all_books)
    all_books = myFilter.qs
    context = {
        'all_books':all_books,
        'myFilter':myFilter,
    }
    return render(request, 'users/dashboard.html',context=context)

@login_required
def homepage(request):
    if request.user.is_authenticated:
        highestRated = Reviews.objects.filter(rating__gte=3).order_by('book_id').distinct()
        lowestRated = Reviews.objects.filter(rating__lte=2.5).order_by('book_id').distinct()
        myRatings = Reviews.objects.filter(user_id=request.user)
        return render(request,'users/homepage.html',context={'highestRated':highestRated,'lowestRated':lowestRated,'myRatings':myRatings})
    else:
        return redirect('accounts:login')

@login_required
def book_detail(request,pk):
    if request.user.is_authenticated:
        try:
            book = Book.objects.get(book_isbn=pk)
            reviews = Reviews.objects.filter(book_id=pk)
            form = RatingForm()
        except Book.DoesNotExist:
            raise Http404('Book does not exist')
        return render(request, 'users/book_detail.html', context={'book': book,'reviews':reviews,'form':form})
    else:
        return redirect('accounts:login')

@login_required
def add_user(request):
    if request.user.is_authenticated and request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User Added Succesfully')
            return redirect('users:user_list')
        else:
            messages.error(request,"Unable to Add User")
            return redirect('users:user_list')
    else:
        form = AddUserForm()
        return render(request,'users/adduser.html',{'form':form})

@login_required
def add_book(request):
    if request.user.is_authenticated and request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Book Added Succesfully')
            return redirect('users:index')
        else:
            messages.error(request,"Unable to Add Book")
            return redirect('users:index')
    else:
        form = AddBookForm()
        return render(request,'users/addbook.html',{'form':form})

@login_required
def update_book(request,pk):
    if request.user.is_authenticated:
        bookobj = Book.objects.get(book_isbn=pk)
        form = AddBookForm(instance=bookobj)
    if request.method == 'POST':
        form = AddBookForm(data=request.POST,instance=bookobj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            messages.success(request,'Book Updated Succesfully')
            return redirect('users:index')
        else:
            messages.error(request,"Unable to Update Book")
            return redirect('users:index')
    else:
        return render(request,'users/updatebook.html',{'form':form})

@login_required
def user_list(request):
    all_users = User.objects.all()
    context = {
        'all_users':all_users,
    }
    return render(request, 'users/userboard.html',context=context)

@login_required
def update_user(request,pk):
    if request.user.is_authenticated:
        userobj = User.objects.get(id=pk)
        form = AddUserForm(instance=userobj)
    if request.method == 'POST':
        form = AddUserForm(data=request.POST,instance=userobj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            messages.success(request,'User Updated Succesfully')
            return redirect('users:user_list')
        else:
            messages.error(request,"Unable to Update User")
            return redirect('users:user_list')
    else:
        return render(request,'users/updateuser.html',{'form':form})

    
@login_required
def delete_book(request, pk):
    if request.user.is_authenticated:
        bookobj = Book.objects.get(book_isbn=pk)
        context = {'book':bookobj}
    if request.method == 'POST':
        bookobj.delete()
        messages.success(request,f'{bookobj.book_title} Removed Succesfully')
        return redirect('users:index')
    else:
        return render(request,'users/deletebook.html',context=context)


@login_required
def rate_book(request,pk):
    if request.user.is_authenticated:
        book = Book.objects.get(book_isbn=pk)
        userobj = get_object_or_404(User,id=str(request.user.id))
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            myReview = form.cleaned_data['review']
            review = Reviews()
            review.book_id = book
            review.user_id = userobj
            review.rating = rating
            review.review = myReview
            review.save()
            messages.success(request,'Rating Added Successfully, Thanks!')
            return redirect('users:homepage')
        else:
            messages.error(request,"Unable to Add Rating")
            return redirect('users:homepage')
    else:
        return redirect('accounts:login')

        