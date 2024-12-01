import os
import time
import socket
import ipaddress
from colorama import Fore, Style

time.sleep(2)
print(Fore.MAGENTA + """
███    ██ ███    ███  █████  ██████
████   ██ ████  ████ ██   ██ ██   █
██ ██  ██ ██ ████ ██ ███████ ██████
██  ██ ██ ██  ██  ██ ██   ██ ██
██   ████ ██      ██ ██   ██ ██""")

print(Fore.RED + """
producer  〔coded by enesxsec〕
instagram 〔xsecit〕
github    〔https://github.com/ghost0x02""")

print(Fore.YELLOW + "----------------------------------------")
time.sleep(1)
print(Style.RESET_ALL)

print(Fore.RED + """

1) -O TARAMASI
---------------------------""")
print(Fore.GREEN + """
2) -vv TARAMASI
---------------------------""")
print(Fore.CYAN + """
3) -sV TARAMASI
---------------------------""")
print(Fore.YELLOW + """
4) -A TARAMASI
---------------------------""")
print(Fore.BLUE + """
5) --data-length TARAMASI
---------------------------""")

print(Style.RESET_ALL)
print(Fore.MAGENTA + "")
islemno = input("root@nmap:~ ")
print(Style.RESET_ALL)
print(Fore.RED + "")

def ip_dogrula(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

if islemno in ["1", "2", "3", "4", "5"]:
    hedef_ip = input("Lütfen ip girin: ")

    if ip_dogrula(hedef_ip):
        if islemno == "1":
            os.system(f"nmap -O {hedef_ip}")
        elif islemno == "2":
            os.system(f"nmap -vv {hedef_ip}")
        elif islemno == "3":
            os.system(f"nmap -sV {hedef_ip}")
        elif islemno == "4":
            os.system(f"nmap -A {hedef_ip}")
        elif islemno == "5":
            os.system(f"nmap --data-length 32 {hedef_ip}")

    else:
        print(Fore.RED + "Hata: Geçersiz IP adresi girdiniz. Lütfen doğru bir IP adresi girin." + Style.RESET_ALL)

else:
    print(Fore.RED + "Hata: Geçersiz işlem numarası seçtiniz. Lütfen 1-5 arasında bir seçenek girin." + Style.RESET_ALL)
