from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import OneTimePassword, User
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from accounts.functions import get_user_data, login
from accounts.serializers import UserSerializer
from config.settings import ACCESS_TTL




class Login(APIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, *args, **kwargs):
        email = self.request.data.get("email")
        password = self.request.data.get("password")
        user = authenticate(email=email, password=password)

        if user is not None:
            if user.confirmed == True:

                access, refresh = login(user)

                data = {"refresh_token": refresh, "access_token": access, "user_data": UserSerializer(user).data, }
                response = Response({"success": True, "data": data, }, status=status.HTTP_200_OK, )

                response.set_cookie(
                    "HTTP_ACCESS",
                    f"Bearer {access}",
                    max_age=ACCESS_TTL * 24 * 3600,
                    secure=True,
                    httponly=True,
                    samesite="None",
                )
                return response
            else:
                return Response({"success": False, "errors": [_("You are not confirmed yet.")]},status=status.HTTP_400_BAD_REQUEST,)

        else:
            return Response(
                {"success": False, "errors": [_("The email address or password is incorrect.")]},
                status=status.HTTP_400_BAD_REQUEST,
            )

