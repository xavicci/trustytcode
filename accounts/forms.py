from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
)
from accounts.models import CustomUser
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            "username",
            "email",
            "edad",
            "telefono",
            "pais",
        )

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "edad",
            "telefono",
            "pais",
        )


class UserLoginForm(AuthenticationForm):

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
