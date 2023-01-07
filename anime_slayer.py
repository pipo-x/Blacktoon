import requests
basic_links = []
def get_basic(Link):
    global basic_links
    html = requests.get(Link).text.split()
    for i in html:
        if ('https://video.anime-slayer.com/episode' in i) and ('الحلقة' not in i):
            basic_links.append(i[6:-1])


def get_embed():
        global basic_links
        count = 1
        for i in basic_links:
            html = requests.get(i).text.split()

            for j in html:
                if ('uptostream.com/iframe' in j) or ('ok.ru/videoembed' in j) or ('moshahda.online/embed' in j) or ('dood.so' in j) or ('drive.google.com/file' in j) or ('4shared.com/web/embed' in j) or ('uqload.com/embed' in j) or ('mystream.to/watch' in j) or ('mp4upload.com/embed' in j) or ('vedpom.com/embed' in j) or ('mega.nz/embed' in j) or ('uptostream.com/iframe' in j) or ('ok.ru/videoembed' in j) or ('drive.google.com/file' in j):
                    linko = j.split('"')
                    print(linko[1])
            print('that was episode number ',count)
            count+=1

get_basic(input('enter the season link : '))
get_embed()