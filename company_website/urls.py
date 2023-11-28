from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home,name="home"),
    path('about',views.about,name="about"),
    path('portfolio',views.port,name="port"),
    path('product-design',views.product,name="product"),
    path('web-design',views.web,name="web"),
    path('mobile-app',views.mobile,name="mobile"),
    path('digital-mart',views.Digital,name="digital"),
    path('it-staff',views.staff,name="staff"),
    path('blog',views.blog,name="blog"),
    path('gallery/<int:pid>',views.gallery,name="gallery"),
    path('team',views.team,name="team"),
     path('contact_us',views.contact,name="contact"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)