from django.contrib import admin
# Register your models here.

from .models import *

admin.site.register(Technician)
admin.site.register(Customer)
admin.site.register(Offer)
admin.site.register(Contact)
admin.site.register(Offer_article)


class Tabular(admin.TabularInline):
    model = Article
    extra = 0
    
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "num")
    search_fields = ("title", "num")
    readonly_fields = ()
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    inlines = [Tabular]
    class Meta:
        Model = Category_Article
        
    
#admin.site.register(Category_Article, Category_Admin)
        
admin.site.register(Category_Article, QuestionAdmin)

admin.site.register(Article)


    