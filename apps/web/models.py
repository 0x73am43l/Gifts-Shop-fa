from django.db import models


class SiteSetting(models.Model):
    site_title = models.CharField(max_length=60, help_text="بهتر است عنوان اصلی را بین 50 تا 60 کاراکتر وارد کنید", verbose_name='عنوان سایت')
    logo = models.ImageField(upload_to='web/logo', help_text='لطفا رنگ پس زمینه لوگوی خود را بی رنگ یا 181818# قرار دهید', verbose_name='لوگو')
    admin_logo = models.ImageField(upload_to='web/logo', help_text='لطفا رنگ پس زمینه لوگوی خود را بی رنگ قرار دهید', verbose_name='لوگوی ادمین')
    favicon = models.ImageField(upload_to='main/favicon', null=True, blank=True)
    meta_description = models.TextField(max_length=160, help_text="توضیحات متا قابل قبول باید بین 155 یا 160 کاراکتر باشد", null=True, blank=True, verbose_name='توضیحات متا')

    class Meta:
        verbose_name_plural = "تنضیمات سایت"
        verbose_name = "تنضیمات"

    def __str__(self):
        return self.site_title


class Slider(models.Model):
    title = models.CharField(max_length=15, blank=True, verbose_name="عنوان اسلاید")
    link = models.CharField(max_length=120, verbose_name="لینک اسلاید")
    description = models.TextField(max_length=120, null=True, blank=True, verbose_name='توضیحات')
    image = models.ImageField(verbose_name='تصویر اسلاید')

    class Meta:
        verbose_name_plural = "اسلاید ها"
        verbose_name = "اسلاید"


class Footer(models.Model):
    pass

    class Meta:
        verbose_name_plural = "فوتر(Footer)"
        verbose_name = "فوتر"


class SocialMedia(models.Model):
    ICON = (
        ("Instagram", "اینستاگرام"),
        ("Telegram", "تلگرام"),
        ("Whatsapp", "واتس آپ"),
        ("Facebook", "فیسبوک"),
        ("Youtube", "یوتوب"),
        ("Aparat", "آپارات"),
    )
    title = models.CharField(max_length=50, null=True, verbose_name='عنوان')
    link = models.CharField(max_length=120, verbose_name='لینک')
    icon_code = models.CharField(max_length=15, choices=ICON, verbose_name='کد آیکون')

    class Meta:
        verbose_name_plural = "شبکه های اجتماعی"
        verbose_name = "شبکه اجتماعی"
