from django.urls import path
from . import views
# basically like mvc architecture , routes
urlpatterns =[
    path('',views.api_home)
]