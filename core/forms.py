from django import forms
from .models import Review, Order, Master, Service


class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [
        (1, "Очень плохо"),
        (2, "Плохо"),
        (3, "Нормально"),
        (4, "Хорошо"),
        (5, "Отлично"),
    ]

    rating = forms.ChoiceField(
        choices=RATING_CHOICES, widget=forms.Select(attrs={"class": "form-control"})
    )
    master = forms.ModelChoiceField(
        queryset=Master.objects.filter(is_active=True),
        empty_label="Выберите мастера",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Review
        fields = ["master", "client_name", "text", "rating"]
        widgets = {
            "client_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ваше имя"}
            ),
            "text": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Опишите ваш опыт",
                }
            ),
        }


class OrderForm(forms.ModelForm):
    master = forms.ModelChoiceField(
        queryset=Master.objects.filter(is_active=True),
        empty_label="Выберите мастера",
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    services = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"}),
        required=True,
    )
    appointment_date = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local", "class": "form-control", "required": True}
        ),
        label="Дата и время записи",
    )

    class Meta:
        model = Order
        fields = [
            "master",
            "client_name",
            "phone",
            "comment",
            "services",
            "appointment_date",
        ]
        widgets = {
            "client_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Ваше имя"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "+7 (___) ___-__-__"}
            ),
            "comment": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Комментарий (необязательно)",
                }
            ),
        }

    def clean(self):
        return super().clean()
