import re
from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.views import APIView
#from accounts.functions import send_sms_otp
from accounts.models import OneTimePassword, User
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated, AllowAny
from accounts.serializers import UserSerializer
from django.conf import settings
from django.core.mail import send_mail




class EmailActivation(APIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        user = self.request.user
        email = user.email
        if OneTimePassword.otp_exist(email):
            return Response({"success": False, "errors": [_("otp already sent")]},status=status.HTTP_400_BAD_REQUEST,)

        otp = OneTimePassword(user)
        print('---- OTP ----')
        print(otp.code)



        subject = 'welcome to GFG world'
        message = f'Hi {user.username}, thank you for registering in geeksforgeeks.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]
        send_mail(subject, message, email_from, recipient_list)


        done = send_sms_otp(phone_number, otp.code)
        if not done:
            return Response(
                {"success": False, "errors": [_("error in sending otp")]},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(
            {
                "success": True,
                "data": {"otp_id": otp.otp_id},
            },
            status=status.HTTP_200_OK,
        )

