from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SubscriptionSerializer, MainUserSerializer, UpdateMainUserSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

class MainUserDetailUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Retrieve the authenticated user's details."""
        user = request.user
        serializer = MainUserSerializer(user)
        return Response(serializer.data, status=HTTP_200_OK)

    def patch(self, request):
        """Update the authenticated user's details."""
        user = request.user
        serializer = UpdateMainUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class SubscriptionToggleView(APIView):
    permission_classes = [IsAuthenticated]  # Require authentication

    def patch(self, request):
        user = request.user  # Get the authenticated user
        serializer = SubscriptionSerializer(user, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            message = (
                "Subscription enabled." if user.is_subscribed else "Subscription disabled."
            )
            return Response({"message": message}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
