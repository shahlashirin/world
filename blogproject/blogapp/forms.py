from.models import blog
from django import forms
class ModeForm(forms.ModelForm):
    class Meta:
        model=blog
        fields=['name','desc','image']