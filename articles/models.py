from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()

class PDFS(models.Model):
    name=models.CharField(max_length=256,null=True)
    pdf_file = models.FileField(upload_to="pdfs/", max_length=256)

class Location(models.Model):
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=150)
    date_added = models.DateField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name