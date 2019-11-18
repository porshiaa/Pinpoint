from django.conf.urls import url

from django.contrib import admin

from django.conf import settings

from django.conf.urls import include

from django.conf.urls.static import static

from pinpoint import views


"""pinpoint_project URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
    1. Add an import:  from my_app import views
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^pinpoint/', include('pinpoint.urls')),
    url(r'^', include('pinpoint.urls')),
    # above maps any URLs starting
    # with pinpoint/ to be handled by
    # the pinpoint application
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




