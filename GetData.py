import requests
import browser_cookie3
import re
from bs4 import BeautifulSoup


def get_detail(print_key):

    # https://gis.fultoncountyny.gov/imo/propdetail.aspx?swis=173089&printkey=08801600010360000000
    # create response object
    # r = requests.get(url + filename)
    url = 'https://gis.fultoncountyny.gov'
    # only need this to grab the cookies.  not able to pass it properly
    # but can keep trying
    #https://github.com/borisbabic/browser_cookie3
    #cj = browser_cookie3.chrome(domain_name= url)

    r = requests.get(url + '/imo/propdetail.aspx?printkey=' +  print_key + '&swis=173089',
                     cookies={"HasAgreedToDisclaimer":"True","ASP.NET_SessionId":"cnmv2g55mk04g4a5qzfacj55"})

    # create beautiful-soup object
    soup = BeautifulSoup(r.content, "lxml")

    find_div = soup.find("div", class_="centerColumn", id="pnlRTaxID")

    find_table = find_div.find("table", class_="reportTable singleBlack")
    table_rows = find_table.find_all('tr')

    # #THis pulls out just one piece of text data
    for i in table_rows:
        zone_data = i.find_all('span', id='lblZoningCode')
        for j in zone_data:
            return j.text
    # # This grabs the label text and the result text
    # for i in table_rows:
    #     table_data = i.find_all("td", class_="headerTD")
    #     table_data = table_data + i.find_all('span')
    #     #data becomes a irregular list
    #     data = [re.sub('\W+',' ', j.text) for j in table_data]
    #     for x in range(len(data)):
    #         print(data[x])




# if __name__ == '__main__':
#     get_detail()