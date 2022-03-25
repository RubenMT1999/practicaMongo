
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
    'posicion':'',
    'nombre':'',
    'descripcion':''
}


posicion =[]
nombre =[]
descripcion =[]


def todas_urls_dos():

    contador = 2

    for a in range(9):
        nueva_url = "https://www.sensacine.com/actores/top/mas-vistos/?page="+str(contador)
        total_urls.append(nueva_url)
        contador += 2



def cargar_url_dos():

    for a in total_urls:
        url= a
        req = requests.get(url)
        soup= BeautifulSoup(req.text, "html.parser")

        for i in soup.findAll("div", {"class": "label label-text label-sm label-primary-full label-ranking"}):
            i1= (i.get_text())
            posicion.append(int(i1))
            miDiccionarioDos['posicion']= posicion

        for o in soup.findAll("a", {"class": "meta-title-link"}):
            o1= o.text
            nombre.append(o1)
            miDiccionarioDos['nombre']= nombre

        for a in soup.findAll("div", {"class": "meta-body-item meta-body-info light"}):
            a1= a.text
            descripcion.append(a1)
            miDiccionarioDos['descripcion']= descripcion


todas_urls_dos()
cargar_url_dos()
print(descripcion
)
















