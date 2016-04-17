from django.db import models

class Article(models.Model):
    class Meta:
        db_table = 'article'
    article_title = models.CharField(max_length=400)
    article_text = models.TextField()
    article_date = models.DateTimeField()