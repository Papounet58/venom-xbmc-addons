#-*- coding: utf-8 -*-
#Vstream https://github.com/Kodi-vStream/venom-xbmc-addons
# Votre nom ou pseudo

# a nettoyer VSlog et commentaire merci
return False
from resources.lib.gui.hoster import cHosterGui #systeme de recherche pour l'hote
from resources.lib.gui.gui import cGui #systeme d'affichage pour xbmc
from resources.lib.handler.inputParameterHandler import cInputParameterHandler #entree des parametres
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler #sortie des parametres
from resources.lib.handler.requestHandler import cRequestHandler #requete url
from resources.lib.parser import cParser #recherche de code
from resources.lib.comaddon import progress, VSlog #import du dialog progress
import base64

#from resources.lib.util import cUtil #outils pouvant etre utiles

#Si vous créez une source et la deposez dans le dossier "sites" elle sera directement visible sous xbmc

SITE_IDENTIFIER = 'ddlfr' #identifant (nom de votre fichier) remplacez les espaces et les . par _ AUCUN CARACTERE SPECIAL
SITE_NAME = 'DDLFR (beta)' #nom que xbmc affiche
SITE_DESC = 'films en streaming, streaming hd, streaming 720p, Films/séries, récent' #description courte de votre source

URL_MAIN = 'https://ddlfr.pw/' #url de votre source

#definis les url pour les catégories principale, ceci est automatique, si la definition est présente elle sera affichee.
#LA RECHERCHE GLOBAL N'UTILE PAS showSearch MAIS DIRECTEMENT LA FONCTION INSCRITE DANS LA VARIABLE URL_SEARCH_*
URL_SEARCH = (URL_MAIN + 'index.php?do=search&subaction=search&story=', 'showMovies')
#recherche global films
URL_SEARCH_MOVIES = (URL_MAIN + '?s=', 'showMovies')
#recherche global serie, manga
URL_SEARCH_SERIES = (URL_MAIN + '?s=', 'showMovies')
#recherche global divers
URL_SEARCH_MISC = (URL_MAIN + '?s=', 'showMovies')
#
FUNCTION_SEARCH = 'showMovies'

# menu films existant dans l'acceuil (Home)
MOVIE_NEWS = (URL_MAIN + 'films/', 'showMovies') #films (derniers ajouts = trie par date)
MOVIE_MOVIE = ('http://', 'load') #films (load source)
MOVIE_HD = (URL_MAIN + 'url', 'showMovies') #films HD
MOVIE_VIEWS = (URL_MAIN + 'url', 'showMovies') #films (les plus vus = populaire)
MOVIE_COMMENTS = (URL_MAIN + 'url', 'showMovies') #films (les plus commentés) (pas afficher sur HOME)
MOVIE_NOTES = (URL_MAIN + 'url', 'showMovies') #films (les mieux notés)
MOVIE_GENRES = (True, 'showGenres') #films genres
MOVIE_ANNEES = (True, 'showMovieYears') #films (par années)
#menu supplementaire non gerer par l'acceuil
MOVIE_VF = (URL_MAIN + 'url', 'showMovies') #films VF
MOVIE_VOSTFR = (URL_MAIN + 'films/vo-vostfr', 'showMovies') #films VOSTFR

# menu serie existant dans l'acceuil (Home)
SERIE_SERIES = ('http://', 'load') #séries (load source)
SERIE_NEWS = (URL_MAIN + 'series/', 'showMovies') #news.png ou series.png | séries (derniers ajouts = trie par date)
SERIE_VIEWS =  (URL_MAIN + 'url', 'showMovies') #views.png | series (les plus vus = populaire)
SERIE_HD = (URL_MAIN + 'series/', 'showMovies') #hd.png | séries HD
SERIE_GENRES = (True, 'showGenres') #séries genres
SERIE_ANNEES = (True, 'showSerieYears') #séries (par années)
SERIE_VFS = (URL_MAIN + 'series/', 'showMovies') #séries VF
SERIE_VOSTFRS = (URL_MAIN + 'series/vostfr/', 'showMovies') #séries Vostfr


