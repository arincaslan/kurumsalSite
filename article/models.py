from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from unidecode import unidecode

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 50, verbose_name="Başlık")
    content = RichTextField(('Makale İçeriği'))
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    article_slug = models.SlugField(unique= True, default='defaultVal')
    article_meta_description = models.CharField(('Makale Meta Açıklaması'), max_length= 250, default= 'default meta acıklaması')

    KATEGORILER = (
        ('Mobil Uygulamar', 'Mobil Uygulamalar'),
        ('Web Tasarımları', 'Web Tasarımları'),
        ('Reklam Hizmetleri', 'Reklam Hizmetleri'),
    )

    article_kategori = models.CharField(('Makale Kategorisi'), max_length=50, choices=KATEGORILER, default= 'websitesi')

    def __str__(self):
        return self.title

    class Meta:
        ordering= ('-created_date',)
        verbose_name = 'Makale'
        verbose_name_plural = 'Makaleler'

    def save(self, *args, **kwargs):
        self.article_slug = slugify(unidecode(self.title))
        super(Article, self).save(*args, **kwargs)
