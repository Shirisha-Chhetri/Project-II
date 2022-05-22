"""Book_Recommender URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.auth.models import User
from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('uploaddataset/',views.upload,name = "Upload dataset"),
     
    # consisting home module
    path('',views.allgenre),
    path('bookson/',views.bookongenre),
    path('about/',views.about),
    path('search/',views.search, name='search'),
    path('signup/',views.signup),
    path('login/',views.loginuser, name='login'),
    path('logout/',views.logouts, name='logouts'),
    path('book/',views.allbook),
    path('search_auto/', views.search_auto, name='search_auto'),
    path('allgenre/',views.genre),

    #consisting genre or book module
    path('getbook/<int:id>/',views.specific_book),
    path('add_to_fav/<int:id>',views.add_fav,name="Add to favourite"),
    path('remove_from_fav/<int:id>',views.remove_fav,name="Remove from favourite"),
    path('user_fav/',views.get_user_fav,name='wishlist'),
    
]