#coding=utf-8
import hashlib    
import urllib,urllib2
import json
import os
import requests
from colors import red, green, blue
from clint.textui import progress
import webbrowser
import zipfile

ver = "1.2"

m = hashlib.md5()

def checker( file, md5, download_url ):
    if os.path.exists(file) is False:
        print red('巴打我搵唔到' + file + '喎，不如幫你Download過個新既好無？').decode("utf-8")
        in1 = raw_input("Enter (y)es or (n)o: ") 
        if in1 == "yes" or in1 == "y" or in1 == "": 
            download( file, download_url)
            return
        elif in1 == "no" or in1 == "n": 
            return
        
    m = hashlib.md5()
    fd = open(file,"rb")
    x = fd.read()
    fd.close()
    m.update(x)
    md5_returned = m.hexdigest()
    if md5_returned != md5:
        print ("搵到更新！依家即刻幫你更新" + file + "\n").decode("utf-8")
        download( file, download_url)
    else:
        print ("搵唔到" + file + "有更新喎巴打！如果入唔到既可能係樓豬未Upload最新既File上Server，請盡情咁屌佢老母啦不過屌完都係要等架啦\n").decode("utf-8")

def download( file, download_url ):
    r = requests.get(download_url, stream=True)
    path = file
    with open(path, 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
            if chunk:
                f.write(chunk)
                f.flush()
    return

r=requests.get("https://raw.githubusercontent.com/l2003201/WL-Updater/master/update.json")
r.json()
update = json.loads(r.text, encoding="utf-8")


if update["version"] != ver:
    print red('喂喂巴打有更新喎不如更新左先啦～\n').decode("utf-8")
    webbrowser.open('https://github.com/l2003201/WL-Updater/raw/master/updater.exe')
    exit()

if os.path.exists('wlviptw.exe') is False:
    print ('喂巴打你好似未down飄流傭兵喎，不如我幫Donwload之後解壓係你依家個目錄到順手更新到最新啦好無？(' + os.getcwd() + ')').decode("utf-8")
    in1 = raw_input("Enter (y)es or (n)o: ") 
    if in1 == "yes" or in1 == "y" or in1 == "": 
        download( 'wl.zip', update["WL_download_url"])
        zip_ref = zipfile.ZipFile('wl.zip', 'r')
        zip_ref.extractall(os.getcwd())
        zip_ref.close()
        os.remove('wl.zip')


checker( "V_hk.Dat", update["V_hk.Dat"]["latest_md5"], update["V_hk.Dat"]["download_url"])
checker( "game.dat", update["game.dat"]["latest_md5"], update["game.dat"]["download_url"])
checker( "game_hk.dat", update["game_hk.dat"]["latest_md5"], update["game_hk.dat"]["download_url"])
checker( "Server.ini", update["Server.ini"]["latest_md5"], update["Server.ini"]["download_url"])

print green("搞撚掂哂！依家所有檔案都係最新啦！如果仲係有問題就問樓豬啦～\n").decode("utf-8")
raw_input()