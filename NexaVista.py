import requests,os,json,re,time
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def temiz():
      os.system("cls" if os.name == "nt" else "clear")

reset = "\033[0m"
kırmızı = "\033[38;5;196m"
mavi          = "\033[38;5;27m"
canli_mavi    = "\033[38;5;33m"
acik_mavi     = "\033[38;5;39m"
mavi_menekse  = "\033[38;5;69m"
morumsu_mavi  = "\033[38;5;99m"
menekse       = "\033[38;5;129m"
parlak_mor    = "\033[38;5;135m"
mor_gecis     = "\033[38;5;165m"
neon_mor      = "\033[38;5;201m"
neon_mavi = "\033[38;5;44m"
yesil = "\033[38;5;118m"

HTTP_HATA_MESAJLARI = {}

def banner():
      print(f"\n{acik_mavi}                                    Fast"+mavi)
      print(r"  _   _             __      ___     _   "+mor_gecis+"Scan"+mavi)
      print(r" | \ | |            \ \    / (_)   | |      "+acik_mavi+"Fast"+mavi)
      print(r" |  \| | _____  ____ \ \  / / _ ___| |_ __ _    "+mor_gecis+"Sort"+mavi)
      print(r" | . ` |/ _ \ \/ / _` \ \/ / | / __| __/ _` |  ")
      print(r" | |\  |  __/>  < (_| |\  /  | \__ \ || (_| |")
      print(r" |_| \_|\___/_/\_\__,_| \/   |_|___/\__\__,_|")
      print("")
      print("\033[38;5;165m        NexaVista - v1.0 ")
      print("            Created by: github.com/KauelaKawela"+reset)

def int_kontrol():
      try:
           requests.get("https://www.google.com",timeout=3)
      except requests.ConnectionError:
           print(f"{menekse}║\n║\n╚════════════╝ {kırmızı}İnternet bağlantısı yok! Lütfen bağlantınızı kontrol edin.{reset}")
           exit()

def load_hata_code():
      try:
           with open("hata_codes.json","r",encoding="utf-8") as hc:
                return json.load(hc)
      except FileNotFoundError:
           print(f"{menekse}║\n║\n╚════════════╝{reset} 'hata_codes.json' {kırmızı}hata kodu dosyası bulunamadı!{reset}")
           exit()

def load_categori(file_categori):
       try:
           with open(file_categori,"r",encoding="utf-8") as fc:
                categories = [line.strip() for line in fc if line.strip()] 
           return categories
       except FileNotFoundError:
            print(f"{menekse}║\n║\n╚════════════╝{reset} '{file_categori}'{kırmızı} kategori dosyası bulunamadı!{reset}")
            exit()

def load_keywords(keys):
       try:
           with open(keys,"r",encoding="utf-8") as ky:
               return json.load(ky)
       except FileNotFoundError:
           print(f"{menekse}║\n║\n╚════════════╝{reset} '{keys}' {kırmızı}dosyası bulunamadı!{reset}")
           exit()

def classify(link, keywords):
       for kategori, kelimeler in keywords.items():
             for kelime in kelimeler:
                   if kelime.lower() in link.lower():
                       return kategori
       return "Bilinmiyor"

def output_folder():
       if not os.path.exists("output"):
           os.makedirs("output")

def write_link_to_file(link, kategori,uzantı,durum):
    try:
        if not link.startswith("http://") and not link.startswith("https://"):
           link = "https://" + link
        kategori = re.sub(r'[^\w\-_.]', '_', kategori)
        filename = f"output/{kategori}.{uzantı.lstrip('.')}"
        with open(filename,"a",encoding="utf-8") as wf:
            if durum:
                wf.write(f"{link} ({durum}) \n")
            else:
                wf.write(f"{link} \n")
    except Exception as e:
        print(f"'{kategori}' {kırmızı}kategorisine ait link dosyaya yazılamadı: {reset}{e}")

