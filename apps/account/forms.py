from django import forms
from . import models


class OtpPhoneInputForm(forms.ModelForm):
    class Meta:
        model = models.MyUser
        fields = ['phone']
        widgets = {
            'phone': forms.TextInput({
                "class": 'form-control mt-4',
                "id": "yourphone",
                "placeholder": "(۹۱۲) ۱۲۰-۱۲۰۰",
                "pattern": ".{10,}",
                "maxlength": "10",
                "oninvalid": "setCustomValidity('شماره شما باید ۱۰ رقم باشد')",
                "oninput": "setCustomValidity('')",
                "style": "text-align: center; direction: ltr"
            })
        }
        labels = {
            'phone': ''
        }
        # widget = {'phone': forms.TextInput(),
        #           attrs={
        #                 "class": 'form-control mt-4',
        #                 "id": "yourphone",
        #                 "placeholder": "(۹۱۲) ۱۲۰-۱۲۰۰",
        #                 "pattern": ".{10,}",
        #                 "maxlength": "10",
        #                 "oninvalid": "setCustomValidity('شماره شما باید ۱۰ رقم باشد')",
        #                 "oninput": "setCustomValidity('')",
        #                 "style": "text-align: center; direction: ltr"
        #     }
        # }

    # phone = forms.CharField(
    #     label='',
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": 'form-control mt-4',
    #             "id": "yourphone",
    #             "placeholder": "(۹۱۲) ۱۲۰-۱۲۰۰",
    #             "pattern": ".{10,}",
    #             "maxlength": "10",
    #             "oninvalid": "setCustomValidity('شماره شما باید ۱۰ رقم باشد')",
    #             "oninput": "setCustomValidity('')",
    #             "style": "text-align: center; direction: ltr"
    #         }
    #     )
    # )