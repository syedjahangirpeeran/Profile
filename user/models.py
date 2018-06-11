from django.db import models

# Create your models here.
class Post(models.Model):
	user_id = models.CharField(max_length=20)
	url = models.CharField(max_length=100)
	image = models.CharField(max_length=100)
	description = models.CharField(max_length=1000)
	likes = models.IntegerField()
	dislikes = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
	comment = models.ForeignKey(Post, on_delete = models.CASCADE)
	top1 = models.CharField(max_length=500)
	top2 = models.CharField(max_length=500)