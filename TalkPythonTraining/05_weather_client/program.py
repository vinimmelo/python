import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport', 'cond temp location')


def main():
    print_the_header()
    currently_city = 'us/or/portland'
    html_page = get_html_from_web(currently_city)
    report = get_weather_from_html(html_page)
    print(f'The temp in {report.location} is {report.cond} and {report.temp}ºF')


def print_the_header():
    print('-----------------------------------')
    print('           WEATHER APP')
    print('-----------------------------------')


def get_html_from_web(city):
    url = 'https://www.wunderground.com/weather/{}'.format(city)
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return ''


def get_weather_from_html(html_page):
    weatherScaleCss = '.wu-value-to'
    weatherConditionCss = '.condition-icon'
    soup = bs4.BeautifulSoup(html_page, 'html.parser')
    location = soup.h1.get_text()
    condition = soup.select(weatherConditionCss)[0].get_text()
    temp = soup.select(weatherScaleCss)[0].get_text()
    location = cleanup_text(location)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    report = WeatherReport(condition, temp, location)
    return report


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == '__main__':
    main()
