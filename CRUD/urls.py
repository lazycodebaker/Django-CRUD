
from django.contrib import admin
from django.urls import path
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.addAndshow,name='addAndshow'),
    path('delete/<int:id>/',views.delteUser,name='deleteUser')
]
