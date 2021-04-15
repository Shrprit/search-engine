from django.urls import path
from . import views

app_name='brcm'

urlpatterns = [
    path('',views.index,name='index'),
    path('events',views.events,name='events'),
    path('news',views.news,name='news'),
    path('search',views.search,name='search'),
    path('about',views.about,name='about'),
    path('search_engine/studentview/<str:s_roll_no>',views.studentview,name='studentview'),
    path('search_engine/bookview/<str:bookname>',views.bookview,name='bookview'),
    path('search_engine/teacherview/<str:teachername>',views.teacherview,name='teacherview')
   
    
]
