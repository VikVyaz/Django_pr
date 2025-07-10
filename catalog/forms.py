from django.forms import ModelForm
from .models import Product
from django.core.exceptions import ValidationError


class StyleFromMixin:
    placeholder_data = {}
    form_class_data = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            data = {
                'class': self.form_class_data.get(name, 'form-control'),
                'placeholder': self.placeholder_data.get(name, '')
            }

            self.fields[name].widget.attrs.update(data)


class ProductForm(StyleFromMixin, ModelForm):
    placeholder_data = {
        'name': 'Наименование продукта',
        'description': 'Описание продукта',
        'image': 'Изображение продукта',
        'category': 'Категория продукта',
        'price': 'Цена продукта'
    }

    form_class_data = {
        'category': 'form-select'
    }

    @staticmethod
    def __ban_bad_words(context):
        for bw in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']:
            if bw in context.lower():
                return bw
        return False

    def clean_name(self):
        name = self.cleaned_data.get('name')
        validation_result = self.__ban_bad_words(name)
        if validation_result:
            raise ValidationError(f'Имя товара не может содержать слово "{validation_result}"')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        validation_result = self.__ban_bad_words(description)
        if validation_result:
            raise ValidationError(f'Описание товара не может содержать слово "{validation_result}"')
        return description

    def clean_price(self):
        # Либо так, либо в модели указать price = models.PositiveIntegerField()
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError('Цена товара должна быть больше нуля')
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 1024 * 1024 * 5:
                raise ValidationError('Размер изображения должно быть не больше 5 МБ')
            if image.content_type not in ['image/jpeg', 'image/png']:
                raise ValidationError('Формат изображения: JPEG или PNG')
        return image

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'image']
