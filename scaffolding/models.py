from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#To create initial migrations for an app, run makemigrations and specify the app name. The migrations folder will be created.
#./manage.py makemigrations <myapp>





class Technician(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    adress = models.CharField(max_length=200, null=True)
    zip_code = models.IntegerField(default=0, null=True)
    city = models.CharField(max_length=200, null=True)
    phone = models.IntegerField(default=0, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.title + " " + self.first_name

class Customer(models.Model):
    title = models.CharField(max_length=200, null=True, default="Entreprise", blank=True)
    name = models.CharField(max_length=200, null=True)
    adress = models.CharField(max_length=200, null=True, blank=True)
    zip_code = models.IntegerField(default=0, null=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.title + " " + self.name
    

    
class Offer(models.Model):
    STATUS = (
        ("Work in Progress", "Work in Progress"),
        ("Sended to Customer", "Sended to Customer"),
        ("Accepted", "Accepted"),
        ("Declined", "Declined"),
        )
    title = models.CharField(max_length=200, null=True)
    construction_site_name = models.CharField(max_length=200, null=True)
    construction_site_adress = models.CharField(max_length=200, null=True)
    construction_site_zip_code = models.IntegerField(default=0, null=True)
    construction_site_city = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    article = models.ManyToManyField("Article", through="Offer_article")
    def __str__(self):
        return str(self.customer)
    
class Category_Article(models.Model):
    title = models.CharField(max_length=200, null=True)
    num = models.IntegerField(default=100, null=True, blank=True)
    def __str__(self):
        return str(self.num) + " - " + self.title
    
class Article(models.Model):
    title = models.CharField(max_length=200, null=True)
    num = models.IntegerField(default=100, null=True, blank=True)
    prix_installation = models.FloatField(default=0, null=True, blank=True)
    date_installation = models.DateField(null=True, blank=True)
    prix_location = models.FloatField(default=0, null=True, blank=True)
    date_debut_location = models.DateField(null=True, blank=True)
    date_fin_location = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category_article = models.ForeignKey(Category_Article, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.num) + " - " +  self.title
    
class Offer_article(models.Model):
    offer =  models.ForeignKey(Offer, null=True, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)

class Contact(models.Model):
    title = models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    adress = models.CharField(max_length=200, null=True)
    zip_code = models.IntegerField(default=0, null=True)
    city = models.CharField(max_length=200, null=True)
    phone = models.IntegerField(default=0, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.title + " " + self.first_name + " " + self.customer.title + " " + self.customer.name


"""


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)
    quantity = models.FloatField(null=True)
    price = models.FloatField(null=True)
    def __str__(self):
        return self.name
    
    
class Article(models.Model):
    CATEGORY = (
        ("Echaudage de façade", "Echaudage de façade"),
        ("Supplément échafaudage de façade", "Supplément échafaudage de façade"),
        ("Echafaudage lourd", "Echafaudage lourd"),
        ("Travaux spéciaux", "Travaux spéciaux"),
        
        )
    name = models.CharField(max_length=200, null=True)
    price =  models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)#il faudrais une arborescence la dériere
    
    def __str__(self):
        return self.name
    
class Offer(models.Model):
    
    STATUS = (
        ("Work in Progress", "Work in Progress"),
        ("Sended to Customer", "Sended to Customer"),
        ("Accepted", "Accepted"),
        ("Declined", "Declined"),
        )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)#lie notre offre a customer
    article = models.ManyToManyField(Article)#il faudrais une arborescence la dériere
    #article = models.ForeignKey(Article, null=True, on_delete=models.SET_NULL)#lie notre offre à un Article ***NUL***
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)#ok
    construction_site_name = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.customer.first_name + " " + self.customer.last_name + " " + self.construction_site_name
    

class Contact(models.Model):
    
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.first_name + " " + self.last_name
    
    class Installation(models.Model):
    title = models.CharField(max_length=200, null=True)
    qty = models.CharField(max_length=200, null=True, blank=True)
    unity = models.CharField(max_length=200, null=True, blank=True)
    price = models.CharField(max_length=200, null=True, blank=True)
    date_montage = models.DateField(blank=True)
    date_demontage = models.DateField(blank=True)
    
class Location(models.Model):
    title = models.CharField(max_length=200, null=True)
    qty = models.CharField(max_length=200, null=True, blank=True)
    unity = models.CharField(max_length=200, null=True, blank=True)
    price = models.CharField(max_length=200, null=True, blank=True)
    date_debut_location = models.DateField(blank=True)
    date_fin_location = models.DateField(blank=True)
"""
    
    