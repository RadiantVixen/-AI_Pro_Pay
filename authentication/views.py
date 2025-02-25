from django.http import HttpResponse
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class SignupView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")

        user = User.objects.create_user(username=username, email=email, password=password)

        profile = getattr(user, "profile", None)
        if profile:
            profile.language = request.data.get("language", "en")
            profile.avatar = request.data.get("avatar", None)
            profile.save()

        token_url = "http://localhost:8000/login"
        token_data = {"username": username, "password": password}
        token_response = requests.post(token_url, data=token_data)

        return Response(token_response.json(), status=status.HTTP_201_CREATED)
