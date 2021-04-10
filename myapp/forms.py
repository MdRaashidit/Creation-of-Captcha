from django import forms
from captcha.fields import CaptchaField

class raashid(forms.Form):
        captcha=CaptchaField()
    
