from bs4 import BeautifulSoup

with open("openstudio_results_report.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    
data = []
div = soup.find('div', {'id':'table_24'})
table = div.find('table')
rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    if len(cols) == 0:
        cols = row.find_all('th')
    cols = [ele.text.strip() for ele in cols]
    data.append(cols) # Get rid of empty values
    #data.append([ele for ele in cols if ele]) # Get rid of empty values

#rotated = list(zip(*data))[::-1]
new_list = []
for i in range(len(data[0])):
    if i == 0:
        continue
    new_list.append((data[0][i], data[1][i], data[2][i]))
print(new_list)
cooling_load_sum = 0
for i, elem  in enumerate(data[2], 0):
    if i == 0:
        continue
    cooling_load_sum += float(elem)
print(cooling_load_sum)
