from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    # Text - field for custom text
    # pub_date - field for date. auto_now_add allows to fill the field with today's date
    # author - model with the link to different model or "different table". In this case
    # it is a link to User model
    # With arguments in User,  each User object will have posts property added
    text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
# Create your models here.
