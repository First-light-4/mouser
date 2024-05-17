import requests

# Ваш API ключ от ScraperAPI
api_key = 'b416d72978bec5625fc6740c24c991f1'
url = 'https://www.digikey.com/en/products'  # URL веб-страницы, которую вы хотите скрапить

# Параметры запроса
params = {
    'api_key': api_key,
    'url': url,
    'render': 'true',  
    'timeout': '60000'  
}

try:
    # Отправка запроса
    response = requests.get('https://api.scraperapi.com/', params=params)

    # Проверка на успешный ответ
    if response.status_code == 200:
        # Вывод содержимого страницы
        with open(f"scraper.html", "w", encoding="utf-8") as file:
            file.write(response.text)
    else:
        print("Ошибка при запросе:", response.status_code)
except Exception as e:
    print("Произошла ошибка при выполнении запроса:", str(e))