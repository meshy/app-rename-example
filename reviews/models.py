from django.conf import settings
from django.db import models


from catalogue.models import Product


class Review(models.Model):
    RATING_CHOICES = [(i, unicode(i) + u' out of 5') for i in range(1, 6)]

    comment = models.TextField(blank=True, default=u'')
    product = models.ForeignKey(Product)
    rating = models.IntegerField(choices=RATING_CHOICES)
    title = models.CharField(blank=True, default=u'', max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
