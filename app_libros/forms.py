from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from .models import *

class BookForm(forms.ModelForm):
    name = forms.CharField(label="Name", required=True)
    author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label="Authors List")
    genre = forms.ModelChoiceField(queryset=Genre.objects.all(), empty_label="Genres List")
    publisher = forms.ModelChoiceField(queryset=Publisher.objects.all(), empty_label="Publisher List")
    class Meta:
        model = Book
        fields = ('name','author','genre','publisher')


class GenreForm(forms.ModelForm):
    name = forms.CharField(label="Name", required=True)
    class Meta:
        model = Genre
        fields = ('name',)


class PublisherForm(forms.ModelForm):
    name = forms.CharField(label="Name", required=True)
    class Meta:
        model = Publisher
        fields = ('name',)


class AuthorForm(forms.ModelForm):
    name = forms.CharField(label="Name", required=True)
    date_of_birth= forms.DateField(
                           widget= forms.DateInput
                           (attrs={'placeholder':'MM/DD/YYYY'}))
    class Meta:
        model = Author
        fields = ('name','date_of_birth')