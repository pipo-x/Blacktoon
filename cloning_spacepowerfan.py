import requests
Links = []

link = input('enter the cimaroom link : ')
html = requests.get(link).text.split()
for i in html:
    if 'https://filmoox.com/?p=' in i :
        Links.append(i[6:-1])
cont = 1
for j in Links:

    html1 = requests.get(j).text.split()
    for n in html1:
        if ('https://drive.google.com' in n) or ('https://mega.nz/' in n) or ('https://ok.ru/' in n) or ('http://bit.ly/' in n):
            print(n[6:-1])
    print('that was ep number' , cont)
    cont+=1
