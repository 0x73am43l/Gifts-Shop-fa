from django import template


register = template.Library()

@register.filter(name='persian_digits')
def persian_int(english_int):
    persian_nums= ('۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹')
    number = str(english_int)
    return ''.join(persian_nums[int(digit)] for digit in number)