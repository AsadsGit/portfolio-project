from django.db import models


class blogpost(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    body = models.TextField (max_length=2000)
    
    def __str__(self):
        return self.title 




