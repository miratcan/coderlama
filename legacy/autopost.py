import click
from selectorlib import Extractor
import requests
import json
from client import generate
from slugify import slugify


NO_AUTOMATION_ERR_MSG = \
    "we just need to make sure you're not a robot"

AI_SENTENCE_TEMPLATE = \
    "Give me a sentence with maximum 100 words to sell this product " \
    "to a software developer without mentioning product name: %s"

e = Extractor.from_yaml_file('selectors.yml')
with open('headers.json') as file:
    headers = json.load(file)


def scrape(url):
    r = requests.get(url, headers=headers)
    print(r.text)
    if r.status_code > 500:
        if NO_AUTOMATION_ERR_MSG in r.text:
            print("Page %s was blocked by Amazon. "
                  "Please try using better proxies\n", url)
        else:
            print("Page %s must have been blocked by Amazon "
                  "as the status code was %d", (url, r.status_code))
        return None
    data = e.extract(r.text)
    data['images'] = json.loads(data['images']) if data['images'] else {}
    data['largest_image_url'] = largest_image_url(data)
    data['price'] = ''.join(data['price'].splitlines())\
        .replace(' ', '')[1:] if data['price'] else None
    return data


def largest_image_url(data):
    if not data['images']:
        return

    def sorter(t):
        return t[1][0]

    ordered = sorted(data['images'], key=sorter, reverse=True)
    return ordered[0][0]


@click.command()
@click.argument('category')
@click.argument('url')
def main(category, url):
    print('------', category, url)
    data = scrape(url)
    import pprint
    pprint.pprint(data)
    print(generate('llama2', AI_SENTENCE_TEMPLATE % data['name']))


if __name__ == '__main__':
    main()
