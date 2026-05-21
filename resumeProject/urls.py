
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from resumeProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',resume,name='resume'),
    path('addresume/',addresume,name='addresume'),
    path('deleteresume/<str:myid>',deleteresume,name='deleteresume'),
    path('updateresume/',updateresume,name='updateresume'),
    path('editresume/<str:myid>',editresume,name='editresume'),
    path('viewresume/<str:myid>',viewresume,name='viewresume'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
