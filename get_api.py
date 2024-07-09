import requests


def get_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    print(response.status_code)
    return response.content


if __name__ == "__main__":
    url_1 = "http://127.0.0.1:5000/mock/api/"
    url_2 = "https://rickandmortyapi.com/api/character/?page=19"

    print(get_api(url_2))
