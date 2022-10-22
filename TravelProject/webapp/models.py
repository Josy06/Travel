from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()
#def nammal admim pageil kodutha name ath pole kannan vendiann def __str__(self) use cheyune
    def __str__(self):
        return self.name

#meet the team
class Team(models.Model):
    Name=models.CharField(max_length=300)
    Img=models.ImageField(upload_to='photo')
    Role=models.TextField()
    def __str__(self):
        return self.Name

