#!/usr/bin/python2
#coding=utf-8

import os
#O = '\x1b[1;96m'
P = '\033[0;00m'
J = '\033[0;33m'
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
B='\033[0;36m'
ff='\033[0;36m'
G='\033[0;36m'
p='\033[00m'
h='\033[0;90m'
os.system("clear")
print("%s[•]%s-------------------------------------------------%s[•]"%(P,B,P))
print("%s[•]%s           TABLE PEMBELIAN TOOLS LITE            %s[•]"%(P,I,P))
print("%s[•]%s-------------------------------------------------%s[•]"%(P,B,P))
print("%s[1] HARGA    : %s25K >>>> WAKTU 1 BULAN MAX 1 DEVICE"%(P,U))
print("%s[2] HARGA    : %s50K >>>> UNLIMITED MAX 1 DEVICE"%(P,U))
print("%s[3] HARGA    : %s100k >>> FILE FULL OPEN SOURCE "%(P,U))
print("%s[•]%s-------------------------------------------------%s[•]"%(P,B,P))
print("%s | "%(B))
lite = raw_input("%s[•] Apakah anda ingin membeli %sY/t : %s"%(P,I,B))
if lite in (""," "):
   print("%s | "%(B))
   print("%s[•] Isi Dengan Benar !!"%(M));exit()
elif lite in ("Y","y"):
     print("%s | "%(B))
     print("%s[•] Anda akan di arahkan ke whatsapp admin"%(P))
     os.system("xdg-open https://wa.me/6281392505882?text=Asalamualaikum+Bang+*Jeeck*+*X*+*Nano*+Saya+Ingin+Membeli+Tools+LITE")
elif lite in ("T","t"):
     print("%s | "%(B))
     print("%s[•] Yakin nggak mau beli bang : ("%(P));exit()
