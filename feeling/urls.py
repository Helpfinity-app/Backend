from django.urls import path
from accounts.views import Login,Register,EmailActivation,Logout,Profile,OverView,Refresh,RefreshAccess,UserValidationView


urlpatterns = [
    path("cat", Login.as_view(), name="login"),
]


