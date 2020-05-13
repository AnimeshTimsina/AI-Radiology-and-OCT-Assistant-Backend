from django.db import models

defect_type = [
    ('CNV','Choroidal neovascularization(CNV)'),
    ('DME','Diabetic macular edema (DME)'),
    ('DRN','Drusen'),
    ('NRM','Normal')
]

class OCT_Image(models.Model):
    image = models.ImageField(upload_to ='oct_uploads/')
    date_uploaded = models.DateTimeField(auto_now_add=True)
    defect_type = models.CharField(max_length=3,choices=defect_type,default='NRM')
    description = models.CharField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return '%s - %s' %(self.id,self.date_uploaded)
