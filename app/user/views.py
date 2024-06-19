"""
vIEWS FOR USERS
"""
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializers import UserSerializer, LoginSerializer

class RegisterUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer
class LoginUserView(ObtainAuthToken):
    """Login a user in the system."""
    serializer_class = LoginSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_object(self):
        """Retrieve and return authentication user."""
        return self.request.user