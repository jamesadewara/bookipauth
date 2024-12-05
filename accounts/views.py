from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SubscriptionSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class SubscriptionToggleView(APIView):
    permission_classes = [IsAuthenticated, JWTAuthentication]  # Require authentication

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