def url_status_cek(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
    try:
        response = requests.head(url, timeout=5,allow_redirects=True)
        kod = response.status_code
        time.sleep(0.2)
        if 200 <= kod < 300:
            return ""
        else:
            return HTTP_HATA_MESAJLARI.get(str(kod), f"Hata kodu: {kod}")
    except requests.exceptions.RequestException as e:
        return f"{kırmızı}Hata:{reset} {e}"
        
def kategorize_et():
      print(rf"""{neon_mor}╠═════════════════════════════════════╗
{mor_gecis}║       Linkleri Kategorize Et        ║
{neon_mor}╠═════════════════════════════════════╣""")
      link_file = input(f"{parlak_mor}╠═══════ > Link dosya yolu: {reset}")
      if not os.path.exists(link_file):
          print(f"{menekse}║\n{morumsu_mavi}║\n{mavi_menekse}╚════════════╝ '{link_file}' {kırmızı}link dosyası bulunamadı{reset}")
          exit()
      uzantı = input(f"{menekse}╠ >$ Dosya uzantısı giriniz: {reset}")
      int_kontrol()
      output_folder()
      keywords = load_keywords("keywords.json")
      links = extract_links(link_file)
      for link in links:
            durum = url_status_cek(link)
            kategori = classify(link, keywords)
            write_link_to_file(link, kategori,uzantı,durum)
            if durum:
                print(f"[{kategori}] >>> {link} ({durum})")
            else:
                print(f"[{kategori}] >>> {link}")
      input(f"{menekse}║\n║\n╚════════════╝Menüye dönmek için herhangi bir tuşa basın")
      main()
      
def extract_links(file_links):
    try:
        with open(file_links, "r", encoding="utf-8") as fl:
            return [match.group(1).strip()
                    for line in fl
                    if (match := re.search(r"(https?://[^\s)>\]]+)", line))]
    except FileNotFoundError:
        print(f"{menekse}║\n║\n╚════════════╝ {file_links}' {kırmızı}link dosyası bulunamadı!{reset}")
        exit()
        
def gecersiz_links():
      print(rf"""{neon_mor}╠═════════════════════════════════════╗
{mor_gecis}║      Geçersiz Linkleri Listele      ║
{neon_mor}╠═════════════════════════════════════╣""")
      link_file = input(f"{parlak_mor}╠═══════ > Link dosya yolu: {reset}")
      if not os.path.exists(link_file):
          print(f"{menekse}║\n{morumsu_mavi}║\n{mavi_menekse}╚════════════╝ '{link_file}' {kırmızı}link dosyası bulunamadı!{reset}")
          exit()
      uzantı = input(f"{menekse}╠ >$ Dosya uzantısı giriniz:{reset} ")
      int_kontrol()
      links = extract_links(link_file)
      output_folder()
      gecersiz_path = f"output/gecersiz_links.{uzantı.lstrip(".")}"
      with open(gecersiz_path, "a", encoding="utf-8") as outfile:
             for link in links:
                  durum = url_status_cek(link)
                  if durum:
                      print(f"{link} ({durum})")
                      outfile.write(f"{link} ({durum})\n")
      print(f"\n{yesil}Geçersiz linkler '{gecersiz_path}' dosyasına kaydedildi{reset}")

def baslik_getir(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.title.string.strip() if soup.title else "(başlık yok)"
    except Exception as e:
        return f"(hata: {e})"
              
def baslık_cek():
      print("Henüz geliştirilmektedir")
      exit()

def kategori_elementleri():
    klasor = "output"
    kategoriler = {}
    if not os.path.isdir(klasor):
        print(f"{neon_mor}║\n║\n{mor_gecis}╚════════════╝ {kırmızı}Kategori dosyası bulunamadı..{reset} ")
        input(f"{menekse}║\n╚══════ > Menüye dönmek için tuşlayın.. {reset}")
        main()
    if not os.listdir(klasor):
        print(f"{neon_mor}║\n║\n{mor_gecis}╚════════════╝ {kırmızı}Kategori dosyası boş..{reset}")
        input(f"{menekse}║\n╚══════ > Menüye dönmek için tuşlayın.. {reset}")
        main()
    for dosya in os.listdir(klasor):
        if dosya.endswith(".txt"):
            kategori = dosya.replace(".txt", "")
            yol = os.path.join(klasor, dosya)
            try:
                with open(yol, "r", encoding="utf-8") as f:
                    kelimeler = [satir.strip() for satir in f if satir.strip()]
                    kategoriler[kategori] = kelimeler
            except Exception as e:
                print(f"Hata: {yol} okunamadı -> {e}")
    for kategori, kelimeler in kategoriler.items():
          print(f"{menekse}╠═ {kategori.upper():<20}{reset} ➜ {len(kelimeler)} link")
          input(f"{morumsu_mavi}║\n╚══════ > Menüye dönmek için tuşlayın.. {reset}")
          main()

def yardım():
      print(f"{neon_mor}╠═════════════════ Yardım Menüsü ═════════════════╗")
      print(f"{neon_mor}║ 1 - Linkleri anahtar kelimelere göre kategorilere ayırır")
      print(f"{mor_gecis}║ 2 - Ulaşılamayan linkleri kontrol eder ve listeler ")
      print(f"{parlak_mor}║ 3 - Linklerden <title> başlığını çeker")
      print(f"{menekse}║ 4 - Her kategoride kaç link olduğunu gösterir")
      print(f"{morumsu_mavi}║ 5 - Bu yardım menüsünü gösterir")
      print(f"{mavi_menekse}║ 0 - Uygulamadan çıkış yapar")
      print(f"{acik_mavi}╠═════════════════════════════════════════════════╝ ")
      input(f"{canli_mavi}║\n╚══════ > Menüye dönmek için tuşlayın.. {reset}")
      main()
      
def cıkıs():
     print(f"{neon_mor}║\n║\n{mor_gecis}╚════════════╝ {kırmızı}Çıkış yapılıyor..{reset}")
     exit()
     
def MENU(secilmis):
      secim_haritası = {
      "0": cıkıs,
      "1": kategorize_et,
      "2": gecersiz_links,
      "3": baslık_cek,
      "4": kategori_elementleri,
      "5": yardım
      }
      secim_haritası.get(secilmis,f"{kırmızı}Hatalı girdi! İşlem sonlandırılıyor{reset}")()
      
def main():
      output_folder()
      global HTTP_HATA_MESAJLARI
      HTTP_HATA_MESAJLARI = load_hata_code()
      temiz()
      banner()
      try:
          menu = input(f"""{mavi}╔═════════════════════════════════════╗
{mavi}║          NexaVista - Menü           ║
{canli_mavi}╠═════════════════════════════════════╣
{acik_mavi}║ 1 - Linkleri Kategorize Et          ║
{mavi_menekse}║ 2 - Geçersiz Linkleri Listele       ║
{morumsu_mavi}║ 3 - Linklerden Başlık Çek           ║
{menekse}║ 4 - Kategori Sayılarını Göster      ║
{parlak_mor}║ 5 - Hakkında / Yardım               ║
{mor_gecis}║ 0 - Çıkış                           ║
{neon_mor}║
{neon_mor}║
{neon_mor}╠═══════╝ $ {reset}""")
          MENU(menu)
      except KeyboardInterrupt:
           print(f"{neon_mor}║\n║\n{mor_gecis}╚════════════╝ {kırmızı}İşlem sonlandırıldı{reset}")
      except AttributeError:
           print(f"{neon_mor}║\n║\n{mor_gecis}╚═══════════╝ {kırmızı}Hatalı girdi türü! Geçerli bir değer girin{reset}")
      except TypeError:
           print(f"{neon_mor}║\n║\n{mor_gecis}╚═══════════╝ {kırmızı}Hatalı girdi türü! Geçerli bir değer girin{reset}")
      except Exception as e:
           print(f"{neon_mor}║\n║\n{mor_gecis}╚════════════╝ {kırmızı}Hata: {e}{reset}")
if __name__ == "__main__":
   main()