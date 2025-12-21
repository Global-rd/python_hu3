# Az oldal alap címe
BASE_URL = "https://quotes.toscrape.com/"

# Idézeteket tartalmazó dobozok útvonala
QUOTE_BOX = '/html/body/div[1]/div[2]/div[1]/div'
# Ezeket a dobozon belül keressük
QUOTE_TEXT = './span[1]'
AUTHOR_NAME = './span[2]/small'

# A főoldal jobb oldalán lévő top 10 kategória linkjei
TOP_TAG_XPATHS = [
    '/html/body/div[1]/div[2]/div[2]/span[1]/a',
    '/html/body/div[1]/div[2]/div[2]/span[2]/a',
    '/html/body/div[1]/div[2]/div[2]/span[3]/a',
    '/html/body/div[1]/div[2]/div[2]/span[4]/a',
    '/html/body/div[1]/div[2]/div[2]/span[5]/a',
    '/html/body/div[1]/div[2]/div[2]/span[6]/a',
    '/html/body/div[1]/div[2]/div[2]/span[7]/a',
    '/html/body/div[1]/div[2]/div[2]/span[8]/a',
    '/html/body/div[1]/div[2]/div[2]/span[9]/a',
    '/html/body/div[1]/div[2]/div[2]/span[10]/a'
]
# A lapozáshoz szükséges "Next" gomb
NEXT_PAGE_BUTTON = '//li[@class="next"]/a'