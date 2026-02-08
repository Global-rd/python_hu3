BASE_URL = "https://quotes.toscrape.com/"
QUOTE_CONTAINER_XPATH = '/html/body/div[1]/div[2]/div[1]/div'
QUOTE_TEXT_XPATH = './span[1]'
AUTHOR_PATH_XPATH = './span[2]/small'
QUOTE_TAGS_XPATH = './/div[@class="tags"]/a'
TOP_1='/html/body/div[1]/div[2]/div[2]/span[1]/a'
TOP_2='/html/body/div[1]/div[2]/div[2]/span[2]/a'
TOP_3='/html/body/div[1]/div[2]/div[2]/span[3]/a'
TOP_4='/html/body/div[1]/div[2]/div[2]/span[4]/a'
TOP_5='/html/body/div[1]/div[2]/div[2]/span[5]/a'
TOP_6='/html/body/div[1]/div[2]/div[2]/span[6]/a'
TOP_7='/html/body/div[1]/div[2]/div[2]/span[7]/a'
TOP_8='/html/body/div[1]/div[2]/div[2]/span[8]/a'
TOP_9='/html/body/div[1]/div[2]/div[2]/span[9]/a'
TOP_10='/html/body/div[1]/div[2]/div[2]/span[10]/a'
NEXT_BUTTON_PATH='//li[@class="next"]/a'

TOP_TAGS_LIST = [
    TOP_1, TOP_2, TOP_3, TOP_4, TOP_5, 
    TOP_6, TOP_7, TOP_8, TOP_9, TOP_10
]