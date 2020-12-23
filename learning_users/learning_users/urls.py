"""learning_users URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url,include
from basic_app import views
import basic_app.views as views
import learning_users.settings as settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import basic_app.views as views
import learning_users.settings as settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
url(r'^$',views.index, name='index'),
    path('admin/', admin.site.urls),
    url(r'^basic_app/',include('basic_app.urls') ),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^special/',views.special,name='special'),
    path("update/<int:pk>/", views.update_task, name="update_task"),
    path("delete/<int:pk>/", views.delete_task, name="delete_task"),
    url(r'^cool/',views.cool,name='cool'),
    url(r'^show_pdf/',views.AnalyticsView,name='show_pdf'),
    url(r'^shownpdf/$',views.shownpdf,name='shownpdf'),
    url(r'^del_pdf/$',views.del_pdf,name='del_pdf'),
    url(r'^rename_pdf/$',views.rename_pdf,name='rename_pdf'),
    url(r'^index1/',views.index1,name='index1'),
    path("update1/<int:pk>/", views.update_task1, name="update_task1"),
    path("delete1/<int:pk>/", views.delete_task1, name="delete_task1"),
    path('ckeditor',include('ckeditor_uploader.urls')),
    path("update2/<int:pk>/", views.update_task2, name="update_task2"),
    path("delete2/<int:pk>/", views.delete_task2, name="delete_task2"),





    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


 
 
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
