from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    image = models.ImageField(upload_to = "blog/images/",blank=True)
    date = models.DateField(default="2022-10-10")
    url = models.URLField(blank=True)


    def __str__(self):
        return self.title
