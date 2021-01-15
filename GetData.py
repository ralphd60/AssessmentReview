import requests
import browser_cookie3

from bs4 import BeautifulSoup


def get_detail():
    print('hello')
    # https://gis.fultoncountyny.gov/imo/propdetail.aspx?swis=173089&printkey=08801600010360000000
    # create response object
    # r = requests.get(url + filename)
    #url = 'https://gis.fultoncountyny.gov'

    #https://github.com/borisbabic/browser_cookie3
    cj = browser_cookie3.chrome(domain_name='gis.fultoncountyny.gov')

    r = requests.get('https://gis.fultoncountyny.gov/imo/propdetail.aspx?printkey=08801600010060000000&swis=173089',cookies={"HasAgreedToDisclaimer":"True","ASP.NET_SessionId":"tkyli455ltwnc245gxkkli55"})


    print(cj)
    print(r.text)

    # create beautiful-soup object
    # soup = BeautifulSoup(r.content, "xml")
    #print(soup.prettify())

if __name__ == '__main__':
    get_detail()