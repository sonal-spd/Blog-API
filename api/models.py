from django.db import models
from django.contrib.auth.models import User
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class Post(models.Model):
    created = models.DateTimeField('created',auto_now_add=True)
    modified = models.DateTimeField('modified',auto_now=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'post_images/',null = True,blank = True,default = 'none')
    status = models.IntegerField(choices=STATUS,default=0)

    class Meta:
        ordering = ['created']
    def __str__(self):
        return self.title