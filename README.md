# rsiFinvizScrape
Python3 scraping function for fetching RSI related data from Finviz

#### To load:
- git clone
- cd into scrapeFinvizRsi
- pip install . (the '.' is important); or pip3 install . (if not aliased).
  - This will install:
    - pandas
    - numpy
    - BeautifulSoup4
#### Use
- `from scrapeFinvizRsi import get_finviz_rsi`
- `df, now = get_finviz_rsi()`

This will give you a dataframe and datetime object `now`. The stocks listed are related to a RSI 'Not oversold' > 40 condition from Finviz's analytics page. I've tweaked the URL a bit in the function. Feel free to edit and drop me line if you want to discuss alternatives or issues. Base url: https://finviz.com/screener.ashx?v=111&f=an_recom_holdbetter,geo_usa,sh_curvol_o1000,sh_opt_optionshort,sh_price_5to20,ta_rsi_nos40&ft=3&o=-volume
