from bs4 import BeautifulSoup
import pandas as pd
import requests
import numpy as np
import datetime


def get_finviz_rsi():
    """Get dataframe of RSI data from scraped Finviz URL.

    Parameters
    ----------
    None

    Returns
    -------
    df : pandas.Dataframe
        data related to rsi values
    now : datetime object
        dt.datetime.now object
    """

    now = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    pandas_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    count = 1
    base_url = '''https://finviz.com/screener.ashx?v=111&f=an_recom_holdbetter,
                  geo_usa,sh_curvol_o1000,sh_opt_optionshort,sh_price_5to20,
                  ta_rsi_nos40&ft=3&o=-volume&r={}'''.format(count)
    html = requests.get(base_url)
    soup = BeautifulSoup(html.text, "lxml")
    count_str = str(soup.findAll(class_='count-text')[0])
    total = count_str.split('</b>')[-1].split()[0]

    ticks = []
    companies = []
    sectors = []
    industries = []
    country = []
    market_cap = []
    pe = []
    price = []
    change = []
    volume = []

    for i in range(1, int(total), 20):
        dyn_url = '''https://finviz.com/screener.ashx?v=111&f=an_recom_holdbetter,
                   geo_usa,sh_curvol_o1000,sh_opt_optionshort,sh_price_5to20,
                   ta_rsi_nos40&ft=3&o=-volume&r={}'''.format(i)
        html = requests.get(dyn_url)
        soup = BeautifulSoup(html.text, "lxml")
        main_div = soup.findAll('div', {'id': 'screener-content'})
        # main_div[0].findAll('table')
        raw_table = main_div[0].findAll('tr',
                                        attrs={'class':
                                               ['table-dark-row-cp',
                                                'table-light-row-cp']})
        for r in raw_table:
            ticks.append(r.findAll('a')[1].text)
            companies.append(r.findAll('a')[2].text)
            sectors.append(r.findAll('a')[3].text)
            industries.append(r.findAll('a')[4].text)
            country.append(r.findAll('a')[5].text)
            market_cap.append(r.findAll('a')[6].text)
            PE = r.findAll('a')[7].text
            if PE == '-':
                PE = np.nan
            pe.append(PE)
            price.append(r.findAll('a')[8].text)
            change.append(r.findAll('a')[9].text)
            volume.append(r.findAll('a')[10].text)

    ziplist = list(zip(ticks, companies, sectors,
                       industries, country, market_cap,
                       pe, price, change, volume))

    df = pd.DataFrame(ziplist, columns=['ticks', 'companies', 'sectors',
                                        'industries', 'country', 'market_cap',
                                        'pe', 'price', 'chg_prcnt', 'volume'])
    df['volume'] = df.volume.astype(str)
    df['volume'] = df.volume.str.replace(',', '')
    df['volume'] = df.volume.astype(int)
    df['change'] = df.chg_prcnt.str.replace('%', '').astype(float)
    df['price'] = df.price.astype(float)
    df['pe'] = df.pe.astype(float)
    df['datetime'] = pandas_now

    return df, now
