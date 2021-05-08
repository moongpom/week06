from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    writer=models.CharField(max_length=50)
    publisher=models.CharField(max_length=50)
    pub_date=models.CharField(max_length=30)
    body=models.TextField()
    image = models.ImageField(upload_to="blog/",blank=True,null=True)
    def __str__(self):
        return self.title

   