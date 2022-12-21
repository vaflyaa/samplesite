from django import forms
from .models import Bb, Rubric
from django.core.exceptions import ValidationError


class BbForm(forms.ModelForm):
    title = forms.CharField(label='Название товара')
    content = forms.CharField(label='Описание', widget=forms.widgets.Textarea())
    price = forms.DecimalField(label='Цена', decimal_places=2)
    rubric = forms.ModelChoiceField(queryset=Rubric.objects.all(), 
                                    label='Рубрика', 
                                    help_text='Не забудьте выбрать рубрику!')

    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'kind', 'rubric')
    
    def clean(self):
        super().clean()
        errors = {}
        if not self.cleaned_data['content']:
            errors['content'] = ValidationError('Укажите описание товара!')
        if self.cleaned_data['price'] < 0:
            errors['price'] = ValidationError('Укажите неотрицательное значени цены!')
        if errors:
            raise ValidationError(errors)
            