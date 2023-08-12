from django.urls import path, re_path

urlpatterns = [
    # ex: /forum/
    path('', 'views.index', name='index'),

    # ex: /forum/5/
    path('<int:post_id', 'views.detail', name='detail'),

    # ex: /forum/5/comment/
    path('<int:post_id>/comment/', 'views.comment', name='comment'),

    # ex: /posts/2023/
    re_path(r'^posts/(?P<year>[0-9]{4})/$', 'views.year_archive', name='by_year'),

    # ex: /posts/2023/3
    re_path(r'^posts/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', 'views.month_archive', name='by_month'),

    # ex: /posts/2023/3/post-slug/
    re_path(r'^posts/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$', 'views.post_detail', name='slug_detail'),
]
