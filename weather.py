import requests
import os

def get_weather_data(place, api_key=None):
    """
    Получает данные о погоде для заданного места.

    Args:
        place: Название места (город, страна).
        api_key: API ключ для OpenWeatherMap.
            Если не указан, то используется ключ из переменной окружения 'OWM_API_KEY'.

    Returns:
        Словарь с данными о погоде, или None, если произошла ошибка.
    """
    if api_key is None:
        api_key = os.getenv('OWM_API_KEY')

    if not place:
        return None

    url = f'https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        name = data['name']
        coord = data['coord']
        country = data['sys']['country']
        feels_like = data['main']['feels_like']
        timezone_offset = data['timezone'] / 3600
        timezone = f"UTC+{timezone_offset}" if timezone_offset >= 0 else f"UTC{timezone_offset}"

        return {
            "name": name,
            "coord": coord,
            "country": country,
            "feels_like": feels_like,
            "timezone": timezone
        }
    else:
        print(f"Ошибка запроса: {response.status_code}")
        return None



