from django.urls import path
from . import views
urlpatterns = [
    path('',views.index ,name="index"),
    path('clas',views.clas ,name="clas"),
    path('chat',views.chat,name='chat'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('books/<int:id>',views.books,name="books"),


]

