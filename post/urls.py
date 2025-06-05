from django.urls import path

from .views import PostListApiView, PostCreateView, PostRetrieveUpdateDestroyView, PostCommentListView, \
    PostCommentCreateView, CommentListCreateApiView, PostLikeListView, CommentRetrieveView, CommentLikeListView, \
    AllLikesApiView, LikesCreateApiView, CustomDestroyLikeApiView

urlpatterns = [
    path('list/', PostListApiView.as_view(), ),
    path('create/', PostCreateView.as_view(), ),
    path('<uuid:pk>/', PostRetrieveUpdateDestroyView.as_view(), ),
    path('<uuid:pk>/likes/', PostLikeListView.as_view(), ),
    path('<uuid:pk>/comments/', PostCommentListView.as_view(), ),
    path('<uuid:pk>/comments/create/', PostCommentCreateView.as_view(), ),
    path('comments/', CommentListCreateApiView.as_view(), ),
    path('comments/<uuid:pk>/', CommentRetrieveView.as_view(), ),
    path('comments/<uuid:pk>/likes/', CommentLikeListView.as_view(), ),
    path('likes/', AllLikesApiView.as_view(), ),
    path('likes/<uuid:pk>/create/', LikesCreateApiView.as_view(), ),
    path('likes/<uuid:post_id>/delete/', CustomDestroyLikeApiView.as_view(), name='delete-like'),
]