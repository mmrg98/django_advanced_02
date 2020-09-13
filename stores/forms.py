from django import forms
from stores.models import Store

class StoreModelForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'description']
