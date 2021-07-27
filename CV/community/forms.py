from django import forms
from django.forms import TextInput, Textarea
from django.utils.safestring import mark_safe

from community.models import *

strength_choices = (
    ('s_ch1', '비판적사고'),
    ('s_ch2', '전문성'),
    ('s_ch3', '도전정신'),
    ('s_ch4', '성취지향'),
    ('s_ch5', '의사소통'),
    ('s_ch6', '주도성'),
    ('s_ch7', '문제해결'),
    ('s_ch8', '치밀성'),
)


# ModelForm(모델 폼)
class PostForm(forms.ModelForm):
    strength = forms.ChoiceField(label='강점', choices=strength_choices, widget=forms.RadioSelect())

    class Meta:
        model = CV
        fields = ['job', 'letter', 'strength']  # '__all__'
        widgets = {
            'letter': Textarea(attrs={
                'class': "letter",
                'cols': "100",
                'rows': "30",
                'placeholder': '자기소개서를 입력하세요.',
            }),
        }

        # 클래스 지정 -> 실행안됨.
        # def __init__(self, *args, **kwargs):
        #     super(PostForm, self).__init__(*args, **kwargs)
        #     # self.fields['letter'].required = False
        #     self.fields['job'].widget.attrs.update({'class': 'job'})
        #     self.fields['strength'].widget.attrs.update({'class': 'strength'})
