from django.shortcuts import get_object_or_404
from posts.models import Group, Post, Follow
from rest_framework import viewsets

from .permissions import IsOwnerOrReadOnly
from .serializers import CommentSerializer, GroupSerializer, PostSerializer, FollowSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        pk = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=pk)
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        pk = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=pk)
        return post.comments.all()


class FollowViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
