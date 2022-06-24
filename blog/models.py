from django.db import models

# Create your models here.
class Category(models.Model):
  title = models.CharField(max_length=255)
  slug = models.SlugField()
  
  def __str__(self):
    return self.title
   
  class Meta:
    ordering = ['title']
    verbose_name_plural = 'Categories'
    

class Post(models.Model):
  category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  slug = models.SlugField(null=True)
  description = models.CharField(max_length=255)
  body = models.TextField()
  posted_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.title
    
  class Meta:
    ordering = ('-posted_at',)


class Comment(models.Model):
  post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  email = models.EmailField()
  body = models.TextField()
  commented_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.name