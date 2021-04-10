"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from shelf.views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from shelf.form import LoginForm

urlpatterns = [
    path('login/', LoginView.as_view(authentication_form=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', signup, name='signup'),
    path('admin/', admin.site.urls),
    
    path('', index, name='index'),
    path('books/', books, name='books'),
    path('books/add-book', add_book),
    path('books/edit-book/<int:book_id>', edit_book, name='edit_book' ),
    path('books/delete/<int:book_id>', delete_book, name='delete_book' ),
    path('books/export/xls', export_xls_books, name='export_xls'),
    
    path('groups/', groups, name='groups' ),
    path('groups/add-group', add_group),
    path('groups/edit-group/<int:group_id>', edit_group, name='edit_group'),
    path('groups/delete/<int:group_id>', delete_group, name='delete_group'),
    
    path('users/', users, name='users'),
    path('users/delete/<int:user_id>', delete_users, name='delete_user' ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)