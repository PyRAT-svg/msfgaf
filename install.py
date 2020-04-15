import os
import time

os.system('pkg install unstable-repo')
os.system('apt upgrade')
os.system('apt install metasploit -y')
os.system('dpkg -i apktool.deb')
os.system('rm -rf apktool.deb')
os.system('mv gafar97port.first.ovpn /storage/emulated/0/')
os.system('pip2 install bs4')
os.system('cd ..')
os.system('clear')
print "Silahkan Download Aplikasi OpenVPN"
time.sleep(3)
os.system('termux-open https://play.google.com/store/apps/details?id=net.openvpn.openvpn')
print "Kemudian Install Apk Signer"
time.sleep(4)
os.system('termux-open https://play.google.com/store/apps/details?id=com.haibison.apksigner')
time.sleep(4)
os.system('rm -rf install.py')
os.system('python2 msfgaf.py')
os.system('')
