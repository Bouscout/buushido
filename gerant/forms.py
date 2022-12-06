from gerant.models import onglet, affichage
from django import forms
from contenu.models import video, la_video
from django import forms
class onglet_form(forms.ModelForm) :
    class Meta:
        model = onglet
        fields = ['name']

class onglet_serie(forms.ModelForm):
    editeur = forms.NullBooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = onglet
        fields = ('name','onglet1',)
        widgets = {
        'onglet1': forms.CheckboxSelectMultiple()
        }
        labels = {
            'name': 'Nom de l\'onglet' ,
            'onglet1':'choisissez en minimum sept(7) et maximum 10 (dix)' ,
        }

class supprimer_onglet(forms.Form):
    supprimer= forms.NullBooleanField(widget=forms.HiddenInput, initial=True)

class supprimer_episode(forms.Form):
    supprimer= forms.NullBooleanField(widget=forms.HiddenInput, initial=True)
    ''' serie = forms.ModelMultipleChoiceField(
                       widget = forms.CheckboxSelectMultiple,
                       queryset = la_video.objects.all()
               )'''
        
class affichage_form(forms.ModelForm):
    class Meta:
        model = affichage
        fields = ('name', 'poster', 'to_display',)
        widgets = {
            'to_display' : forms.CheckboxSelectMultiple() ,
            'poster' : forms.CheckboxSelectMultiple() ,
        }

class formulaire_video(forms.ModelForm):
    couleur = forms.CharField(label='Couleur d\'ambiance', max_length=7,
    widget=forms.TextInput(attrs={'type': 'color'}))
    class Meta:
        model = video
        fields= ['name', 'posteur', 'genre_1', 'genre_2', 'genre_3','genre_4','couleur', 'tof_url', 'background_tof', 'description', 'lesstext', 'moretext',]

class formulaire_episode(forms.ModelForm):
    class Meta:
        model = la_video
        fields = ['episode', 'url', 'url2']