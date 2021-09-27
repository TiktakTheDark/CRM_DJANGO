
#from django.forms import ModelForm
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from django import forms
from .models import Customer, Category_Article, Article, Offer, Offer_article
from django.forms import inlineformset_factory, formset_factory, modelformset_factory





"""
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
"""


    
class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            "title",
            "name",
            "adress",
            "zip_code",
            "city",
            "phone",
            "email",
            )
        

    
class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category_Article
        fields = (
            "title",
            "num",
            )
        
        

class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = (
            "title",
            "num",
            )



class SimpleArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = (
            "title",
            "num",
            "category_article"
            )
   
class OfferModelForm(forms.ModelForm):
    class Meta:
        model = Offer      
        fields = (
                "title",
                "construction_site_name",
                "construction_site_adress",
                "construction_site_zip_code",
                "construction_site_city",
                "status",
                "customer",
                "article",
            )



class ComplexeArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article      
        fields = (
                "title",
                "num",
                "prix_installation",
                "date_installation",
                "prix_location",
                "date_debut_location",
                "date_fin_location",
            )

ArticleFormSet = inlineformset_factory(Article, Offer_article, fields=("title",), extra=3)

TestFormSet = formset_factory(Customer)
