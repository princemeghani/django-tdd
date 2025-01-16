"""
Views for the recipe APIs.
"""
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe, Tag
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing recipe operations.
    This ViewSet provides CRUD operations for Recipe objects with authentication.
    It uses different serializers for list and detail views, and ensures
    recipes are associated with authenticated users.
    Attributes:
        serializer_class: Serializer class for detailed recipe representation
        queryset: Base queryset for all recipe objects
        authentication_classes: List containing TokenAuthentication
        permission_classes: List containing IsAuthenticated permission
    Methods:
        get_queryset: Returns recipes filtered by authenticated user
        get_serializer_class: Returns appropriate serializer based on action
        perform_create: Associates new recipe with authenticated user
    """
    

    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve recipes for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.RecipeSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new recipe."""
        serializer.save(user=self.request.user)


class TagViewSet(mixins.DestroyModelMixin,mixins.UpdateModelMixin,mixins.ListModelMixin, viewsets.GenericViewSet):
                 
    """
    ViewSet for managing tag objects in the database.
    This ViewSet provides CRUD operations for Tag model:
    - List tags (GET)
    - Update tags (PUT/PATCH)
    - Delete tags (DELETE)
    Authentication:
        Requires token authentication
    Permissions:
        Only authenticated users can access endpoints
    Filtering:
        Results are filtered to return only tags belonging to the authenticated user
        Tags are ordered by name in descending order
    Attributes:
        serializer_class: Serializer class used for tag object serialization
        queryset: Base queryset of all tags
        authentication_classes: List of authentication classes (TokenAuthentication)
        permission_classes: List of permission classes (IsAuthenticated)
    """
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter queryset to authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by('-name')
