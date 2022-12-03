
from cProfile import label
from email.policy import default
from django.db import models
from django.conf import settings
from colorfield.fields import ColorField

class video(models.Model):
    name = models.CharField('nom', max_length=100)
    #description= models.CharField(max_length= 200)
    tof_url = models.ImageField(upload_to='media/' , blank=True, null = True)
    background_tof = models.ImageField(upload_to='media/', blank=True, null=True)
    poster_tof = models.ImageField(upload_to='media/', blank=True, null=True)
    posteur = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,default=None, on_delete=models.SET_DEFAULT)
    description = models.TextField(null=True, blank=True)
    lesstext = models.TextField(blank=True, null=True)
    moretext = models.TextField(blank=True, null=True)
    couleur = ColorField(default='#f9f5f5')
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    genre_choix = (
        ('Action' , 'Action'),
        ('Aventure', 'Aventure'),
        ('Comedie', 'Comedie'),
        ('Drama', 'Drama'), 
        ('Horreur', 'Horreur'),
        ('Romance', 'Romance'),
        ('Sci-fi', 'Sci-fi'),
        ('Slice of life', 'Slice of life'),
        ('Mystere', 'Mystere'),
        ('Seinen', 'Seinen'),
        ('Isekai', 'Isekai'),
        ('Shonen', 'Shonen'),
        ('Sport', 'Sport'),
        ('Autres', 'Autres'),
        ('Film', 'Film'),
    )
    genre_1 = models.CharField('genre', max_length = 50, choices= genre_choix, default= "specifiez le genre d'animé s'il vous plait")
    genre_2 = models.CharField('genre', max_length = 50, choices= genre_choix, blank = True, null= True)
    genre_3 = models.CharField('genre', max_length = 50, choices= genre_choix, blank = True, null= True)
    genre_4 = models.CharField('genre', max_length = 50, choices= genre_choix, blank = True, null= True)
    genres = models.CharField(max_length = 200, blank = True, null = True)  

    
    def __str__(self):
        return str(self.name)
    def naming(self):
        self.genres = str(f'{self.genre_1} {self.genre_2} {self.genre_3} {self.genre_4}')

    def text(self):
        tr = str(self.description)
        mid = 0
        x = 200
        try:
            while True:
                if tr[x] == ' ':
                    mid = x
                    break
                x += 1
        except IndexError:
            return
        self.lesstext = tr[0:mid]
        self.moretext = tr[mid+1:]


    def search_value(self, index):
        return video.objects.filter(name__startswith = index)

    def framing_links(self):
        first = str(self.tof_url)
        second = str(self.background_tof)
        self.tof_url = 'https://drive.google.com/uc?export=view&id=' + first[32:65]
        self.background_tof = 'https://drive.google.com/uc?export=view&id=' + second[32:65]
        if self.poster_tof:
            third = str(self.poster_tof)
            self.poster_tof = 'https://drive.google.com/uc?export=view&id=' + third[32:65]
    

'''def fullscreen(self):
        transit = str(self.name)
        transit = transit[:-10] + ' allowfullscreen="allowfullscreen"' + transit[-10:]
        print(transit)
        return transit''' 

class la_video(models.Model):
    episode = models.PositiveIntegerField(verbose_name='===> Ecrivez le chiffre correspondant a l\'episode')
    saison = models.PositiveIntegerField('la saison correspondant a l\'episode',blank=True, null = True, default=1)
    nom = models.ForeignKey(video, on_delete=models.CASCADE, null=True)
    url = models.CharField(max_length = 200, blank=True, null = True)
    ref = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.nom) + 'S' + str(self.saison) + ' episode ' + str(self.episode)

    def get_ref(self):
        self.ref = int(str(self.saison)+str(self.episode))

    def fullscreen(self):
        obj = str(self.url)
        a=0
        b=0
        for i in range(len(obj[5:])) :
            if obj[i-3] != 's':
                continue
            if obj[i-3] + obj[i-2] + obj[i-1] + obj[i] == 'src=' :
                a = i + 2
                break
        for x in range(a+10, len(obj[5:])):
            if obj[x] == ' ' :
                b = x-1
                break
        if b > a :
            self.url = obj[a:b]
        
        
# Create your models here.
