from django.db import models

# Create your models here.
class RegUser(models.Model):
    Name=models.CharField(max_length=100)
    Designation= models.CharField(max_length=100)
    Organisation = models.CharField(max_length=100)
    Address= models.CharField(max_length=100)
    Mob=models.CharField(max_length=15)
    Email=models.CharField(max_length=100)
    Membership=models.CharField(max_length=100)     
    DD=models.CharField(max_length=100, blank=True)
    Amount=models.CharField(max_length=100, blank=True)
    Bank=models.CharField(max_length=15, blank=True)
    Branch=models.CharField(max_length=100, blank=True)
    Date=models.CharField(max_length=100, blank=True)
    
    
    def __unicode__(self):
        return "%s, %s" % (self.Name, self.Organisation)

    def __str__(self):
        return "%s, %s" % (self.Name, self.Organisation)
