from django.db import models

# Create your models here.


class MenuPicture(models.Model):
    picture = models.ImageField()
    food_name = models.CharField(max_length=50, null=True, blank=True)


class BookTable(models.Model):
    email = models.EmailField()
    NoOfGuest = models.IntegerField()
    time = models.TimeField(auto_now=False, auto_now_add=False)
    date = models.DateField()


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class FoodBlog(models.Model):
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    picture = models.ImageField()
    price = models.IntegerField()
    blog_name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)


class Reviews(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    description = models.CharField(max_length=100)


