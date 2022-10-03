
------->Finding Elements by class

s = prettyHtmlContent.find('div', class_='Class Name')
content = s.find_all('p')
print(content)


------->Finding by ID

s = prettyHtmlContent.find('div', id= '<ID name>')


------->Removing the tags from the content of the page and getting the text only

s = prettyHtmlContent.find('div', class_='<class name>')
lines = s.find_all('p')
for line in lines:
    print(line.text)



------->Getting the Links

for link in prettyHtmlContent.find_all('a'):
    print(link.get('href'))



------->Extracting The Image
images_list = []
images = prettyHtmlContent.select('img')
for image in images:
    src = image.get('src')
    alt = image.get('alt')
    images_list.append({"src": src, "alt": alt})
     
for image in images_list:
    print(image)



--------->Saving data to CSV
   In this case we need to import CSV  ->import CSV
prettyHtmlContent = bs(req.text, 'html.parser')
titles = prettyHtmlContent.find_all('div', attrs={'class', 'head'})
titles_list = [] 
count = 1
for title in titles:
    d = {}
    d['Title Number'] = f'Title {count}'
    d['Title Name'] = title.text
    count += 1
    titles_list.append(d)
 
filename = 'titles.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['Title Number','Title Name'])
    w.writeheader()
     
    w.writerows(titles_list)