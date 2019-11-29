from django import forms
from . import models
    # program             = models.ForeignKey(Program,on_delete=models.CASCADE,verbose_name='프로그램')
    # name                = models.CharField('학생이름', max_length=256)
    # school              = models.CharField('출석학교', max_length=256)
    # school_year         = models.IntegerField('학년')
    # gender              = models.CharField('성별',max_length=2, choices=genders,)
    # contact             = models.CharField('연락처', max_length=256, validators=[phone_regex])
    # guardian_name       = models.CharField('신청인 이름',max_length=256)
    # guardian_contact    = models.CharField('보호자 연락처', max_length=256, validators=[phone_regex])
class SignUpModelForm(forms.ModelForm):
    class Meta:
        model = models.ProgramSignUp
        exclude = ['created_at','program']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': '학생 이름을 입력하세요',
                    'class':'form-control',
                    }
                ),
            'school': forms.TextInput(
                attrs={
                    'placeholder': '학생 이름을 입력하세요',
                    'class':'form-control',
                    }
                ),
            'school_year': forms.TextInput(
                attrs={
                    'placeholder': '학생 이름을 입력하세요',
                    'class':'form-control',
                    }
                ),
            'gender': forms.Select(
                attrs={
                    'class':'form-control',
                    }
                ),
            'contact': forms.TextInput(
                attrs={
                    'placeholder': '010-xxxx-xxxx',
                    'class':'form-control',
                    }
                ),
            'guardian_name': forms.TextInput(
                attrs={
                    'placeholder': '신청인(보호자) 이름',
                    'class':'form-control',
                    }
                ),
            'guardian_contact': forms.TextInput(
                attrs={
                    'placeholder': '보호자 연락처',
                    'class':'form-control',
                    }
                ),  
        }