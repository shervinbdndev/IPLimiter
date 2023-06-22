from typing import Self
from django.db import models





class IPModel(models.Model):
    OPTIONS: tuple[tuple[bool, str]] = (
        (False, 'No'),
        (True, 'Yes'),
    )
    
    user_agent = models.CharField(max_length=200, null=True, blank=True, verbose_name='User Agent')
    ip = models.CharField(max_length=50, null=True, blank=True, verbose_name='IP')
    limit = models.BooleanField(choices=OPTIONS, default= False, blank=True, null=True, verbose_name='Is Limited')
    
    def __str__(self: Self) -> str:
        super(IPModel, self).__str__()
        return self.ip
    
    class Meta:
        verbose_name = 'IP'
        verbose_name_plural = 'IPs'