from django.urls import path

from . import views
from hosters import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/',views.Home,name='home'),
    path('login/', views.form_login,name='login'),
    path('devhome/', views.dev_home,name='devhome'),
    path('addlogo/',views.add_logo,name='addlogo'),
    path('addvideo/',views.add_video,name='addvideo'),
    path('adddesign/',views.add_design,name='adddesign'),
    path('addprintart/',views.add_printart,name='addprintart'),
    path('logout/',views.form_logout,name='logout'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)