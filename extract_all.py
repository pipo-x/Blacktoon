from os import name
import requests
all_links = []
names = []
page_links_w_name = []
episodes_link = []
def get_all_links(main_link,num):
    global all_links
    for i in range(1,num):
        main_link = main_link.replace('$',str(i))
        all_links.append(main_link)

def first_extraction(link):
    global page_links_w_name
    html = requests.get(link).text.split()
    for i in html:
        if ('https://video.anime-slayer.com/anime/' in i) and ('AI' not in i) and ('>' not in i):
            page_links_w_name.append(i[6:-1])
            names.append(i[43:])

def second_extraction(link):
    global episodes_link
    html = requests.get(link).text.split()
    for i in html:
        if 'https://video.anime-slayer.com/episode/' in i:
            episodes_link.append(i[6:-1])

def third_extraction(link,file_name):
    global episodes_link
    new_file = open(file_name,'w')
    global episodes_link
    count = 1
    for i in episodes_link:
        requests.get(link).text.split()
        for j in html:
            if ('cdn4.vid4up.xyz/embedvideo' in j)or ('uptostream.com/iframe' in j) or ('ok.ru/videoembed' in j) or ('moshahda.online/embed' in j) or ('dood.so' in j) or ('drive.google.com/file' in j) or ('4shared.com/web/embed' in j) or ('uqload.com/embed' in j) or ('mystream.to/watch' in j) or ('mp4upload.com/embed' in j) or ('vedpom.com/embed' in j) or ('mega.nz/embed' in j) or ('uptostream.com/iframe' in j) or ('ok.ru/videoembed' in j) or ('drive.google.com/file' in j):
                linko = j.split('"')
                new_file.write(linko[1])
        new_file.write('that was eps number ', count)
        count +=1
    file_name.close()

get_all_links(input("enter the main link with $ instead of the number : "),int(input("how many page : ")))
for i in all_links:
    first_extraction(i)

for i in page_links_w_name:
    second_extraction(i)
for j in names:
    for i in episodes_link:
        third_extraction(i,str(j)+'.txt')
