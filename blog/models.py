from django.db import models

# Create your models here.

# Model for Category
class Category(models.Model):
    name = models.CharField(max_length=30)
# Fix plural form
    class Meta:
            verbose_name_plural = "categories"

    def __str__(self):
            return self.name

#Model for Post
class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    #Create and Modified Date and Time
    create_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    #creates a many to many relationship between a post and categories
    categories = models.ManyToManyField("Category", related_name="posts")

    def __str__(self):
        return self.title

# MOdel for Comments
class Comment(models.Model):
    author = models.CharField(max_length=250)
    body = models.TextField()

    #Comment time 
    create_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on '{self.post}'"

