#!/usr/bin/env python3

import os
import time
import sys
import itertools 
import subprocess
import json


RESET = "\033[0m"
BOLD = "\033[1m"
WHITE = "\033[97m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RED = "\033[91m"
MAGENTA = "\033[1;30m"
CYAN = "\033[96m"
MATRIX = GREEN + BOLD
MENU_WHITE = WHITE + BOLD

if os.geteuid() != 0:
    print(RED + BOLD + "\n[!] Bu arac icin root yetkisi gerekmektedir" + RESET)
    sys.exit()

def launch_zenmap():
    try:
        terminals = [
            ["gnome-terminal", "--", "zenmap"],
            ["xterm", "-e", "zenmap"],
            ["konsole", "-e", "zenmap"],
            ["xfce4-terminal", "-e", "zenmap"]
        ]
        for term_cmd in terminals:
            try:
                subprocess.Popen(term_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print(f"{GREEN}[+] Zenmap acildi{RESET}")
                return
            except:
                continue
        subprocess.Popen(["zenmap"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except: pass

def install_requirements():
    tools = ["nmap", "arp-scan", "whois", "dig", "curl"]
    devnull = open(os.devnull, 'w')
    for tool in tools:
        if subprocess.call(["which", tool], stdout=devnull, stderr=devnull) != 0:
            print(f"{RED}[!] {tool} eksik, Yukleniyor...{RESET}")
            os.system(f"apt-get install -y {tool}")
    devnull.close()

def loading_animation():
    os.system("clear")
    spinner = itertools.cycle(["|", "/", "-", "\\"])
    print(f"{MENU_WHITE}Sistem aciliyor ", end="", flush=True)
    for _ in range(20):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.15)
        sys.stdout.write("\b")
    print(f" {MAGENTA}Hosgeldiniz{RESET}\n")
    time.sleep(1)
    os.system("clear")
    
def run_geoip(ip):
    print(MATRIX + f"\n--- Konum ve Istihbarat Analizi: {ip} ---\n" + RESET)
    try:
        result = subprocess.check_output(f"curl -s http://ip-api.com/json/{ip}", shell=True).decode()
        data = json.loads(result)
        
        if data['status'] == 'fail':
            print(f"{RED}[!] HATA: Gecersiz IP veya sorgu basarisiz.{RESET}")
            return

        print(f"{YELLOW} Hedef IP:      {WHITE}{data.get('query')}")
        print(f"{YELLOW} Ülke:          {WHITE}{data.get('country')} ({data.get('countryCode')})")
        print(f"{YELLOW} Şehir/Bölge:   {WHITE}{data.get('city')} / {data.get('regionName')}")
        print(f"{YELLOW} ISP (Şirket):  {WHITE}{data.get('isp')}")
        print(f"{YELLOW} Organizasyon:  {WHITE}{data.get('org')}")
        print(f"{YELLOW} Zaman Dilimi:  {WHITE}{data.get('timezone')}")
        print(f"{YELLOW} Koordinatlar:  {WHITE}{data.get('lat')}, {data.get('lon')}")

        print(f"{CYAN} [Harita Linki]: https://www.google.com/maps/place/{data.get('lat')},{data.get('lon')}{RESET}")

    except Exception as e:
        print(f"{RED}[!] Baglanti hatasi: {e}{RESET}")
    
    print("\n")

def show_banner():
    os.system("clear")
    print(MENU_WHITE + r"""
                                     
""" + RESET)

    print(RED + r"""
                           +*#+#*############*#*%*                            
                      +**##%%@@@@@@@@@@@@@@@@@@@@%%##***                       
                   **##%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%#*#*+                   
                **#%%@%@%@@@@%%##************##%%@@@@@%@#@%#*#*                
             ***%#@@%@%%@##***#######****########***##@%@@%@%%#*#*              
          +*#*%%@@%@%%#*#%#########****###%%%#######%%###%%@%@@%%*#*+        
       +*##%@%@@%@%###%%%%#######****++++*##**#######%%%%##*%@%@@%@###*      
     *#*%%@%@@%%#*#%%%%%%###%######+=--=--=+######%###%%%%%%%*%%%@%@@###**   
   ##*%%@@%@@#*#%%%%%%%%%##%%%####+==+===+==*#####%###%%%%%%%%%%*#@@%@@%%*#* 
 **#%%%@%@%##%@@@@@@@@@@@%%%%%%###*+++*%+*++*####%%%#%%@@@@@@@@@@%##%%%@%%%#*+
*#%%%%@####@@@@@@@@@@@@@@%#%%%%###*===+++===####%%%%%%@@@@@@@@@@@@@%####@%%%#**
###%#*#%###@@@@@@@@@@@@@@%%%%%%%%###+=====+###%%%%%%%@@@@@@@@@@@@@@###%%#*#%%%#
*#####**#*###%%@@@@@@@@@@@%%%%%%%%###########%%%%%%%%@@@@@@@@@@%%%#******#####*
  +***++*+##%##**##%@@@@@@@%#%%%%%%%######%%%%%%%%#%@@@@@@%%####%%%*#+*++**+   
          +*****##%*#**#%@@@%##%%%%%%%%%#%%%%%%%#%@@@%%#*###%##***++           
               +***###%###*#%%%##%#%%%%%%%%%%##%%%#**###%##***+                
                   ++**##%%%%####*##########*#*###%%%##***#+                   
                      +***##%%%%%%%%######%%%%%%%%%#****                       
                          ******##############**+**#*                          
                              +*****######*****+                                             
""" + RESET)

def show_menu():
    print(f"\n{BOLD}{MAGENTA}[KESIF VE ANALIZ]{RESET}")
    print(f"{WHITE}[1] Agda bulunan cihazlar")
    print(f"{WHITE}[2] Os Ve Acik Calisan Servis Analizi")
    print(f"{WHITE}[3] Hizli Port Taramasi (Top 100)")
    print(f"{WHITE}[4] Mobile Cihaz Taraması")

    print(f"\n{BOLD}{MAGENTA}[SALDIRI VE GUVENLIK]{RESET}")
    print(f"{WHITE}[5] Agresif Tarama(TCP+UDP){RESET}")
    print(f"{WHITE}[6] Guvenlik Zaafiyet Taramasi")
    print(f"{WHITE}[7] Tum Portlari Tarama (1-65535)")

    print(f"\n{BOLD}{MAGENTA}[GIZLILIK VE SIZMA]{RESET}")
    print(f"{WHITE}[8] Firewall Tanima Analizi")
    print(f"{WHITE}[9] Hayalet Tarama")
    print(f"{WHITE}[10] Firewall Atlat Tarama")
    
    print(f"\n{BOLD}{MAGENTA}[SORGU]{RESET}")
    print(f"{WHITE}[11] Whois Sorgusu (Person)")
    print(f"{WHITE}[12] Lokasyon Sorgusu (Person)")
    print(f"{WHITE}[13] Dig Taramasi (Serves)")    
    
    print(f"\n{BOLD}{MAGENTA}[DIGER]{RESET}")
    print(f"{WHITE}[14] Ozel Port Taramasi (Manuel)")
    
    print(f"\n{WHITE}[•] 1-3,7-6 (Windows icin port 445)") 
    print(f"{WHITE}[•] 2 acik portun ne icin kullanıldıgını gormek")
    print(f"{WHITE}[•] 5 cikmasi zor portlar")
    print(f"{WHITE}[•] 8 Filtered, gizli portlar")
    print(f"{WHITE}[•] 9-10 Yakalanmamak")
    print(f"\n{RED}[0] Cikis{RESET}")

def run_scan(command, ip_needed=True):
    ip = ""
    if ip_needed:
        raw_ip = input(MENU_WHITE + "\nKurban IP: " + RESET)
        ip = raw_ip.replace(";", "").replace("&", "")
        if not ip: return
        final_command = command.format(ip=ip)
    else:
        final_command = command
    
    print(GREEN + f"\n[i] Calistiriliyor: {final_command}" + RESET)
    os.system(final_command)
    input(MENU_WHITE + "\nDevam etmek icin Enter..." + RESET)

def main():
    install_requirements()
    loading_animation()
    #launch_zenmap()
    
    while True:
        show_banner()
        show_menu()
        try:
            choice_input = input(MENU_WHITE + "\nSeciminiz: " + RESET)
            if not choice_input.isdigit(): continue
            choice = int(choice_input)
        except ValueError: continue

        if choice == 0:
            print(MAGENTA + "Cikis yapiliyor..." + RESET)
            break

        commands = {
            1: "arp-scan --localnet --ignoredups", 
            2: "nmap -sV --version-intensity 9 -O --osscan-guess -Pn {ip}",
            3: "nmap -F {ip}",
            4: "nmap -sU -sS -p U:5353,1900,62078,8008,8009,T:62078,5555,5000,7000 -Pn -n --script=dns-service-discovery,upnp-info {ip}",
            5: "nmap -sS -sU -p- -A -T4 -Pn --min-rate 1000 {ip}",
            6: "nmap -sV --script vuln --script-args=unsafe=1 -Pn {ip}",
            7: "nmap -p- -sV -T4 --min-rate 2000 -Pn --open {ip}",
            8: "nmap -sA -Pn {ip}",
            9: "nmap -sS -D RND:10 -Pn -T3 {ip}",
            10: "nmap -f -g 53 --mtu 24 -Pn {ip}",
            11: "whois -a --verbose {ip}",
            13: "dig {ip} A AAAA MX NS TXT SOA +noall +answer"
        }
        
        if choice == 12:
            raw_ipp = input(MENU_WHITE + "Kurban IP: " + RESET)
            ip = raw_ipp.replace(";", "").replace("&", "").strip()
            
            if ip:
                run_geoip(ip)
            else:
                print(f"{RED}[!] IP girilmedi{RESET}")
            input(MENU_WHITE + "Devam etmek icin Enter..." + RESET)

        if choice == 14:
            raw_ip = input(MENU_WHITE + "Kurban IP: " + RESET)
            ports = input(MENU_WHITE + "Portlar (orn: 80,443): " + RESET)
            run_scan(f"nmap -p {ports} {raw_ip}", ip_needed=False)
            
        elif choice in commands:
            ip_needed = True
            if choice == 1: ip_needed = False
            run_scan(commands[choice], ip_needed)

if __name__ == "__main__":
    main()