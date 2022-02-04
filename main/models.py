from django.db import models

# Create your models here.
class Post(models.Model):
    postname = models.CharField(max_length = 50)
    mainphoto = models.ImageField(blank=True, null=True)
    contents = models.TextField()
    # model.DateTimeField('date published') 도 가능

    def __str__(self):
        return self.postname
