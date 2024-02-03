from django.db import models
from django.utils.text import slugify
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from base.models import TimeStampedModel


class Category(MPTTModel, TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    order = models.IntegerField(default=0)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

