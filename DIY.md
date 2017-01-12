V_hk.Dat製作教學
===================

V_hk.Dat係記錄住版本號既一個文件

飄流傭兵需要模擬官方既封包黎登入各位既帳號，而官方既封包會包含住當前你遊戲既版本號。飄流更新之後版本號當然會變，但飄流傭兵仍然用緊舊既版本號，所以要手動幫傭兵更新版本號既封包先可以登入，否則會出現「版本不符禁止登入」令到傭兵用唔到。

不過V_hk.Dat難求，又唔可以第一時間做更新，經常為左個V_hk.Dat受氣做乞兒仔，咁不如靠自己DIY個V_hk.dat出黎啦

----------


V_hk.Dat更新方法
-------------

 1. 7Moe論壇, 但更新慢，又要回覆又要扣論壇積分
 2. 用我個Updater, 免費, 方便, 但未必可以第一時間Push到個更新
 3. DIY, 有少少麻煩，但免費，第一時間就拎到更新
 
 以上三種方法各位識揀啦，有少少IT能力既就揀第3，否則就只可以等我Push更新啦～


----------


V_hk.Dat DIY教學
--------------

1.首先我地要準備`WPE`同`winhex`呢兩個Software，取得方法就自己Google啦唔好咁懶

2.打開飄流(官方客戶端)至登入畫面，同埋以`系統管理員`身份打開`WPE`

3.利用`WPE`既`Target Program`揀返飄流個客戶端
![Step3](http://i.imgur.com/KAvxvyv.png)

4.預先輸入好帳號密碼( 絕對絕對唔可以入你正確既AC同PW, 因為事後可以分析個封包得出你既帳號密碼，只要格式正確就可以)，然後禁`WPE`既`箭咀`，再禁登入
![Step4](http://i.imgur.com/twMcFnR.jpg)

5.禁登入之後應該會出現帳號密碼錯誤或者斷線訊息，之後返`WPE`禁`紅色正方形`，之後就可以關閉飄流啦～
![Step5](http://i.imgur.com/8kY4oHK.jpg)

6.之後`WPE`應該會出現哂開始到結束時飄流開始到結束之間既所有封包，留意下個登入封包。如果第五六格係`92 AC`咁佢就肯定係傳送登入資料既封包，搵佢出黎右Click將佢`Add to Send List`
![Step6](http://i.imgur.com/3rDyh4S.png)

7.係返Wpe開返Send列表，將呢個封包Save低
![Step7](http://i.imgur.com/cpp0f6X.png)

8.用`Winhex`打開剛才Save既封包，禁`Ctrl + A`之後再禁
`Ctrl + T`，開出`Modify Block Data`介面，選擇`XOR`，旁邊值輸入`AD`，再OK將封包解密.
![Step8](http://i.imgur.com/XfWv9zA.png)

9.之後你就會得到已經解密既封包
![Step9](http://i.imgur.com/tatVED7.png)

10.因為新飄既代號係`HP`而H既16進制算法係`48` P既16進制係`50`，所以我地要將`48 50`前面既數值全部刪除，先反白`48 50`之前既所有數值，之後禁`Edit`，然後`Remove`
![Step10](http://i.imgur.com/6U97uNV.png)
![Step10-2](http://i.imgur.com/WSZwEBj.png)

11.但係HP同版本號之間仲有D唔需要既野，我地同時要將佢刪除。將`48 50`  之後2格 ( 今次係 `15 04` 下次未必一樣 )同`07`之間既所有數值`反白` > `Edit` > `Remove`
![Step11](http://i.imgur.com/87gfZqT.png)
![Step11-2](http://i.imgur.com/Yin4xbE.png)

12.`File` > `Save As` ，將佢儲存係傭兵目錄並覆蓋舊版既V_hk.Dat
![Step12](http://i.imgur.com/bOV9hKb.png)
![Step12-2](http://i.imgur.com/VgWJexW.png)

13.開傭兵測試，連到線就搞撚掂啦！
![Step13](http://i.imgur.com/4KkxmZd.png)