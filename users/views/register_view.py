# users/views/register_view.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.serializers.register_serializer import RegisterSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user_data = serializer.save()  # Calls the create() in your serializer
            return Response(
                {
                    "message": "User registered successfully",
                    "data": user_data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