ANIM_ANIMS = ('http://', 'load') #animés (load source)
ANIM_NEWS = (URL_MAIN + 'animes/', 'showMovies') #animés (derniers ajouts = trie par date)
ANIM_VIEWS =  (URL_MAIN + 'url', 'showMovies') #views.png #animés (les plus vus = populaire)
ANIM_GENRES = (True, 'showGenres') #anime genres
ANIM_ANNEES = (True, 'showAnimesYears') #anime (par années)
ANIM_VFS = (URL_MAIN + 'animes', 'showMovies') #animés VF
ANIM_VOSTFRS = (URL_MAIN + 'animes', 'showMovies') #animés VOSTFR
ANIM_ENFANTS = (URL_MAIN + 'animes', 'showMovies')

DOC_NEWS = (URL_MAIN + 'documentaires/', 'showMovies') #Documentaire
DOC_DOCS = ('http://', 'load') #Documentaire Load
DOC_GENRES = (True, 'showGenres') # Documentaires Genres

SPORT_SPORTS = (URL_MAIN + 'url', 'showMovies') #sport

NETS_NETS = ('http://' , 'load') #video du net load
NETS_NEWS =  (URL_MAIN + 'top-video.php', 'showMovies') #video du net (derniers ajouts = trie par date)
NETS_VIEWS =  (URL_MAIN + 'url', 'showMovies') #videos (les plus vus = populaire)
NETS_GENRES = (True, 'showGenres') #video du net (genre)

REPLAYTV_REPLAYTV = ('http://', 'load') #Replay load
REPLAYTV_NEWS = (URL_MAIN, 'showMovies') #Replay trie par date
REPLAYTV_GENRES = (True, 'showGenres') #Replay Genre

