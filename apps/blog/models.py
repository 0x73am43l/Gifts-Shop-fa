from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.contenttypes.fields import GenericRelation
from .choices import LikeChoice

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)
    object = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'دسته'
        verbose_name_plural = 'دسته بندی'
        # ordering = 'id'


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='article_set', verbose_name='دسته بندی')
    title = models.CharField(max_length=200, verbose_name='عنوان')
    slug = models.SlugField(max_length=200, unique=True)
    content = RichTextField(blank=True, null=True, verbose_name='محتوا')
    # author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='article_set')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # status = models.PositiveSmallIntegerField(choices=)
    # image = models.ImageField(upload_to='articles/', blank=True, default=)
    object = models.Manager()
    # vote = GenericRelation(Like, related_query_name='articles')

    @property
    def short_title(self):
        return self.title[:30]

    def __str__(self):
        return '{title} - {author}'.format(title=self.short_title, author=self.author)

    def likes(self):
        return self.vote.aggregate(
            count = models.Count(
                'vote', filter=models.Q(vote=LikeChoice.LIKE)
            )
        )

    def dislike(self):
        return self.vote.aggregate(
            count = models.Count(
                'vote', filter=models.Q(vote=LikeChoice.DISLIKE)
            )
        )

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ('-updated', '-created', 'id')
