import urllib
from wordcloud import WordCloud
pilv = WordCloud().generate(urllib.request.urlopen("https://raw.githubusercontent.com/astridhelvik/dh2017/master/aisakell").read().decode("utf8"))
pilt = pilv.to_image()
pilt.save('pilt4.png')