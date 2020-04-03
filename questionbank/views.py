from django.shortcuts import render
from django.contrib.auth.mixins import AccessMixin
from django_encrypted_filefield.views import FetchView


class MyPermissionRequiredMixin(AccessMixin):
    """
    Your own rules live here
    """
    pass


class MyFetchView(MyPermissionRequiredMixin, FetchView):
    pass