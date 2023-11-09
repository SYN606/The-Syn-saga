from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from autoslug import AutoSlugField
from taggit.managers import TaggableManager


class Blog(models.Model):
    blog_title = models.CharField(max_length=50)
    tags = TaggableManager()
    desc = models.CharField(max_length=50)
    content = RichTextUploadingField()
    slug = AutoSlugField(populate_from='blog_title', unique=True, null=True, default=None)
    date = models.DateField(auto_now=True)
    

    def __str__(self) -> str:
        return self.blog_title