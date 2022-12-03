from django.shortcuts import redirect, render, get_object_or_404
from gerant.models import affichage, calendrier
from contenu.models import video
from django.forms import formset_factory

def maison(request):
    return redirect('redirect', genre='home')

def page_serie(request, id):
    serie = get_object_or_404(video, pk=id)
    episode = serie.la_video_set.all() or None
    saison = [x for x in range(1, (episode.latest('saison').saison)+1)]
    return render(request, 'page_serie.html', {'serie':serie , 'episodes':episode,  'saison':saison })

def page_epi(request, id, il):
    serie = get_object_or_404(video, pk=id)
    episode = serie.la_video_set.all() or None
    end = 0
    if il == episode[(len(episode))-1].ref :
        end = 2
    elif il == episode[0].ref :
        end = 3
    return render(request, 'page_episode.html', {'serie':serie , 'episodes':episode, 'id':il, 'end':end})

def categorie(request, genre):
    videos = video.objects.all()
    if genre == 'mylist':
        choix = 'Ma liste'
        videos = request.user.anime_prefere.all()
    else :
        choix = genre
        videos = video.objects.filter(genres__contains =str(choix))
    return render(request, 'categorie.html', {'videos':videos, 'nom':choix})


def accueil(request):
    affiche = affichage.objects.all()[0]
    return render(request, 'page accueil.html', {'affiche':affiche, 'user':request.user})

def rediriger_accueil(request, genre):
    if genre == 'home' :
        return redirect('home')
    return redirect('genre', genre)

def rediriger_serie(request, id):
    print('on est la')
    return redirect('page_serie', id=id)


def redirect_epi(request, id, il, syntax):
    if syntax == 'previous':
        return redirect('page_episode', id=id, il=il-1)
    elif syntax == 'next':
        return redirect('page_episode', id=id, il=il+1)
    elif syntax == 'accueil':
        return redirect('page_serie', id)
    else :
        return redirect('page_episode', id=id, il=int(syntax))

liston = video()
dico = {}
indice = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for x in indice:
    dico[x] = liston.search_value(x.upper()) 

def voir_tout(request):
    global dico
    return render(request, 'voir_tout.html', {'indice':indice, 'dico':dico,})

def agenda(request):
    agenda = calendrier.objects.all()
    return render(request, 'agenda.html', {'agenda':agenda})
        


# Create your views here.
