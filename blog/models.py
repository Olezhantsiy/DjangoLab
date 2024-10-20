from  django.contrib.auth.models import  User
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE);
    def __str__(self):
        return self.title
    def get_short_text(self):
        if len(self.text) > 300:
            return ' '.join(self.text.split()[:45]) + "..."
        else:
            return self.text


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=400)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.comment[:60]


