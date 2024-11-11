from django import forms
from django.core import validators


class contactForm(forms.Form):
    name = forms.CharField(
        label="User Name",
        # initial="Rahim",
        help_text="Total length must be within 70 characters",
        required=False,
        widget=forms.Textarea(
            attrs={
                "id": "text_area",
                "class": "adding_classes",
                "placeholder": "Enter you name here",
            }
        ),
    )
    # file = forms.FileField()
    # email = forms.EmailField(label="User Email")
    # age = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # check = forms.BooleanField()
    # birthday = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    appointment = forms.DateTimeField(
        widget=forms.DateInput(attrs={"type": "datetime-local"})
    )
    CHOICES = [("s", "Small"), ("m", "Medium"), ("l", "Large")]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    MEAT = [("p", "Pepperoni"), ("m", "Mashroom"), ("b", "Beef")]
    pizze = forms.MultipleChoiceField(
        choices=MEAT, widget=forms.CheckboxSelectMultiple()
    )


# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput())
#     email = forms.CharField(widget=forms.EmailInput())

#     def clean(self):
#         cleaned_data = super().clean()
#         stName = self.cleaned_data["name"]
#         stEmail = self.cleaned_data["email"]
#         if len(stName) < 10:
#             raise forms.ValidationError("Enter at least 10 characters")
#         if ".com" not in stEmail:
# raise forms.ValidationError("Your email must contain .com")


def len_check(text):
    if len(text) < 10:
        raise forms.ValidationError("Enter a name more than 10 character")


class StudentData(forms.Form):
    text = forms.CharField(validators=[len_check])
    name = forms.CharField(
        widget=forms.TextInput(),
        validators=[
            validators.MinLengthValidator(10, message="Enter at least 10 characters")
        ],
    )
    email = forms.CharField(
        widget=forms.EmailInput(), validators=[validators.EmailValidator()]
    )
    age = forms.IntegerField(
        validators=[validators.MaxValueValidator(30), validators.MinValueValidator(10)]
    )
    file = forms.FileField(
        validators=[validators.FileExtensionValidator(allowed_extensions=["pdf"])]
    )
