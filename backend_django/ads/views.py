from rest_framework import pagination, viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated, AllowAny

from .permissions import IsOwner, IsAdmin
from .models import Ad, Comment
from .serializers import AdSerializer, CommentSerializer, AdListSerializer
from .filters import AdFilter


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter
    http_method_names = ["get", "post", "patch", "delete"]

    def get_serializer_class(self):
        if self.action in ("me", "list"):
            self.serializer_class = AdListSerializer
        else:
            self.serializer_class = AdSerializer

        return super().get_serializer_class()

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = [AllowAny]
        elif self.action == "update":
            self.permission_classes = [IsAuthenticated & IsOwner | IsAdmin]
        elif self.action == "destroy":
            self.permission_classes = [IsAuthenticated & IsOwner | IsAdmin]
        else:
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user.pk)

    @action(detail=False)
    def me(self, request, *args, **kwargs):
        self.queryset = self.get_queryset().filter(author_id=self.request.user.pk)
        return self.list(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'
    http_method_names = ["get", "post", "patch", "delete"]

    def get_queryset(self):
        """
        Выдача всех комментарий указанного объявления
        """
        self.queryset = self.queryset.filter(ad_id=self.kwargs.get('ad_id'))
        return super().get_queryset()

    def get_permissions(self):
        if self.action == "update":
            self.permission_classes = [IsAuthenticated & IsOwner | IsAdmin]
        elif self.action == "destroy":
            self.permission_classes = [IsAuthenticated & IsOwner | IsAdmin]
        else:
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(ad_id=self.kwargs.get("ad_id"), author_id=self.request.user.pk)


