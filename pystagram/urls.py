# coding: utf-8

"""pystagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^photo/(?P<photo_id>\d+)$', 'photo.views.single_photo', name='view_single_photo'),
    # kwargs의 용법
    url(r'^hidden_photo/(?P<photo_id>\d+)$', 'photo.views.single_photo', name='view_hidden_single_photo', kwargs={'hidden':True}),
]

# 업로드 된 파일은 static_files라는 URL을 따르므로 여기에도 추가를 시켜야 한다.
urlpatterns += static('static_files', document_root=settings.MEDIA_ROOT)
