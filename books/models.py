from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
 
# class Post(models.Model):
#     title = models.CharField(max_length=200, unique=True)
#     slug = models.SlugField(max_length=200, unique=True)
#     author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
#     updated_on = models.DateTimeField(auto_now= True)
#     content = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     status = models.IntegerField(choices=STATUS, default=0)

#     class Meta:
#         ordering = ['-created_on']

#     def __str__(self):
#         return self.title

class Comment(models.Model):
    id=models.IntegerField(primary_key=True)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    book_id=models.IntegerField(default=0)
    username_id=models.IntegerField(default=0)
    class Meta:
        ordering = ['created_date']
    def __str__(self):
        return 'Comment {} by {}'.format(self.text, self.username_id)
    


class genre(models.Model):
    id=models.IntegerField(primary_key=True)
    name= models.TextField()
    class Meta:
        ordering = ['id']
    def __str__(self):
        return '{}'.format(self.name)
    
class homepage(models.Model):
    id=models.IntegerField(primary_key=True)
    image= models.URLField()
    class Meta:
        ordering = ['id']
    def __str__(self):
        return '{}'.format(self.image)

class authors(models.Model):
    id=models.IntegerField(primary_key=True)
    name= models.TextField()
    date_of_birth = models.DateTimeField()
    date_of_death= models.DateTimeField()
    image=models.URLField()
    Bio=models.TextField()
    knowmore=models.URLField()
    penname=models.TextField()
    class Meta:
        ordering = ['name']
    def __str__(self):
        return ' {} {} {}'.format(self.name, self.image, self.Bio)

class details(models.Model):
    id=models.IntegerField(primary_key=True)
    title= models.TextField()
    summary=models.TextField()
    language_id=models.IntegerField(default=0)
    date_posted = models.DateTimeField(auto_now_add=True)
    image=models.URLField()
    bookreview=models.TextField()
    publication=models.TextField()
    buying_link=models.URLField()
    # writer_id=models.IntegerField(default=0)
    writer_id= models.ForeignKey(authors, on_delete=models.CASCADE)
    class Meta:
        ordering = ['date_posted']
    def __str__(self):
        return 'Book {} {} \n Summary: {}\n'.format(self.title, self.image, self.summary)
        
