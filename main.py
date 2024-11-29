import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://dikoed.ru/catalog/krokodil/'
    response = requests.get(url)
    print(response.status_code)
    #print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    spoon = soup.find_all("div", class_='product-col list clearfix')
    print([i.text for i in spoon])

    with open('page.txt', 'a', encoding='utf-8') as file:
        file.write(''.join([i.text for i in spoon]))

    # soup = BeautifulSoup(response.text, 'html.parser')
    # part = soup.find('div', class_='content-text')


    # with open('page.txt', 'a', encoding='UTF-8') as file:
    #     file.write(part.text)

if __name__ == "__main__":
    main()