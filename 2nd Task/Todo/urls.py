from django.contrib import admin
from django.urls import path
from . import views
from .views import login_view,signup_view,todo_list, add_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home , name="home"),
    #path('login.html/',views.login , name="login"),
    path('signup.html/',views.signup , name="signup"),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('todo/',views.todo , name="todo"),
     path('todo/', todo_list, name='todo'),
    path('add_task/', add_task, name='add_task'),
]