from django.urls import path, re_path
from .views import CommentListView, PostDetailView, PostListView, TestTemplateView, index

urlpatterns = [
    # ex: /forum/
    path('', index, name='index'),

    # ex: /forum/5/
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),

    path('test/', TestTemplateView.as_view(), name='template'),

    # ex: /forum/5/comment/
    path('<int:post_id>/comment/', CommentListView.as_view(), name='comment'),

    # ex: /posts/2023/
    re_path(r'^posts/(?P<year>[0-9]{4})/$', PostListView.as_view(), name='by_year'),

    # ex: /posts/2023/3
    re_path(r'^posts/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', PostListView.as_view(), name='by_month'),

    # # ex: /posts/2023/3/post-slug/
    # re_path(r'^posts/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$', 'views.post_detail', name='slug_detail'),
]
