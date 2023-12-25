from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views



urlpatterns = [
    path(
        route='',
        view=views.IndexView.as_view(),
        name='index',
    ),
    
    path(
        route='limited/',
        view=views.LimitView.as_view(),
        name='limit',
    )
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)