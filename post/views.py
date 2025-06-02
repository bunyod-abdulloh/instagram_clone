from rest_framework import generics
from rest_framework.permissions import AllowAny

from post.models import Post
from post.serializers import PostSerializer
from shared.custom_pagination import CustomPagination


class PostListApiView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny, ]
    pagination_class = CustomPagination

    def get_queryset(self):
        return Post.objects.all()
