"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from prediction import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("prediction.urls"))
    # path('sighnup',views.sighnup,name='sighnup'),
    # path('login',views.login,name='login'),
    # path('predict',views.predict,name="predict"),
    # path('result',views.result,name="result"),
    # path("about/",views.about,name="about"),
    
    # path("contact",views.contact,name="contact"),
    #path('',include("prediction.urls"))
    # path('home',views.home,name='home'),
    # path('predict',views.predict,name="predict"),
    # path('/',views.index,name="index"),
    # path('result',views.result,name="result")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
