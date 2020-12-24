from django.db import models

# Create your models here.
xray_defetct_type = [
('PNM','Pleumonia'),
('NRM','Normal')
]
class XRAY_Image(models.Model):
    image = models.ImageField(upload_to ='xray_uploads/')
    date_uploaded = models.DateTimeField(auto_now_add=True)
    defect_type = models.CharField(max_length=3,choices=xray_defetct_type,default='NRM')
    description = models.CharField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return '%s - %s' %(self.id,self.date_uploaded)
