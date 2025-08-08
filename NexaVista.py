import requests,os,json,re,time,sys
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from datetime import datetime

def temiz():
      os.system("cls" if os.name == "nt" else "clear")

r = "\033[0m"
k = "\033[38;5;196m"
m = "\033[38;5;27m"
cm = "\033[38;5;33m"
am = "\033[38;5;39m"
mam = "\033[38;5;69m"
mom = "\033[38;5;99m"
mn = "\033[38;5;129m"
pm = "\033[38;5;135m"
mg = "\033[38;5;165m"
nm = "\033[38;5;201m"
nem = "\033[38;5;44m"
y = "\033[38;5;118m"
s = "\033[38;5;226m"

HTTP_HATA_MESAJLARI = {}

def banner():
      print(f"\n{am}                                    Fast"+m)
      print(r"  _   _             __      ___     _   "+mg+"Scan"+m)
      print(r" | \ | |            \ \    / (_)   | |      "+am+"Fast"+m)
      print(r" |  \| | _____  ____ \ \  / / _ ___| |_ __ _    "+mg+"Sort"+m)
      print(r" | . ` |/ _ \ \/ / _` \ \/ / | / __| __/ _` |  ")
      print(r" | |\  |  __/>  < (_| |\  /  | \__ \ || (_| |")
      print(r" |_| \_|\___/_/\_\__,_| \/   |_|___/\__\__,_|")
      print("")
      print(f"{mg}        NexaVista - v1.0 ")
      print("            Created by: github.com/KauelaKawela"+r)

def int_kontrol():
      try:
           requests.get("https://www.google.com",timeout=3)
      except requests.ConnectionError:
           print(f"{mn}║\n║\n╚════════════╝ {k}İnternet bağlantısı yok! Lütfen bağlantınızı kontrol edin.{r}")
           sys.exit()
                    
def load_hata_code():
      try:
           with open("hata_codes.json","r",encoding="utf-8") as hc:
                return json.load(hc)
      except FileNotFoundError:
           print(f"{mn}║\n║\n╚════════════╝{r} 'hata_codes.json' {k}hata kodu dosyası bulunamadı!{r}")
           sys.exit()

def load_categori(file_categori):
       try:
           with open(file_categori,"r",encoding="utf-8") as fc:
                categories = [line.strip() for line in fc if line.strip()] 
           return categories
       except FileNotFoundError:
            print(f"{mn}║\n║\n╚════════════╝{r} '{file_categori}'{k} kategori dosyası bulunamadı!{r}")
            sys.exit()

def load_keywords(keys):
       try:
           with open(keys,"r",encoding="utf-8") as ky:
               return json.load(ky)
       except FileNotFoundError:
           print(f"{mn}║\n║\n╚════════════╝{r} '{keys}' {k}dosyası bulunamadı!{r}")
           sys.exit()

def classify(link, keywords):
       for kategori, kelimeler in keywords.items():
             for kelime in kelimeler:
                   if kelime.lower() in link.lower():
                       return kategori
       return "Bilinmiyor"

def output_folder():
       if not os.path.exists("output"):
           os.makedirs("output")
           
def uzantı_sec():
      try:
            uzantılar = {1:"txt",2:"json",3:"csv",4:"xml",5:"html"}
            print(f"\n{k} 1- [{r}txt{k}]\t2- [{r}json{k}]\t3- [{r}csv{k}]\t4- [{r}xml{k}]\n\n 5- [{r}html{k}]\t6- [{r}???{k}]\t7- [{r}???{k}]\t8- [{r}???{k}]\n")
            usecim = int(input(f"{mom}╠ > Dosya uzantısı seçiniz: {r}"))
            if usecim in uzantılar:
                return uzantılar[usecim]
            else:
                raise ValueError()
      except ValueError:
            print(f"{nm}║\n║\n{mg}╚════════════╝ {k}Hatalı seçim! Geçerli uzantı giriniz {r}")
            sys.exit()
            
def formatla(link, uzantı, durum=None):
    if uzantı.lower().strip() == "json":
        return {"link": link, "durum": durum}
    elif uzantı.lower().strip() == "csv":
        return f"{link},{durum if durum else ''}"
    elif uzantı.lower().strip() == "html":
        return f"<li><a href='{link}'>{link}</a> ({durum if durum else ''})</li>"
    elif uzantı.lower().strip() == "xml":
        return f"<link><url>{link}</url><durum>{durum}</durum></link>"
    elif uzantı.lower().strip() == "txt":
        return f"{link} ({durum})" if durum else f"{link}"
    else:
        print(f"{nm}║\n║\n{mg}╚═══════════╝ {k}Hatalı seçim türü! Geçerli uzantı girin{r}")
        sys.exit()
        
