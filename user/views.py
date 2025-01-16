"""
Views for the user API.
"""
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)


class CreateUserView(generics.CreateAPIView):
    """
    Create a new user in the system.

    This view handles the creation of new users via API endpoint.

    Methods:
        post: Creates a new user with the provided data.

    Request Body:
        - email (str): User's email address
        - password (str): User's password
        - name (str, optional): User's full name

    Returns:
        - 201 Created: Successfully created user object
        - 400 Bad Request: Invalid data provided

    Example:
        POST /api/user/create/
        {
            "email": "user@example.com",
            "password": "secretpassword123",
            "name": "John Doe"
        }
    """
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """
    Create a new authentication token for user.

    This view extends Django's ObtainAuthToken to create and return an auth token.
    The token can be used for authenticating subsequent requests.

    Attributes:
        serializer_class: Serializer class used for token generation
        renderer_classes: Response renderer classes for the view

    Returns:
        Response with auth token if credentials are valid
        
    Example:
        POST /api/user/token/
        {
            "email": "user@example.com",
            "password": "userpassword123"
        }
    """
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """
    View for managing authenticated user operations.

    This view provides endpoints for retrieving and updating user information.
    Only authenticated users can access these endpoints.

    Attributes:
        serializer_class: Serializer class used for user data serialization
        authentication_classes: List of authentication methods (Token Authentication)
        permission_classes: List of required permissions (IsAuthenticated)

    Methods:
        get_object(): Retrieves the currently authenticated user instance

    Example:
        GET /api/user/me/
        Returns the authenticated user's details

        PATCH /api/user/me/
        Updates the authenticated user's information

        PUT /api/user/me/
        Updates the authenticated user's information
    """
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user
