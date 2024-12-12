from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.models import SubscriptionPlan
from .serializers import SubscriptionSerializer, MainUserSerializer, UpdateMainUserSerializer, SubscriptionPlanSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import render, redirect
from django.contrib.auth import logout


from django.core.mail import send_mail
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

def template_signin(request, pk):
    if pk == "google":
        provider_name = "Google"
    elif pk == "microsoft":
        provider_name = "Microsoft"
    elif pk == "github":
        provider_name = "Github"
    elif pk == "facebook":
        provider_name = "Facebook"
    elif pk == "apple":
        provider_name = "Apple"
    elif pk == "linkedin":
        provider_name = "Linkedin"
    else:
        return Response("<p>This Provider is not currently available</p>", status=HTTP_400_BAD_REQUEST)
    
    context = {
        "provider_name": provider_name,
        "provider": pk
    }

    return render(request, 'accounts\templates\oauths\template-signin.html', context)

def logout_view(request):
    logout(request)
    return redirect("/")

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

    @swagger_auto_schema(
        operation_summary="Toggle User Subscription",
        operation_description="Enable or disable subscription for the authenticated user.",
        request_body=SubscriptionSerializer,
    )
    def patch(self, request):
        user = request.user  # Get the authenticated user
        serializer = SubscriptionSerializer(user, data=request.data, partial=True)
        
        if serializer.is_valid():
            if request.data.get("subscribe"):
                # Subscribe user
                plan_id = request.data.get("plan_id")
                try:
                    plan = SubscriptionPlan.objects.get(id=plan_id)
                    user.subscribe(plan)
                    message = f"Subscribed to plan: {plan.name}."
                except SubscriptionPlan.DoesNotExist:
                    return Response({"error": "Invalid plan ID."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                # Cancel subscription
                user.cancel_subscription()
                message = "Subscription cancelled."

            return Response({"message": message}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubscriptionPlanListView(APIView):
    """
    View to list all subscription plans.
    """
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="List Subscription Plans",
        operation_description="Get a list of all available subscription plans.",
        responses={200: SubscriptionPlanSerializer(many=True)},
    )
    def get(self, request):
        plans = SubscriptionPlan.objects.all()
        serializer = SubscriptionPlanSerializer(plans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)