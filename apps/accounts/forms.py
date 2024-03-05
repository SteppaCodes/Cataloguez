from django import forms
from django.utils.translation import gettext_lazy as _

from .validators import validate_name
from .models import User

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Enter your email address"}),
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder":"Enter your password"})
    )


class RegisterForm(forms.ModelForm):
    
    first_name = forms.CharField(
        max_length = 50,
        validators=[validate_name],
        widget= forms.TextInput(attrs={"placeholder":"Enter your first name"})
    )
    last_name = forms.CharField(
        max_length = 50,
        validators=[validate_name],
        widget= forms.TextInput(attrs={"placeholder":"Enter your last name"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Enter your email address"}),
    )
    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={"placeholder":"Enter your password"})
    )
    password2 = forms.CharField(
        label = _("Confirm Password"),
        widget=forms.PasswordInput(attrs={"placeholder":"Confirm your password"})
    )

    terms_agreement = forms.BooleanField(
        label="I agree to the terms and conditions",
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "terms_agreement",
        ]

