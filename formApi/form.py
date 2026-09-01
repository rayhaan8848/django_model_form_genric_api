from django import forms

GENDER_FIELDS=(
    ('male','male'),
    ('female','female')
)
SUBJECT_FIELD=(
    ('django','django'),
    ('mern','mern'),
    ('dataSCI','dataSCI'),
)

class ContactForm(forms.Form):
    name=forms.CharField(label="Full Name", widget=forms.TextInput(attrs={'class':'form-control'})  ,initial='user',strip=True,min_length=2,)
    age=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    gender=forms.ChoiceField(choices=GENDER_FIELDS,widget=forms.RadioSelect)
    subject=forms.MultipleChoiceField(choices=SUBJECT_FIELD,widget=forms.CheckboxSelectMultiple)

