from django.db import models


class Review(models.Model):
    user_name = models.CharField(max_length=100, null=True)
    feedback = models.TextField(null=True)
    rating = models.IntegerField(null=True)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Review"
