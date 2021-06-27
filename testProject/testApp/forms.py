from django.contrib.auth.models import User
from django.forms import ModelForm

from testApp.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('productname', 'brand','price')


class signupform(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
