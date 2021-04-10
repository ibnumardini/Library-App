from django.shortcuts import render, redirect
from shelf.models import Book, Group
from shelf import form, resource
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import JsonResponse, HttpResponse
import time, datetime
from django.contrib.auth.models import User

def signup(request):
    if request.POST:
        forms = UserCreationForm(request.POST)
        if forms.is_valid():
            forms.save()
        
            messages.success(request, "Signup Successfully!")
            return redirect('signup')        
        else:
            messages.error(request, forms.errors)
            return redirect('signup')
        
    else:
        ctx = {
            'form' : form.SignupForm()
        }
        return render(request, 'signup.html', ctx)

@login_required(login_url = settings.LOGIN_URL)
def books(request):
    filter = ""
    
    if request.POST and request.POST['filter_by_group'] != 'reset_filter' :
        filter = request.POST['filter_by_group']
        
        books = Book.objects.all().filter(group__name=filter).order_by('-id')

    else:
        books = Book.objects.all().order_by('-id')
        
    groups = Group.objects.all().order_by('-id')
    
    ctx = {
        'books' : books,
        'groups' : groups,
        'filter' : filter
    }
    return render(request, 'books.html', ctx) 

@login_required(login_url = settings.LOGIN_URL)
def index(request):
    return render(request, 'index.html')

@login_required(login_url = settings.LOGIN_URL)
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    
    if request.POST:
        forms = form.BookForm(request.POST, request.FILES, instance=book)
        if forms.is_valid:
            forms.save()
            
            messages.success(request, 'Data Edited')
            
            return redirect('edit_book', book_id=book_id)
    
    ctx = {
        'book' : book,
        'form' : form.BookForm(instance=book) 
    }
    return render(request, 'edit-book.html', ctx)

@login_required(login_url = settings.LOGIN_URL)
def add_book(request):
    if request.POST:
        forms = form.BookForm(request.POST, request.FILES)
        if forms.is_valid:
            forms.save()
            alert = ['success', 'Data Successfully to Saved']

        else :
            alert = ['danger', 'Data Failed to Saved']
            
        ctx = {
                'form' : form.BookForm,
                'alert' : alert
            }
        return render(request, 'add-book.html', ctx)
    
    else :
        ctx = {
            'form' : form.BookForm
        }
        return render(request, 'add-book.html', ctx)
    
@login_required(login_url = settings.LOGIN_URL)
def delete_book(request, book_id):
    book = Book.objects.filter(id=book_id)
    
    try:
        book.delete()
        
        messages.success(request, 'Book Successfully to Deleted!')
        
    except:
        messages.error(request, 'Book Failed to Deleted!')
        
    return redirect('books')

@login_required(login_url = settings.LOGIN_URL)
def groups(request):
    groups = Group.objects.all().order_by('-id')
    
    ctx = {
        'groups' : groups
    }
    return render(request, 'groups.html', ctx)

@login_required(login_url = settings.LOGIN_URL)
def add_group(request):
    if request.POST:
            
            forms = form.GroupForm(request.POST)
            if forms.is_valid:
                try:
                    forms.save()
                    alert = ['success', 'Data Successfully to Saved']
                
                except:
                    alert = ['danger', 'Data Failed to Saved']
                
            else :
                alert = ['danger', 'Data Failed to Saved']
                
            ctx = {
                'form' : form.GroupForm,
                'alert' : alert
            }
            return render(request, 'add-group.html', ctx)
    
    else:
    
        ctx = {
            'form' : form.GroupForm
        }
        return render(request, 'add-group.html', ctx)

@login_required(login_url = settings.LOGIN_URL)
def edit_group(request, group_id):
    group = Group.objects.get(id=group_id)
    
    if request.POST:
        forms = form.GroupForm(request.POST, instance=group)
        if forms.is_valid:
            try:
                forms.save()
                messages.success(request, 'Data Edited')
                
            except:
                messages.error(request, 'Data failed to Edited')
        
            return redirect('edit_group', group_id=group_id)
        
    ctx = {
        'group': group,
        'form': form.GroupForm(instance=group)
    }        
    return render(request, 'edit-group.html', ctx)

@login_required(login_url = settings.LOGIN_URL)
def delete_group(request, group_id):
    group = Group.objects.filter(id=group_id)

    try:
        group.delete()
        
        messages.success(request, 'Group Deleted!')
        
    except:
        messages.error(request, "Group Failed to Deleted!")
        
    return redirect('groups')

@login_required(login_url= settings.LOGIN_URL)
def export_xls_books(request):
    book = resource.BookResource()
    dataset = book.export()
    
    d = datetime.datetime.now()
    posixTime = str(time.mktime(d.timetuple()))
    
    response = HttpResponse(dataset.xls, content_type='applicatino/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="book_'+ posixTime +'.xls"'
    
    return response

@login_required(login_url= settings.LOGIN_URL)
def users(request):
    users = User.objects.all()
    
    ctx = {
        'users' : users
    }
    return render(request, 'users.html', ctx)

@login_required(login_url= settings.LOGIN_URL)
def delete_users(request, user_id):
    user = User.objects.filter(id=user_id)

    try:
        user.delete()
        
        messages.success(request, 'User Deleted!')
    except:
        messages.error(request, "User Failed to Deleted!")
        
    return redirect('users')

    