from multiprocessing import Pool
import bs4 as bs
import random
import requests
import string


def random_starting_url():
    starting = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(3))
    url = ''.join(['http://', starting, '.com'])
    return url


def handle_local_links(url, link):
    if link.startwith('/'):
        return ''.join([url, link])
    else:
        return link


def get_links(url):
    try:
        resp = requests.get(url)
        soup = bs.BeautifulSoup(resp.text, 'lxml')
        body = soup.body
        links = [link.get('href') for link in body.find_all('a')]
        links = [handle_local_links(url, link) for link in links]
        links = [str(link.encode('ascii')) for link in links]
        return links
    except TypeError as e:
        # print(e)
        print('Got a TypeError, probably got None that we tried to iterate over')
        return []
    except IndexError as e:
        # print(e)
        print('Got a IndexError, probably we did not find any useful links')
        return []
    except AttributeError as e:
        # print(e)
        print('Likely got None for links, so we are throwing this')
        return []
    except Exception as e:
        # print(str(e))
        # log this error
        return []


def main():
    how_many = 50
    pool = Pool(processes=how_many)
    parse_us = [random_starting_url() for _ in range(how_many)]
    data = pool.map(get_links, [link for link in parse_us])
    data = [url for url_list in data for url in url_list]
    pool.close()

    with open('urls.txt', 'w') as f:
        f.write(str(data))


if __name__ == '__main__':
    main()
