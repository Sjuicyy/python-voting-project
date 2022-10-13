from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index')
    path('',views.detail,name='detail')
    path('',views.results,name='results')
    path('',views.vote,name='vote')
    
]
