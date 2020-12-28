import csv
import requests
from bs4 import BeautifulSoup

file_list = []
with open("faceBook_pg.csv") as file_reader:
    file_read = csv.reader(file_reader, delimiter=',')
    count = 0
    for i in file_read:
        if count != 0:
            file_list.append(i[0])
        else:
            count+= 1

url = 'https://www.facebook.com/'

like_list = []
for link in file_list:
    url += link
    response = requests.get(url)
    data=response.content.decode()
    soup = BeautifulSoup(data, "html.parser")
    pg_likes = soup.select_one('span[class="_52id _50f5 _50f7"]').text[1:7]
    like_list.append(pg_likes)
    url = 'https://www.facebook.com/'

with open("faceBook_pg.csv","w") as file_write:
    file_writer = csv.writer(file_write, delimiter=',')
    file_writer.writerow(['FB_Page_Handles', 'Likes_Count'])
    for i in range(len(file_list)):
        file_writer.writerow([file_list[i], like_list[i]])





