from rest_framework import generics, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from post.models import Post, PostComment
from post.serializers import PostSerializer, CommentSerializer
from shared.custom_pagination import CustomPagination


class PostListApiView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny, ]
    pagination_class = CustomPagination

    def get_queryset(self):
        return Post.objects.all()


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, ]

    def put(self, request, *args, **kwargs):
        post = self.get_object()
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "success": True,
                "code": status.HTTP_200_OK,
                "message": "Maqola muvaffaqiyatli yangilandi!",
                "data": serializer.data
            }
        )

    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        post.delete()

        return Response(
            {
                "success": True,
                "code": status.HTTP_204_NO_CONTENT,
                "message": "Maqola muvaffaqiyatli o'chirildi!"
            }
        )


class PostCommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self):
        post_id = self.kwargs['pk']
        queryset = PostComment.objects.filter(post__id=post_id)
        return queryset


class PostCommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        post_id = self.kwargs['pk']
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=self.request.user, post=post)


class CommentListCreateApiView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    queryset = PostComment.objects.all()
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        post_id = self.request.data.get('post')
        if not post_id:
            raise serializers.ValidationError({"post": "Post ID yuborilishi shart."})
        serializer.save(author=self.request.user, post_id=post_id)
