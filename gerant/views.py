from django.shortcuts import render, get_object_or_404, redirect
from django.forms import formset_factory, modelformset_factory
from gerant.forms import onglet_serie , affichage_form, supprimer_onglet, formulaire_episode, formulaire_video, supprimer_episode
from .models import affichage, onglet
from contenu.models import video, la_video

# Create your views here.
def accueil_gerant(request):
    print('il est :', request.user.is_friend)
    if request.user.is_friend != True:
        return redirect('home')
    videos = video.objects.all()
    return render(request, 'gerant.html', {'videos':videos})


def create_onglet(request):
    if request.user.is_friend != True:
        return redirect('home')
    actual_onglet = onglet.objects.all()
    form = onglet_serie(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'onglet.html', {'form':form, 'onglets':actual_onglet})

def edit_onglet(request, id):
    if request.user.is_friend != True:
        return redirect('home')
    cas = get_object_or_404(onglet, pk=id)
    form = onglet_serie(request.POST or None, instance=cas)
    supprim = supprimer_onglet()
    if request.method == 'POST':
        if 'editeur' in request.POST:
            if form.is_valid():
                form.save()
                #form.save()
        if 'supprimer' in request.POST:
            supprim = supprimer_onglet(request.POST or None)
            if supprim.is_valid():
                print('allez ca degage')
                cas.delete()
                return redirect('onglet')
                
    return render(request, 'onglet.html', {'form':form , 'supprim':supprim})
    
def diffuser(request):
    if request.user.is_friend != True:
        return redirect('home')
    cas = get_object_or_404(onglet, pk=id)
    cas = get_object_or_404(affichage, pk=1)
    form = affichage_form(request.POST or None, instance=cas)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'onglet.html', {'form':form})

'''class MyArticleForm(formulaire_episode):
    def __init__(self, *args, user, **kwargs):
            self.user = user
            super().__init__(*args, **kwargs)'''

def ajouter_plusieurs_episode(request, id):
    if request.user.is_friend != True:
        return redirect('home')
    #formulaire = modelformset_factory(la_video, form=formulaire_episode, extra=5)
    form4 = None
    serie = get_object_or_404(video, pk=id)
    if len(serie.la_video_set.all()) > 0 :
        #form = formulaire(queryset=serie.la_video_set.all())
        form = None
        form4 = formulaire_episode(request.POST or None)
    else:
        formulaire = formset_factory(formulaire_episode, extra=12)
        form = formulaire(request.POST or None)
    if form4 :
        if form4.is_valid():
            vid= form4.save()
            vid.nom = serie
            vid.get_ref()
            vid.fullscreen()
            vid.save()
            return redirect('page_serie', id=id)
    if form :    
        if form.is_valid():
            for cas in form:
                if cas :
                    epi =cas.save()
                    epi.nom = serie
                    epi.get_ref()
                    epi.fullscreen()
                    epi.save()
            return redirect('page_serie', id=id)
    return render(request, 'postage.html', {'serie':serie, 'form':form, 'form4':form4 ,})

def poster_video(request):
    if request.user.is_friend != True:
        return redirect('home')
    form = formulaire_video(request.POST or None)
    if form.is_valid():
        vid= form.save()
        vid.posteur = request.user
        vid.naming()
        vid.text()
        vid.framing_links()
        vid.save()
        print(vid.id)
        return redirect('new_episodes', id=vid.id)
    return render(request, 'postage.html', {'form2':form})

def modifier_serie(request, id):
    if request.user.is_friend != True:
        return redirect('home')
    cas = get_object_or_404(video, pk=id)
    form = formulaire_video(request.POST or None, instance=cas)
    form2 = supprimer_episode()
    if form.is_valid():
        vid= form.save()
        vid.naming()
        vid.text()
        vid.save()
    if 'supprimer' in request.POST:
        form2 = supprimer_episode(request.POST)
        if form2.is_valid():
            cas.delete()
            return redirect('gerant_accueil')
        return redirect ('page_serie', id=id)
    return render(request, 'postage.html', {'form2':form, 'supprim':form2})

def supprim_episode(request, id):
    if request.user.is_friend != True:
        return redirect('home')
    cas = get_object_or_404(video, pk=id)
    videos = cas.la_video_set.all()
    form = supprimer_episode(request.POST or None)
    if request.method == 'POST':
        for elem in request.POST.getlist('episodes'):
            la_video.objects.get(id=int(elem)).delete()
    return render(request, 'postage.html', {'form3':form, 'video':videos})
    
    