def load(): #fonction chargee automatiquement par l'addon l'index de votre navigation.
    oGui = cGui() #ouvre l'affichage

    oOutputParameterHandler = cOutputParameterHandler() #appelle la fonction pour sortir un parametre
    oOutputParameterHandler.addParameter('siteUrl', 'http://venom/') # sortie du parametres siteUrl n'oubliez pas la Majuscule
    oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'Recherche', 'search.png', oOutputParameterHandler)
    #Ajoute lien dossier (identifant, function a attendre, nom, icone, parametre de sortie)
    #Puisque nous ne voulons pas atteindre une url on peut mettre ce qu'on veut dans le parametre siteUrl

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_NEWS[1], 'Films (Derniers ajouts)', 'news.png', oOutputParameterHandler)
    #ici la function showMovies a besoin d'une url ici le racourci MOVIE_NEWS

    #oOutputParameterHandler = cOutputParameterHandler()
    #oOutputParameterHandler.addParameter('siteUrl', MOVIE_MOVIE[0])
    #oGui.addDir(SITE_IDENTIFIER, MOVIE_MOVIE[1], 'Films', 'films.png', oOutputParameterHandler)

    #oOutputParameterHandler = cOutputParameterHandler()
    #oOutputParameterHandler.addParameter('siteUrl', MOVIE_GENRES[0])
    #oGui.addDir(SITE_IDENTIFIER, MOVIE_GENRES[1], 'Films (Genres)', 'genres.png', oOutputParameterHandler)
    #showGenres n'a pas besoin d'une url pour cette methode

    #oOutputParameterHandler = cOutputParameterHandler()
    #oOutputParameterHandler.addParameter('siteUrl', MOVIE_ANNEES[0])
    #oGui.addDir(SITE_IDENTIFIER, MOVIE_ANNEES[1], 'Films (Par Années)', 'annees.png', oOutputParameterHandler)

    #oOutputParameterHandler = cOutputParameterHandler()
    #oOutputParameterHandler.addParameter('siteUrl', MOVIE_VIEWS[0])
    #oGui.addDir(SITE_IDENTIFIER, MOVIE_VIEWS[1], 'Films (Les plus vus)', 'views.png', oOutputParameterHandler)

    #oOutputParameterHandler = cOutputParameterHandler()
    #oOutputParameterHandler.addParameter('siteUrl', MOVIE_COMMENTS[0])
    #oGui.addDir(SITE_IDENTIFIER, MOVIE_COMMENTS[1], 'Films (Les plus commentés)', 'comments.png', oOutputParameterHandler)

    #oOutputParameterHandler = cOutputParameterHandler()
    #oOutputParameterHandler.addParameter('siteUrl', MOVIE_NOTES[0])
    #oGui.addDir(SITE_IDENTIFIER, MOVIE_NOTES[1], 'Films (Les mieux notés)', 'notes.png', oOutputParameterHandler)

    #oOutputParameterHandler = cOutputParameterHandler()
    #oOutputParameterHandler.addParameter('siteUrl', MOVIE_VF[0])
    #oGui.addDir(SITE_IDENTIFIER, MOVIE_VF[1], 'Films (VF)', 'vf.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', MOVIE_VOSTFR[0])
    oGui.addDir(SITE_IDENTIFIER, MOVIE_VOSTFR[1], 'Films (VOSTFR)', 'vostfr.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_NEWS[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_NEWS[1], 'Séries (Derniers ajouts)', 'news.png', oOutputParameterHandler)

    #oOutputParameterHandler = cOutputParameterHandler()
    #oOutputParameterHandler.addParameter('siteUrl', SERIE_SERIES[0])
    #oGui.addDir(SITE_IDENTIFIER, SERIE_SERIES[1], 'Séries', 'series.png', oOutputParameterHandler)

    #oOutputParameterHandler = cOutputParameterHandler()
    #oOutputParameterHandler.addParameter('siteUrl', SERIE_GENRES[0])
    #oGui.addDir(SITE_IDENTIFIER, SERIE_GENRES[1], 'Séries (Genres)', 'genres.png', oOutputParameterHandler)

    #oOutputParameterHandler = cOutputParameterHandler()
    #oOutputParameterHandler.addParameter('siteUrl', SERIE_ANNEES[0])
    #oGui.addDir(SITE_IDENTIFIER, SERIE_ANNEES[1], 'Séries (Par Années)', 'annees.png', oOutputParameterHandler)

    #oOutputParameterHandler = cOutputParameterHandler()
    #oOutputParameterHandler.addParameter('siteUrl', SERIE_VFS[0])
    #oGui.addDir(SITE_IDENTIFIER, SERIE_VFS[1], 'Séries (VF) ', 'vf.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', SERIE_VOSTFRS[0])
    oGui.addDir(SITE_IDENTIFIER, SERIE_VOSTFRS[1], 'Séries (VOSTFR)', 'vostfr.png', oOutputParameterHandler)

    oGui.setEndOfDirectory() #ferme l'affichage

def showSearch(): #fonction de recherche
    oGui = cGui()

    sSearchText = oGui.showKeyBoard() #appelle le clavier xbmc
    if (sSearchText != False):
        sUrl = URL_SEARCH[0] + sSearchText #modifie l'url de recherche
        showMovies(sUrl) #appelle la fonction qui pourra lire la page de resultats
        oGui.setEndOfDirectory()
        return


def showGenres(): #affiche les genres
    oGui = cGui()

    #juste a entrer les categories et les liens qui vont bien
    liste = []
    liste.append( ['Action', URL_MAIN + 'action/'] )
    liste.append( ['Animation', URL_MAIN + 'animation/'] )
    liste.append( ['Arts Martiaux', URL_MAIN + 'arts-martiaux/'] )
    liste.append( ['Aventure', URL_MAIN + 'aventure/'] )
    liste.append( ['Biopic', URL_MAIN + 'biopic/'] )
    liste.append( ['Comédie', URL_MAIN + 'comedie/'] )
    liste.append( ['Comédie Dramatique', URL_MAIN + 'comedie-dramatique/'] )
    liste.append( ['Comédie Musicale', URL_MAIN + 'comedie-musicale/'] )
    liste.append( ['Documentaire', URL_MAIN + 'documentaire/'] )
    liste.append( ['Drame', URL_MAIN + 'drame/'] )
    liste.append( ['Epouvante Horreur', URL_MAIN + 'epouvante-horreur/'] )
    liste.append( ['Erotique', URL_MAIN + 'erotique'] )
    liste.append( ['Espionnage', URL_MAIN + 'espionnage/'] )
    liste.append( ['Famille', URL_MAIN + 'famille/'] )
    liste.append( ['Fantastique', URL_MAIN + 'fantastique/'] )
    liste.append( ['Guerre', URL_MAIN + 'guerre/'] )
    liste.append( ['Historique', URL_MAIN + 'historique/'] )
    liste.append( ['Musical', URL_MAIN + 'musical/'] )
    liste.append( ['Policier', URL_MAIN + 'policier/'] )
    liste.append( ['Péplum', URL_MAIN + 'peplum/'] )
    liste.append( ['Romance', URL_MAIN + 'romance/'] )
    liste.append( ['Science Fiction', URL_MAIN + 'science-fiction/'] )
    liste.append( ['Spectacle', URL_MAIN + 'spectacle/'] )
    liste.append( ['Thriller', URL_MAIN + 'thriller/'] )
    liste.append( ['Western', URL_MAIN + 'western/'] )
    liste.append( ['Divers', URL_MAIN + 'divers/'] )

    for sTitle, sUrl in liste: #boucle

        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', sUrl) #sortie de l'url en parametre
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', sTitle, 'genres.png', oOutputParameterHandler)
        #ajouter un dossier vers la fonction showMovies avec le titre de chaque categorie.

    oGui.setEndOfDirectory()


def showMovieYears():#creer une liste inversée d'annees
    oGui = cGui()

    for i in reversed (xrange(1913, 2019)):
        Year = str(i)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', URL_MAIN + 'films/annee-' + Year)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', Year, 'annees.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showSerieYears():
    oGui = cGui()

    for i in reversed (xrange(1936, 2019)):
        Year = str(i)
        oOutputParameterHandler = cOutputParameterHandler()
        oOutputParameterHandler.addParameter('siteUrl', URL_MAIN + 'series/annee-' + Year)
        oGui.addDir(SITE_IDENTIFIER, 'showMovies', Year, 'annees.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def showMovies(sSearch = ''):
    oGui = cGui() #ouvre l'affichage
    if sSearch: #si une url et envoyer directement grace a la fonction showSearch
      sUrl = sSearch
    else:
        oInputParameterHandler = cInputParameterHandler()
        sUrl = oInputParameterHandler.getValue('siteUrl') #recupere l'url sortie en parametre

    oRequestHandler = cRequestHandler(sUrl) #envoye une requete a l'url
    sHtmlContent = oRequestHandler.request() #requete aussi
    #Vslog(sHtmlContent)
    #sHtmlContent = sHtmlContent.replace('<span class="likeThis">', '').replace('</span>', '')
    #la fonction replace est pratique pour supprimer un code du resultat

    sPattern = '<a class="short-poster img-box with-mask" href="([^"]+)"><img itemprop="image" src="([^"]+)" alt="([^"]+)"\/>'
    #pour faire simple recherche ce bout de code dans le code source de l'url
    #- "([^"]+)" je veux cette partie de code qui se trouve entre guillemets mais pas de guillemets dans la chaine
    #- .+? je ne veux pas cette partie et peux importe ceux qu'elle contient
    #- >(.+?)< je veux cette partie de code qui se trouve entre < et > mais il peut y avoir n'inporte quoi entre les 2.
    #- (https*://[^"]) je veux l'adresse qui commence par https ou http jusqu'au prochain guillemet.
    #
    #Pour tester vos Regex, vous pouvez utiliser le site https://regex101.com/ en mettant dans les modifiers "gmis"

    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    #le plus simple et de faire un  VSlog(str(aResult))
    #dans le fichier log d'xbmc vous pourrez voir un array de ce que recupere le script
    #et modifier sPattern si besoin
    VSlog(str(aResult)) #Commenter ou supprimer cette ligne une fois fini

    #affiche une information si aucun resulat
    if (aResult[0] == False):
        oGui.addText(SITE_IDENTIFIER)

    if (aResult[0] == True):
        total = len(aResult[1])
        #dialog barre de progression
        progress_ = progress().VScreate(SITE_NAME)

        for aEntry in aResult[1]:
            progress_.VSupdate(progress_, total) #dialog update
            if progress_.iscanceled():
                break

            #L'array affiche vos info dans l'orde de sPattern en commencant a 0, attention dans ce cas la on recupere 6 information
            #Mais selon votre regex il ne peut y en avoir que 2 ou 3.
            sTitle = aEntry[2]
            sUrl2 = aEntry[0]
            sThumb = aEntry[1]
            sLang = ''
            sQual = ''
            sHoster = ''
            sDesc = ''
          
            sTitle = sTitle.replace('FRENCH', '')
            sTitle = sTitle.replace('BDRIP', '')
            sTitle = sTitle.replace('WEBRIP', '')
            sTitle = sTitle.replace('HDRIP', '')
            sTitle = sTitle.replace('DVDRIP', '')
            sTitle = sTitle.replace('HDTV', '')
            sTitle = sTitle.replace('720p', '')
            sTitle = sTitle.replace('1080p', '')
            

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl2) #sortie de l'url
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle) #sortie du titre
            oOutputParameterHandler.addParameter('sThumb', sThumb) #sortie du poster

            if '/series' in sUrl:
                #oGui.addTV(SITE_IDENTIFIER, 'ShowSerieSaisonEpisodes', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
                oGui.addTV(SITE_IDENTIFIER, 'showLinks', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
                #addTV pour sortir les series tv (identifiant, function, titre, icon, poster, description, sortie parametre)
            else:
                oGui.addMovie(SITE_IDENTIFIER, 'showLinks', sTitle, '', sThumb, sDesc, oOutputParameterHandler)
                #addMovies pour sortir les films (identifiant, function, titre, icon, poster, description, sortie parametre)

            #il existe aussi addMisc(identifiant, function, titre, icon, poster, description, sortie parametre)
            #la difference et pour les metadonner serie, films ou sans

        progress_.VSclose(progress_) #fin du dialog

        sNextPage = __checkForNextPage(sHtmlContent) #cherche la page suivante
        if (sNextPage != False):
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sNextPage)
            oGui.addNext(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Next >>>[/COLOR]', oOutputParameterHandler)
            #Ajoute une entree pour le lien Next | pas de addMisc pas de poster et de description inutile donc

    if not sSearch:
        oGui.setEndOfDirectory() #ferme l'affichage


def __checkForNextPage(sHtmlContent): #cherche la page suivante
    oParser = cParser()
    sPattern = '<span class="pnext"><a href="([^"]+)">'
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        return aResult[1][0]

    return False

def showLinks():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sThumb = oInputParameterHandler.getValue('sThumb')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()
    #VSlog(sHtmlContent)
    oParser = cParser()

    sDesc = ''

    sPattern = 'data-re_idnews="([^"]+)" data-re_xfn="video" data-re_page="([^"]+)">([^<]+)</div>'
    
    aResult = oParser.parse(sHtmlContent, sPattern)
    VSlog(aResult)
    
    
    if (aResult[0] == False):
        oGui.addText(SITE_IDENTIFIER)

    if (aResult[0] == True):
        total = len(aResult[1])

        progress_ = progress().VScreate(SITE_NAME)

        for aEntry in aResult[1]:
            VSlog(aEntry)
            sId = aEntry[0]
            sPage = aEntry[1]
            sTitle = sMovieTitle + ' ('+aEntry[2]+')'

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('sId', sId)
            oOutputParameterHandler.addParameter('sPage', sPage)
            oOutputParameterHandler.addParameter('sMovieTitle', sMovieTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)
            if (sPage != '0'):
                oGui.addLink(SITE_IDENTIFIER, 'showHosters', sTitle, sThumb, sDesc, oOutputParameterHandler)
                
        progress_.VSclose(progress_)

    oGui.setEndOfDirectory()
     
def showHosters():
    oGui = cGui()
    VSlog('showHosters')
    oParser = cParser()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')
    sId = oInputParameterHandler.getValue('sId')
    sPage = oInputParameterHandler.getValue('sPage')

    sUrl2 = URL_MAIN + 'engine/ajax/re_video_part.php'
    VSlog(sUrl2)
    VSlog(sId)
    VSlog(sUrl)
    oRequestHandler = cRequestHandler(sUrl2)
    oRequestHandler.setRequestType(1)
    oRequestHandler.addHeaderEntry('User-Agent',"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0")
    oRequestHandler.addHeaderEntry('Content-Type','application/x-www-form-urlencoded; charset=UTF-8')
    oRequestHandler.addHeaderEntry('Origin',URL_MAIN)
    oRequestHandler.addHeaderEntry('Referer',sUrl)
    oRequestHandler.addParameters('block', 'video')
    oRequestHandler.addParameters('page', sPage)
    oRequestHandler.addParameters('id', sId)
    sHtmlContent = oRequestHandler.request()
    VSlog(sHtmlContent)

    sHosterUrl = sHtmlContent
    VSlog(sHosterUrl)
    
    oHoster = cHosterGui().checkHoster(sHosterUrl)
    VSlog(oHoster)
    if (oHoster != False):
        sHosterUrl = sHosterUrl
        oHoster.setDisplayName(sMovieTitle)
        oHoster.setFileName(sMovieTitle)
        cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    oGui.setEndOfDirectory() #fin

#Pour les series, il y a generalement une etape en plus pour la selection des episodes ou saisons.
def ShowSerieSaisonEpisodes():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sThumb = oInputParameterHandler.getValue('sThumb')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = '?????????????????????'

    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)

    if (aResult[0] == True):
        total = len(aResult[1])

        progress_ = progress().VScreate(SITE_NAME)

        for aEntry in aResult[1]:
            progress_.VSupdate(progress_, total)
            if progress_.iscanceled():
                break

            sTitle = sMovieTitle + aEntry[0]
            sUrl2 = aEntry[1]

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl2)
            oOutputParameterHandler.addParameter('sMovieTitle', sTitle)
            oOutputParameterHandler.addParameter('sThumb', sThumb)

            oGui.addTV(SITE_IDENTIFIER, 'seriesHosters', sTitle, '', sThumb, '', oOutputParameterHandler)

        progress_.VSclose(progress_)

    oGui.setEndOfDirectory()

def seriesHosters(): #cherche les episodes de series
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumb = oInputParameterHandler.getValue('sThumb')

    oRequestHandler = cRequestHandler(sUrl)
    sHtmlContent = oRequestHandler.request()

    sPattern = '<dd><a href="([^<]+)" class="zoombox.+?" title="(.+?)"><button class="btn">.+?</button></a></dd>'
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern)
    if (aResult[0] == True):
        for aEntry in aResult[1]:

            sHosterUrl = aEntry[0]
            oHoster = cHosterGui().checkHoster(sHosterUrl)
            if (oHoster != False):
                oHoster.setDisplayName(aEntry[1])
                oHoster.setFileName(aEntry[1])
                cHosterGui().showHoster(oGui, oHoster, sHosterUrl, sThumb)

    oGui.setEndOfDirectory()

#Voila c'est un peux brouillon mais ça devrait aider un peu, n'hesitez pas a poser vos questions et meme a partager vos sources.
