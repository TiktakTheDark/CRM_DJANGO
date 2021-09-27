from django.shortcuts import render, redirect
#from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.forms import UserCreationForm #, AuthenticationForm
#from .forms import CreateUserForm
#from django.contrib.auth import authenticate
from .models import Customer, Category_Article, Offer, Article, Offer_article
from .forms import CustomerModelForm, CategoryModelForm , ArticleModelForm, SimpleArticleModelForm, OfferModelForm, ComplexeArticleModelForm, ArticleFormSet, TestFormSet
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
#from django.forms.formsets import formset_factory
#from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from extra_views import ModelFormSetView, CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory
#CRUD - CREATE - RETRIEVE - UPDATE - DELETE - LIST

class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserCreationForm
    def get_success_url(self):
        return "/login"
    
class HomePageView(TemplateView):
    template_name = "scaffolding/home.html"
    
# CUSTOMER

class CustomerListView(ListView):
    template_name = "scaffolding/customer.html"
    queryset = Customer.objects.all().order_by("name")

class CustomerDetailView(DetailView):
    template_name = "scaffolding/customer_detail.html"
    queryset = Customer.objects.all()

class CustomerCreateView(CreateView):
    template_name = "scaffolding/customer_create.html"
    form_class = CustomerModelForm
    def get_success_url(self):
        return "/customer"

class CustomerUpdateView(UpdateView):
    template_name = "scaffolding/customer_update.html"
    form_class = CustomerModelForm
    queryset = Customer.objects.all()
    def get_success_url(self):
        return "/customer"

class CustomerDeleteView(DeleteView):
    template_name = "scaffolding/customer_delete.html"
    form_class = CustomerModelForm
    queryset = Customer.objects.all()
    def get_success_url(self):
        return "/customer"

# CATEGORY

class CategoryListView(ListView):
    template_name = "scaffolding/category.html"
    queryset = Category_Article.objects.all().order_by("title")

class CategoryDetailView(DetailView):
    template_name = "scaffolding/category_detail.html"
    queryset = Category_Article.objects.all()
    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['form'] = ArticleModelForm
        return context
    def post(self, request, **kwargs):
        form = ArticleModelForm()
        if request.method == "POST":
            form = ArticleModelForm(request.POST)
            if form.is_valid():
                art =  form.save(commit=False)
                art.category_article_id = self.kwargs['pk']
                art.save()
                return redirect("/category")
        context = {"form": form}
        return render(request, "scaffolding/home.html", context) #adress n'existe pas faut la changer

class CategoryCreateView(CreateView):
    template_name = "scaffolding/category_create.html"
    form_class = CategoryModelForm
    def get_success_url(self):
        return "/category"

class ArticleCreateView(CreateView):
    template_name = "scaffolding/article.html"
    form_class = SimpleArticleModelForm
    def get_success_url(self):
        return "/category"

# OFFER

class OfferListView(ListView):
    template_name = "scaffolding/offer.html"
    queryset = Offer.objects.all()

class OfferCreateView(CreateView):
    template_name = "scaffolding/offer_create.html"
    form_class = OfferModelForm
    def get_success_url(self):
        return "/offer"
    
class OfferDetailView(DetailView):
    model = Offer # = queryset = Offer.objects.all()
    template_name = "scaffolding/offer_detail.html"
    #context_object_name = 'list_offre'
    def get_context_data(self, **kwargs):
        context = super(OfferDetailView, self).get_context_data(**kwargs)
        context['test_list'] = Offer.article.through.objects.all().filter(offer_id=self.kwargs['pk'])
        context["test_list2"] = ArticleFormSet()
        return context

class OfferUpdateView(UpdateView):
    template_name = "scaffolding/offer_update.html"
    form_class = OfferModelForm
    queryset = Offer.objects.all()
    def get_context_data(self, **kwargs):
        context = super(OfferUpdateView, self).get_context_data(**kwargs)
        context['test_list'] = Offer.article.through.objects.all().filter(offer_id=self.kwargs['pk'])
        context["test_list2"] = ComplexeArticleModelForm
        return context
    def get_success_url(self):
        return "/offer"
    
class Test(ModelFormSetView):
    model = Customer
    fields="__all__"
    template_name = "scaffolding/test.html"

    def get_success_url(self):
        return "/customer"

class TestItemInline(InlineFormSetFactory):
    model = Offer_article
    fields="__all__"

class TestCreateOrderView(CreateWithInlinesView):
    model = Offer
    inlines = [TestItemInline]
    fields = "__all__"
    template_name = "scaffolding/test2.html"

