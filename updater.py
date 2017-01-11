#coding=utf-8
import hashlib    
import urllib,urllib2
import json
import os.path
import requests
from colors import red, green, blue
from clint.textui import progress

ver = "1.0"

m = hashlib.md5()

def checker( file, md5, download_url ):
    if os.path.exists(file) is False:
        print red('巴打我搵唔到' + file + '喎，你肯定你已經將呢個Program放左入傭兵根目錄？').decode("utf-8")
        return
    m = hashlib.md5()
    fd = open(file,"rb")
    x = fd.read()
    fd.close()
    m.update(x)
    md5_returned = m.hexdigest()
    if md5_returned != md5:
        print green("搵到更新！依家即刻幫你更新" + file).decode("utf-8")
        r = requests.get(download_url, stream=True)
        path = file
        with open(path, 'wb') as f:
            total_length = int(r.headers.get('content-length'))
            for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
                if chunk:
                    f.write(chunk)
                    f.flush()
    else:
        print blue("搵唔到" + file + "有更新喎巴打！如果入唔到既可能係樓豬未Upload最新既File上Server，請盡情咁屌佢老母啦不過屌完都係要等架啦").decode("utf-8")


r=requests.get("https://raw.githubusercontent.com/l2003201/WL-Updater/master/update.json")
r.json()
update = json.loads(r.text, encoding="utf-8")

if update["version"] != ver:
    print red('呢舊更新器好似有更新喎得閒就記得Download返個更新檔啦喂～').decode("utf-8")

checker( "V_hk.Dat", update["V_hk.Dat"]["latest_md5"], update["V_hk.Dat"]["download_url"])
checker( "game.dat", update["game.dat"]["latest_md5"], update["game.dat"]["download_url"])
checker( "game_hk.dat", update["game_hk.dat"]["latest_md5"], update["game_hk.dat"]["download_url"])
checker( "Server.ini", update["Server.ini"]["latest_md5"], update["Server.ini"]["download_url"])

print green("搞撚掂哂！依家所有檔案都係最新啦！如果仲係有問題就問樓豬啦～").decode("utf-8")
raw_input()