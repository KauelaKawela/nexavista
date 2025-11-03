import requests,os,json,re,time,sys,clr
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from datetime import datetime
from datas.func import csf,formated,urlstus,docat,helper_func
from datas.func import check_tittle as ctl
from datas.func import notfoundlinks as nfl
from os import system

def banner():
      print(f"\n{clr.am}                                    Fast"+clr.m)
      print(r"  _   _             __      ___     _   "+clr.mg+"Scan"+clr.m)
      print(r" | \ | |            \ \    / (_)   | |      "+clr.am+"Fast"+clr.m)
      print(r" |  \| | _____  ____ \ \  / / _ ___| |_ __ _    "+clr.mg+"Sort"+clr.m)
      print(r" | . ` |/ _ \ \/ / _` \ \/ / | / __| __/ _` |  ")
      print(r" | |\  |  __/>  < (_| |\  /  | \__ \ || (_| |")
      print(r" |_| \_|\___/_/\_\__,_| \/   |_|___/\__\__,_|")
      print("")
      print(f"{clr.mg}        NexaVista - v1.0 ")
      print("            Created by: github.com/KauelaKawela"+clr.r)
        
def kategori_elementleri():
    klasor = "output"
    kategoriler = {}
    uzantılar = (".txt", ".json", ".csv", ".xml", ".html")
    if not os.path.isdir(klasor):
        print(f"{clr.nm}║\n║\n{clr.mg}╠════════════╝ {clr.k}Kategori klasörü bulunamadı!{clr.r}")
        helper_func.helper_func.error_log_write("Kategori klasörü bulunamadı!")
        input(f"{clr.mn}║\n╚══════ > Menüye dönmek için bir tuşa basın.. {clr.r}")
        main()
    dosyalar = [dosya for dosya in os.listdir(klasor) if dosya.endswith(uzantılar)]
    if not dosyalar:
        print(f"{clr.nm}║\n║\n{clr.mg}╠════════════╝ {clr.k}Kategori klasörü boş!{clr.r}")
        helper_func.error_log_write("Kategori klasörü boş!")
        input(f"{clr.mn}║\n╚══════ > Menüye dönmek için bir tuşa basın.. {clr.r}")
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
            print(f"{clr.k}Hata: {dosya} okunamadı -> {e}{clr.r}")
            helper_func.error_log_write(e)
    for kategori, sayi in kategoriler.items():
        print(f"{clr.mn}╠═ {kategori.upper():<20}{clr.r} ➜ {clr.m}{sayi} link{clr.r}")
    input(f"{clr.mom}║\n╚══════ > Menüye dönmek için bir tuşa basın.. {clr.r}")
    main()
    
def yardım():
      print(f"{clr.nm}╠═════════════════ Yardım Menüsü ═════════════════╗")
      print(f"{clr.nm}║ 1 - Linkleri anahtar kelimelere göre kategorilere ayırır")
      print(f"{clr.mg}║ 2 - Ulaşılamayan linkleri kontrol eder ve listeler ")
      print(f"{clr.pm}║ 3 - Linklerden <title> başlığını çeker")
      print(f"{clr.mn}║ 4 - Her kategoride kaç link olduğunu gösterir")
      print(f"{clr.mom}║ 5 - Bu yardım menüsünü gösterir")
      print(f"{clr.mam}║ 0 - Uygulamadan çıkış yapar")
      print(f"{clr.am}╠═════════════════════════════════════════════════╝ ")
      input(f"{clr.cm}║\n╚══════ > Menüye dönmek için tuşlayın.. {clr.r}")
      main()
      
def cıkıs():
     print(f"{clr.nm}║\n║\n{clr.mg}╚════════════╝ {clr.k}Çıkış yapılıyor..{clr.r}")
     sys.exit()
     
def MENU(secilmis):
      secim_haritası = {
      "0": cıkıs,
      "1": docat.kategorize_et,
      "2": nfl.gecersiz_links,
      "3": ctl.baslık_cek,
      "4": kategori_elementleri,
      "5": yardım
      }
      func = secim_haritası.get(secilmis)
      if func:
          func()
      else:
          print(f"{clr.nm}║\n║\n{clr.mg}╚═══════════╝ {clr.k}Hatalı girdi türü! Geçerli bir değer girin{clr.r}")
          helper_func.error_log_write("Hatalı girdi türü! Geçerli bir değer girin")
      
def main():
      helper_func.output_folder()
      global HTTP_HATA_MESAJLARI, timestep
      HTTP_HATA_MESAJLARI = helper_func.load_hata_code()
      timestep = datetime.now().strftime("%Y%m%d_%H%M%S")
      system("clear||cls")
      banner()
      try:
          menu = input(f"""{clr.m}╔═════════════════════════════════════╗
{clr.m}║          NexaVista - Menü           ║
{clr.cm}╠═════════════════════════════════════╣
{clr.am}║ 1 - Linkleri Kategorize Et          ║
{clr.mam}║ 2 - Geçersiz Linkleri Listele       ║
{clr.mom}║ 3 - Linklerden Başlık Çek           ║
{clr.mn}║ 4 - Kategori Sayılarını Göster      ║
{clr.pm}║ 5 - Hakkında / Yardım               ║
{clr.mg}║ 0 - Çıkış                           ║
{clr.nm}║
{clr.nm}║
{clr.nm}╠═══════╝ $ {clr.r}""")
          MENU(menu)
      except KeyboardInterrupt as e:
           print(f"{clr.nm}║\n║\n{clr.mg}╚════════════╝ {clr.k}İşlem sonlandırıldı{clr.r}")
      except AttributeError as e:
           print(f"{clr.nm}║\n║\n{clr.mg}╚═══════════╝ {clr.k}Hatalı girdi türü! Geçerli bir değer girin{clr.r}")
           helper_func.error_log_write(e)
      except TypeError as e:
           print(f"{clr.nm}║\n║\n{clr.mg}╚═══════════╝ {clr.k}Hatalı girdi türü! Geçerli bir değer girin{clr.r}")
           helper_func.error_log_write(e)
      except Exception as e:
           print(f"{clr.nm}║\n║\n{clr.mg}╚════════════╝ {clr.k}Hata: {e}{clr.r}")
           helper_func.error_log_write(e)
           
if __name__ == "__main__":
   main()