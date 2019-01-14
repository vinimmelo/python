
def main():
    print_the_header()
    code = input('What zipcode do you want the weather for (97201)? ')
    url = get_html_from_web('us/or/portland')
    print(url)


def print_the_header():
    print('-----------------------------------')
    print('           WEATHER APP')
    print('-----------------------------------')


def get_html_from_web(city):
    url = 'https://www.wunderground.com/weather/{}'.format(city)
    return url


if __name__ == '__main__':
    main()
