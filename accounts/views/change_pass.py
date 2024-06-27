from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.serializers import UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.hashers import check_password



class ChangePass(APIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        user=self.request.user
        data=self.request.data
        if check_password(data["oldpass"], user.password):
            user.set_password(data["newpass"])
            user.save()
            return Response("Password has been updated successfully", status=status.HTTP_200_OK)
        else:
            return Response("Old password is invalid", status=status.HTTP_406_NOT_ACCEPTABLE)