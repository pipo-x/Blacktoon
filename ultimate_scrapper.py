import requests
from bs4 import BeautifulSoup

all_pg_lnks = []
series_links = []
episodes_links = []
ep_semi_embed = []
embed = []


def page_gn(page_typo, pg_cnt_str, pg_cnt_end):
    for cnt in range(pg_cnt_str, pg_cnt_end + 1):
        all_pg_lnks.append(page_typo.replace('$', str(cnt)))


def gat_serie_name(pg_lnk, what_to_search, what_class):
    html = requests.get(pg_lnk)
    data = html.content
    soup = BeautifulSoup(data, 'html.parser')
    name = soup.find(str(what_to_search), {'class': str(what_class)}).get_text()
    return str(name)


def link_selector(pg_link, what_list, what_to_search, what_class, is_a, is_href):
    html = requests.get(pg_link)
    data = html.content

    soup = BeautifulSoup(data, 'html.parser')
    for i in soup.find_all(str(what_to_search), {'class': str(what_class)}):
        link = i.find(str(is_a))
        if link is None:
            continue
        to_append = link[is_href]
        if to_append not in what_list:
            what_list.append(to_append)


def excute():
    page_gn(input('enter links typo : '), int(input('enter how many pages to scrap the beginning : ')),
            int(input('enter the end : ')))
    for pg_lnk in all_pg_lnks:
        link_selector(pg_lnk, series_links, 'article', 'TPost C', 'a', 'href')
        for serie_lnk in series_links:
            file = open(str(gat_serie_name(serie_lnk, 'h1', 'Title') + '.txt'), 'a')

            link_selector(serie_lnk, episodes_links, 'td', 'MvTbTtl', 'a', 'href')
            count = 1
            for ep_lnk in episodes_links:

                link_selector(ep_lnk, ep_semi_embed, 'div', 'TPlayerTb Current', 'iframe', 'src')
                i = ep_semi_embed[0]
                for rng in range(20):
                    link = i[:i.index("=") + 1] + str(rng) + i[i.index('=') + 2:]
                    link_selector(link, embed, 'div', 'Video', 'iframe', 'src')
                    try:
                        file.write(embed[0] + '\n')
                    except:
                        file.write('there was a fckng error ...' + '\n')
                    embed.clear()
                file.write('that was ep number ' + str(count) + '\n')
                count += 1

            ep_semi_embed.clear()
            episodes_links.clear()
            file.close()


excute()