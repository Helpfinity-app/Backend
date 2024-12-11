from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.functions import get_user_data, login
from accounts.serializers import UserSerializer, UserRegisterSerializer
from accounts.models import User, ConfirmationCode
from config.settings import ACCESS_TTL



class Register(APIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]
    def post(self, *args, **kwargs):
        confirmation_codes = ConfirmationCode.objects.all()

        serializer = UserRegisterSerializer(data=self.request.data)
        if serializer.is_valid():
            user = User.objects.create_user(**serializer.validated_data)

            if not any(con_code['code'] == self.request.data["confirmation_code"] for con_code in confirmation_codes):
                return Response({"success": False, "errors": [_("You are not confirmed yet, the code you enterd is incorrect")]},status=status.HTTP_400_BAD_REQUEST, )

            else:
                user.confirmed = True
                user.save()
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


        return Response( {"success": False,"errors": [_("incorrect data"), serializer.errors],},status=status.HTTP_400_BAD_REQUEST,)

