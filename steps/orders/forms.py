from django import forms
from .models import Order

num = [(i, str(i)) for i in range(1, 21)]


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
        num_del = forms.TypedChoiceField(choices=num, coerce=int, label ="мой текст")
