from django.db import models

# Create your models here.

class Post(models.Model):
    # author
    # image
    title = models.CharField(max_length=255)
    content = models.TextField()
    # category
    # tag
    counted_view = models.IntegerField(default=0)   
    status = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title