from django.db import models
from django.contrib.auth.models import User,AbstractUser, AbstractBaseUser


# Create your models here.
class Bed(models.Model):
    bed_no = models.CharField(max_length=3, blank=True, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.bed_no
    
class Booking(models.Model):
    date = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    bed = models.ForeignKey(Bed, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.user) +"_"+ str(self.bed)