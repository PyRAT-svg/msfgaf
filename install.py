import os
import time

os.system('pkg install unstable-repo')
os.system('apt upgrade')
os.system('apt install gem -y')
os.system('apt install figlet -y')
os.system('gem install lolcat -y')
os.system('apt install metasploit -y')
os.system('dpkg -i apktool.deb')
os.system('rm -rf apktool.deb')
os.system('mv gafar97port.first.ovpn /storage/emulated/0/')
os.system('mkdir Malware')
print "Silahkan Download Aplikasi OpenVPN"
time.sleep(5)
os.system('termux-open https://play.google.com/store/apps/details?id=net.openvpn.openvpn')
print "Kemudian Install Apk Signer"
time.sleep(5)
os.system('termux-open https://play.google.com/store/apps/details?id=com.haibison.apksigner')
time.sleep(5)
os.system('rm -rf install.py')
os.system('python2 msfgaf.py')
os.system('')
