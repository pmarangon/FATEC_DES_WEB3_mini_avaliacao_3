

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import  static
from django.http import HttpResponse

def holliday_view(request):
    return HttpResponse('Feriado')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('holliday/', holliday_view),
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]

