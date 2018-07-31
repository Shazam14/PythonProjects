from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django.forms.widgets import CheckboxSelectMultiple
from django.contrib.auth.models import User





class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'name','fathersname','guardiansname', 'address', 'dateofbirth','applicationtype','studentname', 'mobilenumber', 'homenumber', 'civilstatus', 'religion')

        fieldsets = (
            (None, {'fields': ('email', 'password')}),
            ('Personal info', {'email': ('studentname',)}),
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('name', 'email', 'address')



class EditProfileForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username','email', 'first_name', 'last_name', 'dateofbirth', 'studentname', 'address', 'dateuserjoined', 'mobilenumber', 'profilepic', 'religion')


class MedicalForm(forms.Form):
    post_info = forms.CharField(label='Your Medical Condition', max_length=64)

#for medical forms
# class PresentConditionForm(forms.ModelForm):
#
#     class Meta:
#         model = PresentCondition
#
#         field = (
#             'name',
#             'presentconditionchoices',
#         )
#     def save(self, commit=True):
#         condition = super(PresentConditionForm, self).save(commit=False)
#         condition.name = cleaned_data['studentname']
#


#
# immunisationchoices = (
#     ('BCG', 'BCG'),
#     ('DPT1', 'DPT1'),
#     ('DPT2', 'DPT2'),
#     ('DPT3', 'DPT3'),
#     ('DPTB1', 'DPT Booster 1'),
#     ('DPTB2', 'DPT Booster 2'),
#     ('DPTB3', 'DPT Booster 3 range 13-19 years old'),
#     ('PLIO1', 'POLIO 1'),
#     ('PLIO2', 'POLIO 2'),
#     ('PLIO3', 'POLIO 3'),
#     ('PB1', 'POLIO BOOSTER 1'),
#     ('PB2', 'POLIO BOOSTER 2'),
#     ('HIB1', 'HIB 1'),
#     ('HIB2', 'HIB 2'),
#     ('HIB3', 'HIB 3'),
#     ('HIBB', 'HIB BOOSTER'),
#     ('MSLS', 'MEASLES'),
#     ('MMR', 'MMR'),
#     ('MMRB', 'MMRB'),
#     ('HPB1', 'HEPATITIS B1'),
#     ('HPB2', 'HEPATITIS B2'),
#     ('HPB3', 'HEPATITIS B3'),
#     ('HPBB', 'HEPATITIS B BOOSTER'),
#     ('HPA1', 'HEPATITIS A1'),
#     ('HPA2', 'HEPATITIS A2'),
#     ('VRCL', 'VARICELLA - CHICKEN POX'),
#     ('INFLZ', 'INFLUENZA'),
#     ('TYPHD', 'TYPHOID'),
#
#
# )
