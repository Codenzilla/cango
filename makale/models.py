from django.db import models
from ckeditor.fields import RichTextField

class Makale(models.Model):
    yazar = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Yazar")
    baslik = models.CharField(max_length = 50,verbose_name="Başlık")
    icerik = RichTextField()
    olusturmaZamani = models.DateTimeField(auto_now_add = True,verbose_name="Oluşturulma Tarihi")
    article_image = models.FileField(blank = True, null = True,verbose_name="Foto Ekle",upload_to='media/')
    def __str__(self):
        return self.baslik

    class Meta:
        ordering = ['-olusturmaZamani']

class Comment(models.Model):
    article = models.ForeignKey(Makale, on_delete = models.CASCADE, verbose_name = "makale", related_name = "comments")
    comment_author = models.CharField(max_length = 50, verbose_name = "İsim")
    comment_content = models.CharField(max_length = 200, verbose_name = "Yorum")
    comment_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.comment_content
    
    class Meta:
        ordering = ['-comment_date']