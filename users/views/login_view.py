# users/views/login_view.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.serializers.login_serializer import LoginSerializer

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user_data = serializer.validated_data
            return Response(
                {
                    "message": "Login successful",
                    "data": user_data
                },
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