def wltf(link, kategori, uzantı, durum=None):
    try:
        if not link.startswith("http://") and not link.startswith("https://"):
            link = "https://" + link
        kategori = re.sub(r'[^\w\-_.]', '_', kategori)
        filename = f"output/{kategori}_{timestep}.{uzantı.lstrip('.')}"
        formatted = formatla(link, uzantı, durum)
        with open(filename, "a", encoding="utf-8") as wf:
            if uzantı == "json":
                json.dump(formatted, wf, ensure_ascii=False)
                wf.write("\n")
            else:
                wf.write(f"{formatted}\n")
    except Exception as e:
        print(f"'{kategori}' {k}kategorisine ait link dosyaya yazılamadı: {r}{e}")
        
def url_status_cek(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
    try:
        response = requests.head(url, timeout=5, allow_redirects=True)
        kod = response.status_code
        time.sleep(0.2)
        if 200 <= kod < 300:
            return ""
        else:
            return HTTP_HATA_MESAJLARI.get(str(kod), f"Hata kodu: {kod}")
    except requests.exceptions.ConnectionError as e:
        if "NameResolutionError" in str(e) or "[Errno -2]" in str(e) or "[Errno 7]" in str(e):
            return "000 - Alan adı çözümlenemedi (DNS Hatası)"
        else:
            return "001 - Sunucuya bağlantı sağlanamadı"
    except requests.exceptions.Timeout:
        return "002 - Zaman aşımı (timeout)"
    except requests.exceptions.MissingSchema:
        return "003 - Geçersiz URL formatı"
    except requests.exceptions.RequestException as e:
        return f"004 - Beklenmeyen hata: {e}"
        
def kategorize_et():
      print(rf"""{nm}╠═════════════════════════════════════╗
{mg}║       Linkleri Kategorize Et        ║
{nm}╠═════════════════════════════════════╣""")
      link_file = input(f"{pm}╠═══════ > Link dosya yolu: {r}")
      if not os.path.exists(link_file):
          print(f"{mn}║\n{mom}║\n{mam}╚════════════╝ '{link_file}' {k}link dosyası bulunamadı{r}")
          sys.exit()
      uzantı = uzantı_sec()
      int_kontrol()
      keywords = load_keywords("keywords.json")
      links = extract_links(link_file)
      for link in links:
            durum = url_status_cek(link)
            kategori = classify(link, keywords)
            wltf(link, kategori,uzantı,durum)
            if durum:
                print(f"{k}[{r}{kategori}{k}]{r} >>> {link} >>> {durum}\n----")
            else:
                print(f"{k}[{r}{kategori}{k}]{r} >>> {link}\n----")
      input(f"{mn}║\n║\n╚════════════╝Menüye dönmek için herhangi bir tuşa basın")
      main()
          
def extract_links(file_links):
    try:
        with open(file_links, "r", encoding="utf-8") as fl:
            return [
                match.group(1).strip()
                for line in fl
                if (match := re.search(r"(https?://[^\s\"')><]*[^\s\"')><.,;])", line))
            ]
    except FileNotFoundError:
        print(f"{mn}║\n║\n╚════════════╝ '{file_links}' {k}link dosyası bulunamadı!{r}")
        sys.exit()
        
def gecersiz_links():
      print(rf"""{nm}╠═════════════════════════════════════╗
{mg}║      Geçersiz Linkleri Listele      ║
{nm}╠═════════════════════════════════════╣""")
      link_file = input(f"{pm}╠═══════ > Link dosya yolu: {r}")
      if not os.path.exists(link_file):
          print(f"{mn}║\n{mom}║\n{mam}╚════════════╝ '{link_file}' {k}link dosyası bulunamadı!{r}")
          sys.exit()
      uzantı = uzantı_sec()
      int_kontrol()
      links = extract_links(link_file)
      gecersiz_path = f"output/gecersiz_links.{uzantı}"
      with open(gecersiz_path, "a", encoding="utf-8") as outfile:
             for link in links:
                  durum = url_status_cek(link)
                  if durum:
                      formatted = formatla(link,uzantı,durum)
                      print(f"{k}[{r}{link}{k}]{r} >>> {durum}\n----")
                      if uzantı == "json":
                          json.dump(formatted,outfile,ensure_ascii=False)
                          outfile.write("\n")
                      else:
                          outfile.write(f"{formatted}\n")
      print(f"\n{y}Geçersiz linkler '{gecersiz_path}' dosyasına kaydedildi{r}")

def baslik_getir(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.title.string.strip() if soup.title else "(başlık yok)"
    except Exception as e:
        return f"(hata: {e})"
              
def baslık_cek():
      print(rf"""{nm}╠═════════════════════════════════════╗
{mg}║       Linklerden Başlık Çek        ║
{nm}╠═════════════════════════════════════╣""")
      link_file = input(f"{pm}╠═══════ > Link dosya yolu: {r}")
      if not os.path.exists(link_file):
          print(f"{mn}║\n{mom}║\n{mam}╚════════════╝ '{link_file}' {k}link dosyası bulunamadı{r}")
          sys.exit()
      uzantı = uzantı_sec()
      int_kontrol()
      title_yolu = f"output/titles.{uzantı}"
      links = extract_links(link_file)
      with open(title_yolu,"a",encoding="utf-8") as cıktı_file:
           for link in links:
                 baslık = baslik_getir(link)
                 formatted = formatla(link,uzantı,baslık)
                 print(f"{k}[{r}{link}{k}]{r} >>> {baslık}\n----")
                 if uzantı == "json":
                     json.dump(formatted,cıktı_file,ensure_ascii=False)
                     cıktı_file.write("\n")
                 else:
                     cıktı_file.write(f"{formatted}\n")

def kategori_elementleri():
    klasor = "output"
    kategoriler = {}
    uzantılar = (".txt", ".json", ".csv", ".xml", ".html")
    if not os.path.isdir(klasor):
        print(f"{nm}║\n║\n{mg}╠════════════╝ {k}Kategori klasörü bulunamadı!{r}")
        input(f"{mn}║\n╚══════ > Menüye dönmek için bir tuşa basın.. {r}")
        main()
    dosyalar = [dosya for dosya in os.listdir(klasor) if dosya.endswith(uzantılar)]
    if not dosyalar:
        print(f"{nm}║\n║\n{mg}╠════════════╝ {k}Kategori klasörü boş!{r}")
        input(f"{mn}║\n╚══════ > Menüye dönmek için bir tuşa basın.. {r}")
        main()
    for dosya in dosyalar:
        kategori = "_".join(os.path.splitext(dosya)[0].split("_")[:-2])
        if not kategori:  # Eğer tarih formatı yoksa tam ismi al
            kategori = os.path.splitext(dosya)[0]
        yol = os.path.join(klasor, dosya)
        try:
            with open(yol, "r", encoding="utf-8") as f:
                satirlar = [satir.strip() for satir in f if satir.strip()]
                if kategori not in kategoriler:
                    kategoriler[kategori] = 0
                kategoriler[kategori] += len(satirlar)
        except Exception as e:
            print(f"{k}Hata: {dosya} okunamadı -> {e}{r}")
    for kategori, sayi in kategoriler.items():
        print(f"{mn}╠═ {kategori.upper():<20}{r} ➜ {m}{sayi} link{r}")
    input(f"{mom}║\n╚══════ > Menüye dönmek için bir tuşa basın.. {r}")
    main()
    
def yardım():
      print(f"{nm}╠═════════════════ Yardım Menüsü ═════════════════╗")
      print(f"{nm}║ 1 - Linkleri anahtar kelimelere göre kategorilere ayırır")
      print(f"{mg}║ 2 - Ulaşılamayan linkleri kontrol eder ve listeler ")
      print(f"{pm}║ 3 - Linklerden <title> başlığını çeker")
      print(f"{mn}║ 4 - Her kategoride kaç link olduğunu gösterir")
      print(f"{mom}║ 5 - Bu yardım menüsünü gösterir")
      print(f"{mam}║ 0 - Uygulamadan çıkış yapar")
      print(f"{am}╠═════════════════════════════════════════════════╝ ")
      input(f"{cm}║\n╚══════ > Menüye dönmek için tuşlayın.. {r}")
      main()
      
def cıkıs():
     print(f"{nm}║\n║\n{mg}╚════════════╝ {k}Çıkış yapılıyor..{r}")
     sys.exit()
     
def MENU(secilmis):
      secim_haritası = {
      "0": cıkıs,
      "1": kategorize_et,
      "2": gecersiz_links,
      "3": baslık_cek,
      "4": kategori_elementleri,
      "5": yardım
      }
      func = secim_haritası.get(secilmis)
      if func:
          func()
      else:
          print(f"{nm}║\n║\n{mg}╚═══════════╝ {k}Hatalı girdi türü! Geçerli bir değer girin{r}")
      
def main():
      output_folder()
      global HTTP_HATA_MESAJLARI, timestep
      HTTP_HATA_MESAJLARI = load_hata_code()
      timestep = datetime.now().strftime("%Y%m%d_%H%M%S")
      temiz()
      banner()
      try:
          menu = input(f"""{m}╔═════════════════════════════════════╗
{m}║          NexaVista - Menü           ║
{cm}╠═════════════════════════════════════╣
{am}║ 1 - Linkleri Kategorize Et          ║
{mam}║ 2 - Geçersiz Linkleri Listele       ║
{mom}║ 3 - Linklerden Başlık Çek           ║
{mn}║ 4 - Kategori Sayılarını Göster      ║
{pm}║ 5 - Hakkında / Yardım               ║
{mg}║ 0 - Çıkış                           ║
{nm}║
{nm}║
{nm}╠═══════╝ $ {r}""")
          MENU(menu)
      except KeyboardInterrupt:
           print(f"{nm}║\n║\n{mg}╚════════════╝ {k}İşlem sonlandırıldı{r}")
      except AttributeError:
           print(f"{nm}║\n║\n{mg}╚═══════════╝ {k}Hatalı girdi türü! Geçerli bir değer girin{r}")
      except TypeError:
           print(f"{nm}║\n║\n{mg}╚═══════════╝ {k}Hatalı girdi türü! Geçerli bir değer girin{r}")
      except Exception as e:
           print(f"{nm}║\n║\n{mg}╚════════════╝ {k}Hata: {e}{r}")
if __name__ == "__main__":
   main()