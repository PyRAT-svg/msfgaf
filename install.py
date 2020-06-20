import os, sys
import time
import random

os.system('clear')

def flush(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)

def nxt():
	print '---------------------------------------------------'
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
os.system('mkdir Malware')
os.system('clear')
flush('cleaning...')
nxt()
os.system('rm -rf install.py')
flush('Starting MSFGAF')
os.system('python2 msfgaf.py')
