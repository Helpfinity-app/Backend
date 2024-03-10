from django.urls import path
from accounts.views import Login,Register,EmailActivation,Logout,Profile,OverView,Refresh,RefreshAccess,UserValidationView


urlpatterns = [
    path("login", Login.as_view(), name="login"),
    path("register", Register.as_view(), name="register"),
    path("activation", EmailActivation.as_view(), name="activation"),
    #path("verification", EmailVeriy.as_view(), name="verification"),
    path("logout", Logout.as_view(), name="logout"),
    path("profile", Profile.as_view(), name="profile"),
    path("overview", OverView.as_view(), name="overview"),
    path("refresh", Refresh.as_view(), name="refresh"),
    path("refresh-access", RefreshAccess.as_view(), name="refresh-access"),
    path("is-valid", UserValidationView.as_view(), name="is-valid"),
]


