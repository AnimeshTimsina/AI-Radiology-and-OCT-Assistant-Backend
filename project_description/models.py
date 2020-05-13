from django.db import models

class SourceCategory(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Source Categories'

    def __str__(self):
        return self.name

class SourceLinks(models.Model):
    category = models.ForeignKey(SourceCategory,on_delete=models.CASCADE,related_name='links')
    url = models.URLField()
    desc = models.CharField(max_length=5000)

    class Meta:
        verbose_name_plural = 'Source Links'

    
    

