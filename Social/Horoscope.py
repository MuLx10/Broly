import requests
from lxml import html

url = "http://www.ganeshaspeaks.com/horoscopes/daily-horoscope/" 
img_url = "https://images.ganeshaspeaks.com/images_gsv7/"

astroSign = ['aquarius',
             'cancer',
             'leo',
             'sagittarius',
             'capricorn',
             'aries',
             'taurus',
             'scorpio',
             'pisces',
             'libra',
             'virgo',
             'gemini']
             
def main():        
    horoscopes, imgs = [], []
    for sunsign in astroSign:
        response = requests.get(url+ sunsign)
        tree = html.fromstring(response.content)
        horoscope = str(tree.xpath("//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()"))
        horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("[\"", "").replace("\"]", "").replace("[\'", "").replace("\']", "")
        horoscope = horoscope.split('.')[0]+'.'
        img = img_url+sunsign.lower()+'200.png'
        
        horoscopes.append(horoscope)
        imgs.append(img)
        
    return imgs, horoscopes, [None]*len(astroSign)
    
    
if __name__ == "__main__":
    main()