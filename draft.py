import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://tl.rulate.ru/book/80509/2660617/ready_new'
    response = requests.get(url)
    print(response.status_code)

    soup = BeautifulSoup(response.text, 'html.parser')
    part = soup.find('div', class_='content-text')


    with open('page.txt', 'a', encoding='UTF-8') as file:
        file.write(part.text)

if __name__ == "__main__":
    main()