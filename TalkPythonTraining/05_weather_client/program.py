import requests
import bs4



def main():
    print_the_header()
    html_page = get_html_from_web('us/or/portland')
    get_weather_from_html(html_page)
    # parse html
    # display the selected data


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
    cityCss = '.region-content-header-h1'
    weatherScaleCss = '.wu-unit-temperature.wu-label'
    weatherTempCss = '.wu-unit-temperature.wu-label'
    weatherConditionCss = '.condition-icon'
    soup = bs4.BeautifulSoup(html_page, 'html.parser')
    pass


if __name__ == '__main__':
    main()
