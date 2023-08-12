from typing import Any, Dict
from django import http
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post, Comment

def index(request):
    return HttpResponse('<html><body>Our first response</body></html>')

class PostListView(ListView):
    model = Post
    context_object_name = 'post_data'

    def get_queryset(self):
        self.queryset = Post.objects.all()

        if self.kwargs.get('year'):
            self.queryset = self.queryset.filter(created_at__year=self.kwargs['year'])

        if self.kwargs.get('month'):
            self.queryset = self.queryset.filter(created_at__month=self.kwargs['month'])

        return self.queryset

    def render_to_response(self, context: Dict[str, Any], **response_kwargs: Any) -> HttpResponse:
        posts = ''

        for post in context['post_data']:
            posts += f'<li>{post.title}</li>'

        return HttpResponse(f'<html><body>{posts}</body></html>')


class PostDetailView(DetailView):
    model = Post

    def render_to_response(self, context: Dict[str, Any], **response_kwargs: Any) -> HttpResponse:
        post = context.get('object')
        return HttpResponse(f'<html><body><ul><li>Title: {post.title}</li><li>Body: {post.body}</li><li>User: {post.user.first_name}</li></ul></body></html>')


class CommentListView(ListView):
    model = Comment
    context_object_name = 'comment_data'

    def get_queryset(self) -> QuerySet[Any]:
        self.queryset = Comment.objects.filter(post__id=self.kwargs['post_id'])
        return self.queryset

    def render_to_response(self, context: Dict[str, Any], **response_kwargs: Any) -> HttpResponse:
        comments = ''

        for comment in context['comment_data']:
            comments += f'<li>{comment.body}</li>'

        return HttpResponse(f'<html><body><ul>{comments}</ul></body></html>')
