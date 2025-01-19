from typing import Any, Callable

from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse


class SuperuserRequiredMiddleware:
    def __init__(self, get_response: Callable):
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> Any:
        if not request.user.is_superuser:  # type: ignore
            if request.path != reverse("login"):
                return redirect("login")
        response = self.get_response(request)
        return response
