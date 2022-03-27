
from bs4 import *
import requests



url_todas=["https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&ref_=adv_prv"]

miDiccionario= {
    'posiciones': '',
    'titulos': '',
    'anio':'',
    'valoraciones': '',
    'sinopsis':'',
    'imagenes':''

}

posiciones= []
titulos= []
valoraciones= []
imagenes= []
anio=[]
sinopsis=[]



def obtener_todas_url():

    var1 = 1

    for a in range(9):
        url_1 = "https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start="+str(var1)+"01&ref_=adv_nxt"
        url_todas.append(url_1)
        var1 += 1



def cargar_url():

    for a in url_todas:
        url= a
        req = requests.get(url)
        soup= BeautifulSoup(req.text, "html.parser")

        for i in soup.findAll("span", {"class": "lister-item-index unbold text-primary"}):
            i1= (i.get_text()).replace('.','').replace(',','')
            posiciones.append(int(i1))
            miDiccionario['posiciones']= posiciones



        for e in soup.findAll("h3", {"class": "lister-item-header"}):
            e1 = (e.find('a'))
            titulos.append(e1.get_text())
            miDiccionario['titulos']= titulos



        for m in soup.findAll("span", {"class": "lister-item-year text-muted unbold"}):
            m1= (m.get_text()).replace('(','').replace(')','').replace('I','')
            anio.append(m1)
            miDiccionario['anio']= anio



        for s in soup.findAll("div", {"class": "inline-block ratings-imdb-rating"}):
            s1 = (s.find_next('strong'))
            valoraciones.append(float((s1.get_text())))
            miDiccionario['valoraciones'] = valoraciones


        for v in soup.findAll("div", {"class": "ratings-bar"}):
            v1 = v.next_sibling.next_sibling.get_text().replace('\n','')
            sinopsis.append(v1)
            miDiccionario['sinopsis'] = sinopsis



        for u in soup.findAll("div", {"class": "lister-item-image float-left"}):
            u1= (u.find('a')).find('img').attrs["loadlate"]
            imagenes.append(u1)
            miDiccionario['imagenes'] =imagenes



#-------------------------------------------------------------------------------------------


total_urls = ["https://www.sensacine.com/actores/top/mas-vistos/"]


miDiccionarioDos ={
    'nombre':'',
    'descripcion':'',
    'imagen':'',
    'composiciones':''
}

nombre =[]
descripcion =[]
imagen = []

composiciones = {}

prueba=[]
prueba2=[]




def cargar_url_dos():



     url= "https://www.mobafire.com/teamfight-tactics/items-cheatsheet#items-cheatsheet"
     req = requests.get(url)
     soup= BeautifulSoup(req.text, "html.parser")

     for i in soup.findAll("div", {"class": "items-wrap__details__item__description"}):
            i1= i.find_next().get_text()
            nombre.append(i1)
            miDiccionarioDos['nombre']= nombre


     for i in soup.findAll("div", {"class": "items-wrap__details__item__description"}):
        i1 = i.find_next().find_next().get_text().replace('\n',' ')
        descripcion.append(i1)
        miDiccionarioDos['descripcion'] = descripcion

     for i in soup.findAll("div", {"class": "items-wrap__details__item__pic"}):
        i1 = str(i.find_next('img')).replace('<img src="','').replace('"/>','')
        imagen.append(i1)
        miDiccionarioDos['imagen'] = imagen


     url2 = "https://www.mobafire.com/teamfight-tactics/team-comps"
     req2 = requests.get(url2)
     soup = BeautifulSoup(req2.text, "html.parser")

     for i in soup.findAll("div", {"class": "champ-wrap"}):
        i1 = i.find_next().attrs['alt']
        prueba.append(i1)

     for i in soup.findAll("div", {"class": "tft-row__title"}):
        i1 = i.get_text().replace('\xa0','')
        prueba2.append(i1)



     composiciones[prueba2[0]] = prueba[0:9]
     composiciones[prueba2[1]] = prueba[18:25]
     composiciones[prueba2[2]] = prueba[34:42]
     composiciones[prueba2[3]] = prueba[50:58]
     composiciones[prueba2[4]] = prueba[68:75]
     composiciones[prueba2[5]] = prueba[84:92]
     composiciones[prueba2[6]] = prueba[101:109]
     composiciones[prueba2[7]] = prueba[118:127]
     composiciones[prueba2[8]] = prueba[130:139]

     miDiccionarioDos['composiciones']= composiciones



cargar_url_dos()
print(miDiccionarioDos
)
















