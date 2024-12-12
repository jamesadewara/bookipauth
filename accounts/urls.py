from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SubscriptionToggleView, MainUserDetailUpdateView, SubscriptionPlanListView, template_signin, logout_view

urlpatterns = [
    path('provider-signin/:str', template_signin),  
    path('logout', logout_view),  

    # Authentication URLs
    path('auth/', include('allauth.urls')),  # Includes Allauth HTML-based authentication views
    path('auth/', include('dj_rest_auth.urls')),  # RESTful login/logout/password reset endpoints
    path('auth/registration/', include('dj_rest_auth.registration.urls')),  # User registration endpoints

    # Social Authentication URLs
    # path('auth/social/', include('allauth.socialaccount.urls')),  # Includes social login URLs from Allauth

    # JWT Authentication URLs
    path('authjwt/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT token generation
    path('authjwt/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT token refresh
    path('authjwt/user/me/', MainUserDetailUpdateView.as_view(), name='user-detail'),  # Current user details

    # Subscription Management URLs
    path('subscription/toggle/', SubscriptionToggleView.as_view(), name='subscription-toggle'),  # Toggle subscription
    path('subscription/plans/', SubscriptionPlanListView.as_view(), name='subscription-plans'),  # View subscription plans
]