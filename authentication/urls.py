from django.urls import path
from . import views, stripe 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from authentication.llama import upload_pdf, ask_question
from stripe import create_checkout_session

urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('signup', views.SignupView.as_view() , name = 'signup'),
    path('test', views.index , name = 'test'),
    path("upload/", upload_pdf, name="upload"),
    path("ask/", ask_question, name="ask"),
    path("create-checkout-session/", create_checkout_session, name="create-checkout-session"),
]

