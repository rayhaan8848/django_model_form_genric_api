from django import forms
from .models import Detail

GENDER_FIELDS=(
    ('male','male'),
    ('female','female')
)
SUBJECT_FIELD=(
    ('django','django'),
    ('mern','mern'),
    ('dataSCI','dataSCI'),
)

class DetailForm(forms.ModelForm):
    class  Meta:
        model=Detail
        fields='__all__'
        widgets = {
            'gender':forms.RadioSelect(choices=GENDER_FIELDS),
            'subject':forms.CheckboxSelectMultiple(choices=SUBJECT_FIELD)
        }
