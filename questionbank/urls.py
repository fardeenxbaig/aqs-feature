from django.conf.urls import url

from django_encrypted_filefield.constants import FETCH_URL_NAME
from .views import MyFetchView

urlpatterns = [
    url(
        r"^question-images/(?P<path>.+)",
        MyFetchView.as_view(),
        name=FETCH_URL_NAME
    ),
]