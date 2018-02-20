from django import forms
from .models import Book
import datetime

YEAR_CHOICES = tuple([2000+i for i in range(22)])

CHOICES=[('select1','select 1'),
         ('select2','select 2')]

TRUEFALSE = (
    ('True','True'),
    ('False', 'False'),
)

class QueryForm(forms.Form):

    publish_date_before = forms.DateField(
        label='',
        required=False,
        # initial = datetime.datetime.now(),
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'id':'datepicker1', 
                'placeholder':'published before'
            }))

    publish_date_after = forms.DateField(
        label='',
        required=False,
        # initial = datetime.datetime.now(),
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'id':'datepicker2', 
                'placeholder':'published after'
            }))

    keywords = forms.CharField(
        required=False,
        label='',
        widget=forms.TextInput(
            
            attrs={
                'class':'form-control',
                'placeholder':'space-separated words matching title, synopsis, website or tags'
            }
        )
    )



    status = forms.BooleanField(
        required=False,

        # widget=forms.RadioSelect(
        #     attrs={
        #         'class':'form-control'
        #     }
        #     )
        )

    # status = forms.ChoiceField(
    #     choices=TRUEFALSE,
    #     required=False,
    #     widget=forms.RadioSelect(
    #         attrs={}
    #     ))
    
    class Meta:
        field=[
            # 'boolean',
            'status',
        ]



class BookForm(forms.ModelForm):

    title = forms.CharField(
        required=True, 
        label = "",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'id':'id_title',
                'placeholder': "book title",
                'label':''
            }))


    publish_date = forms.DateField(
        label='',
        # initial = datetime.datetime.now(),
        widget = forms.TextInput(
            attrs={
                'class': 'form-control',
                'id':'datepicker', 
                'placeholder':'publish date'
            }))

    synopsis = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'id':'id_content',
                'rows':5,
                'placeholder': "book synopsis",
                'label':''
            }))

    pages = forms.IntegerField(
        label = "", 
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'number of pages',
                'type':'number',
                'id':'id_pages'
            }
        )
    )


    lon = forms.CharField(
        label="", 
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'id':'id_lon',
                'placeholder': "longitude",
                'type':'text', 
            }
        )
    )

    lat = forms.CharField(
        label="", 
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'id':'id_lat',
                'placeholder': "latitude",
                'type':'text', 
            }
        )
    )

    class Meta:
        model = Book
        fields = [
            'title',
            'publish_date',
            'synopsis',
            'pages',
            'lon',
            'lat',
        ]