from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"placeholder": "Enter your email address"}),
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder":"Enter your password"})
    )

