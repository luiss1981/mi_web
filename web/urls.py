from django.urls import path
from django.conf import settings
from .views import IndexView
from django.conf.urls.static import static

app_name ='web'

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)