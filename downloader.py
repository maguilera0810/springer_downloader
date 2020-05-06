"""
Mauricio Aguilera
27 - Abril - 2020
"""

from bs4 import BeautifulSoup
import urllib3
import os


def ReadListado(file="links.txt"):
    file = open(file, "r")
    listado = ["http"+i.strip("\n").split("http")[1] for i in file if "http" in i]
    file.close()
    return listado

def link(url):
    def get_element(url):
        try:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            http = urllib3.PoolManager()
            r = http.request("GET", url)
            html = BeautifulSoup(r.data, "html.parser")
            return html.find_all("a")
        except Exception as e:
            print("Se ha producido un error: ", e)
    for e in get_element(url):
        res = e.get('href')
        if "/content/pdf/" in res:
            return f"https://link.springer.com{res}"
def main():
    lista = ReadListado(file="links.txt")
    for book in lista:
        res = link(book)
        print(f"Descargando......{res}\n")
        os.system(f"wget -c {res} -P pdfs")

main()
