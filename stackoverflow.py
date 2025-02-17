import requests #solicitudes HTTP
from bs4 import BeautifulSoup #analizar HTML

#User-Agent para que parezca que la solicitud es de un navegador real
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = 'https://stackoverflow.com/questions'
#obtener el html de la pagina
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
#encontrar el contenedor de las preguntas
questions = soup.find(id="questions")
#encontrar todas las preguntas
questions_list = questions.find_all("div", class_="s-post-summary")

for question in questions_list:
    #encontrar el contenedor con el titulo de la pregunta
    question_container = question.find("h3")
    question_text = question_container.text
    #busca el siguiente div con la descripcion de la pregunta
    text_description = question_container.find_next_sibling("div").text
    #limpiar el texto
    text_description = " ".join(text_description.split())

    print(question_text)
    print(text_description)
    print()