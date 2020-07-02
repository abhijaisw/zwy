from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField



# Create your models here.
class Blog(models.Model):
    blog_id			= models.AutoField(primary_key=True)
    title 			= models.CharField(max_length=200)
    category		= models.CharField(max_length=200, blank=True, null=True)
    sub_cat			= models.CharField(max_length=200, blank=True, null=True)
    blog_image 		= models.ImageField(upload_to='images/', blank=True, null=True)
    desc 			= RichTextUploadingField()
    pub_date 		= models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Image(models.Model):
	title			=models.CharField(max_length=200, blank=True, null=True)
	images 			=models.ImageField(upload_to='images/', blank=True, null=True)
	pub_date		=models.DateField(auto_now_add=True)


class Video(models.Model):
    title           =   models.CharField(max_length=200, blank=True, null=True)
    thumbnail       =   models.ImageField(upload_to='images/')
    video_file      =   models.FileField(upload_to='videos/')