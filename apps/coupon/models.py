from django.db import models
from django.core.exceptions import ValidationError


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name='کد')
    valid_from = models.DateTimeField(verbose_name='معتبر از')
    valid_to = models.DateTimeField(verbose_name='معتبر تا')
    discount = models.IntegerField(verbose_name='تخفیف')
    active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        return self.code

    def clean(self):
        super(Coupon, self).clean()
        if self.valid_to <= self.valid_from:
            raise ValidationError('"valid to" should bigger than "valid from"')

    class Meta:
        verbose_name_plural = 'کد تخفیف'
        verbose_name = 'کد های تخفیف'
