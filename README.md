IrisIp

<img width="1906" height="905" alt="Ekran görüntüsü 2026-01-07 013434" src="https://github.com/user-attachments/assets/6a0345f4-c617-4097-a4db-563aaf7da9a3" />


Gelişmiş Ağ Keşif ve Zafiyet Tarama Aracı

IrisIp, hedef IP veya host üzerinde detaylı ağ analizi ve güvenlik taramaları gerçekleştirmek üzere tasarlanmış, menü tabanlı bir siber güvenlik otomasyon aracıdır.
Arka planda Nmap ve Nikto gibi endüstri standardı araçları kullanarak sızma testi (pentest) süreçlerinin bilgi toplama aşamasını hızlandırır.

Manuel olarak çalıştırılması zaman alan karmaşık tarama komutlarını otomatikleştirerek, kullanıcıya hızlı ve raporlanabilir sonuçlar sunar.

TEMEL ÖZELLİKLER

IrisIp, hedef sistem üzerinde aşağıdaki analizleri gerçekleştirebilir:

• Port Tarama
Hedef üzerindeki açık TCP/UDP portlarını ve bu portlarda çalışan servisleri tespit eder.

• Servis ve Versiyon Tespiti
Çalışan servislerin (Apache, SSH, FTP vb.) üretici ve sürüm bilgilerini analiz eder.

• İşletim Sistemi Tespiti
TCP/IP yığını analizi ile hedefin olası işletim sistemini (Linux, Windows vb.) belirler.

• Zafiyet Tarama
Nmap Scripting Engine (NSE) ve Nikto veritabanlarını kullanarak bilinen güvenlik açıklarını (CVE) ve konfigürasyon hatalarını araştırır.

• Traceroute ve Firewall Tespiti
Hedefe giden ağ yolunu haritalandırır ve aradaki Firewall / WAF varlığını analiz eder.

GEREKSİNİMLER

Aracın tam fonksiyonlu çalışabilmesi için aşağıdaki bileşenlerin sistemde yüklü olması gerekir:

• Python 3.x
• Nmap
• Nikto

KURULUM

Projeyi yerel makinenize klonlamak ve gerekli izinleri vermek için:

• git clone https://github.com/KULLANICI_ADI/IrisIp.git

• cd IrisIp
• chmod +x irisip.py

KULLANIM

Aracı başlatmak için terminalde aşağıdaki komutu çalıştırın:

• python3 irisip.py

Program başlatıldığında, tarama seçeneklerini içeren menü tabanlı bir arayüz sunulur.

ÖRNEK KULLANIM SENARYOSU

• Hedef IP veya host adresi girilir
(Örn: 192.168.1.10 veya scanme.nmap.org)

• Menüden istenilen tarama modu seçilir
(Hızlı Tarama, Kapsamlı Tarama, Zafiyet Analizi vb.)

• Tarama sonuçları terminal ekranında görüntülenir

YASAL UYARI

Bu araç (IrisIp), yalnızca eğitim amaçlı ve izinli sızma testlerinde kullanılmak üzere geliştirilmiştir.
Yetkisiz sistemlere karşı kullanılması kesinlikle yasaktır ve yasal suç teşkil eder.

Geliştirici, bu aracın kötüye kullanımından doğabilecek herhangi bir zarardan sorumlu tutulamaz.
