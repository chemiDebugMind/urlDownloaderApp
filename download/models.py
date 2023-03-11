from django.db import models

# Create your models here.


class Downloader(models.Model):
    urls = models.TextField()
    ip_address = models.GenericIPAddressField()
    receiver_email  =models.EmailField(blank=True)
    downloaded_at = models.DateTimeField(auto_now_add=True)




