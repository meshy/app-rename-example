from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category)
    sku = models.CharField(max_length=255)

    def __unicode__(self):
        return self.sku
