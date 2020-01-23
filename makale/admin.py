from django.contrib import admin

from .models import Makale,Comment

admin.site.register(Comment)

@admin.register(Makale)
class MakaleAdmin(admin.ModelAdmin):
    list_display = ["baslik","yazar","olusturmaZamani"]
    list_display_links = ["baslik", "olusturmaZamani"]
    search_fields = ["baslik"]
    list_filter = ["olusturmaZamani"]
    class Meta:
        model = Makale

