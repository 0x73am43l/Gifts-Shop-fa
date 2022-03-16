from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name='کتگوری')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='اسلاگ')
    image = models.ImageField(verbose_name='تصویر')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '۱ - دسته بندی'


class Product(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name='نام محصول')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='Products', verbose_name='کتگوری')
    description = RichTextField(null=True, verbose_name='توضیحات')
    image = models.ImageField(verbose_name='تصویر')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='اسلاگ')
    avaliable = models.BooleanField(default=True, verbose_name='موجود')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '۲ - محصول'


class Region(models.Model):
    # class country(models.TextChoices):
    #
    #
    # country = models.CharField(max_length=60, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    image = models.ImageField(verbose_name='تصویر')

    # available = models.M

    def __str__(self):
        return self.country

    class Meta:
        verbose_name_plural = '۳ - ریجن'


class Item(models.Model):
    title = models.CharField(max_length=50, null=True, verbose_name='عنوان')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='ریجن')
    image = models.ImageField(verbose_name='تصویر')
    price = models.PositiveBigIntegerField(verbose_name='قیمت')
    code = models.CharField(max_length=50, null=True, verbose_name='کد گیفت')
    slug = models.SlugField(max_length=150, unique=True, verbose_name='اسلاگ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '۴ - آیتم'


class AskedQuestions(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    content = RichTextField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '۴ - آیتم'



class Comments(models.Model):
    pass