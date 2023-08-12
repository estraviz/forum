from django.contrib.syndication.views import Feed
from django.db.models.base import Model
from django.urls import reverse

from .models import Post


class LatestPostFeed(Feed):
    title = 'Our Posts'
    link = '/latest/posts'
    description = 'Latest posts made.'

    def items(self):
        return Post.objects.order_by('-created_at')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item: Model) -> str:
        return item.body

    def item_link(self, item: Model) -> str:
        return reverse('detail', args=[item.pk])
