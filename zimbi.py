from bs4 import BeautifulSoup
import requests, time 
import os, subprocess
from pathlib import Path



def celeb():
    global filename

    u_i = input('Celeb Name(EX: Tom+Hanks): ')
    ash = ('http://www.zimbio.com/photos/'+u_i+'/browse?Page=')
    fNum = input("What page do you want to start on? : ")
    lNum = input("Last page? : ")
    for i in range(int(fNum), int(lNum)):
        with open('links.txt', 'a') as out:
            out.write(ash+str(i)+'\n')
            url = ash + str(i)
            r = requests.get(url)
            html = r.text
            soup = BeautifulSoup(html, 'html.parser')
            filename = 'CelebLinks.txt'
            with open(filename, 'a') as out:
                for url in soup.find_all('img'): 
                    out.write(url.get('src')+'\n')
                break
                    

import fileinput
def imgChanger():
    
    filename = "CelebLinks.txt"

    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace('s.jpg', 'l.jpg'), end='')


def img_download():
    filename = "CelebLinks.txt"
    path = input('Enter Directory Name: ')
    os.mkdir(path)
    with open(path):
        cmd = 'F:\wget\wget.exe -nc -i '+filename
        usef = os.system(cmd)





    
    


def main():

    print('Welcome to the Zimbio Image Ripper!')
    time.sleep(1)
    print('\n')
    u_i = input('1 - Celeb Image Links 2 - Change Image Size by link 3 - Download Images 4 - Exit '+'\n')
    while True:
        if u_i == "1":
            celeb()
            break
        elif u_i == "2":
            print('Changing links!')
            imgChanger()
            break
        elif u_i == "3":
            print('Downloading Images!')
            img_download()
            break
        elif u_i == "4":
            print('Bye!')
            break
        else:
            print("Huh?")
            break
    

main()
