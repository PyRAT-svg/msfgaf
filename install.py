import os, sys
import time
import random

def flush(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)

def nxt():
	print putih+'---------------------------------------------------'
	raw_input('\n\x1b[1;91m					[ \x1b[1;97mNext \x1b[1;91m]')

flush('izinkan akses penyimpanan')
nxt()
os.system('termux-setup-storage')
nxt()
os.system('pkg install unstable-repo')
os.system('apt upgrade')
os.system('apt install ruby -y')
os.system('apt install figlet')
os.system('gem install lolcat')
flush('Anda akan menginstall Metasploit package')
flush('proses ini akan membutuhkan beberapa waktu')
nxt()
os.system('apt install metasploit -y')
flush('installing Apktool')
nxt()
os.system('dpkg -i apktool.deb')
os.system('rm -rf apktool.deb')
os.system('mv gafar97port.first.ovpn /storage/emulated/0/')
os.system('mkdir Malware')
os.system('clear')
print "Silahkan Download Aplikasi OpenVPN"
nxt()
os.system('termux-open https://play.google.com/store/apps/details?id=net.openvpn.openvpn')
print "Kemudian Install Apk Signer"
nxt()
os.system('termux-open https://play.google.com/store/apps/details?id=com.haibison.apksigner')
print "Download WhatsApp db extracktor" 
nxt()
os.system('termux-open https://play.google.com/store/apps/details?id=com.smeiti.wstotext')
print 'Yang terakhir Silahkan Download GBWhatsApp'
os.system('termux-open http://cdn3.gbplus.net/2/?wpdmpro=10-40-1&wpdmdl=14&masterkey=5ecfd251cdc1a')
flush('cleaning...')
nxt()
os.system('rm -rf install.py')
flush('Starting MSFGAF')
os.system('python2 msfgaf.py')