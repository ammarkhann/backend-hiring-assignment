from django.db import models

# Create your models here.
from django.conf import settings

User = settings.AUTH_USER_MODEL



def upload_location(instance,filename):
	return 'user-uploaded-photos/%s/%s' %(instance.user.username,filename)

class Photo(models.Model):
	user        		= models.ForeignKey(User,on_delete=models.CASCADE)
	image 		 		= models.ImageField(upload_to=upload_location,width_field='image_width',height_field='image_height')
	image_width 		= models.PositiveIntegerField(blank=True,null=True)
	image_height 		= models.PositiveIntegerField(blank=True,null=True)
	caption 	   		= models.CharField(max_length=250)
	is_draft 			= models.BooleanField(default=False)
	published_date   	= models.DateField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.caption

