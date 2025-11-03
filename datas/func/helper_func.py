import traceback,os,requests,json
from datetime import datetime

def output_folder():
       if not os.path.exists("output"):
           os.makedirs("output")
           
def error_log_write(e):
    if not os.path.exists("error_log"):
        os.makedirs("error_log")
    anlik = datetime.now()
    filename = f"error_log/error_log_{anlik.strftime('%d-%m-%Y_%H-%M-%S')}.txt"
    with open(filename, "a", encoding="utf-8") as er_file:
        if isinstance(e, Exception): 
            tb = traceback.extract_tb(e.__traceback__)
            if tb:
                dosya, satir, fonksiyon, kod = tb[-1]
            else:
                dosya, satir, fonksiyon, kod = ("?", "?", "?", "?")
            er_file.write(
                f"[{anlik.strftime('%d-%m-%Y %H:%M:%S')}] "
                f"HATA: {repr(e)} | Tür: {type(e).__name__}\n"
                f"Dosya: {dosya}, Satır: {satir}, Fonksiyon: {fonksiyon}, Kod: {kod}\n"
                f"{traceback.format_exc()}\n"
            )
        else: 
            er_file.write(
                f"[{anlik.strftime('%d-%m-%Y %H:%M:%S')}] HATA: {e}\n"
            )
       
def int_kontrol():
      try:
           requests.get("https://www.google.com",timeout=3)
      except requests.ConnectionError as e:
           print(f"{clr.mn}║\n║\n╚════════════╝ {clr.k}İnternet bağlantısı yok! Lütfen bağlantınızı kontrol edin.{clr.r}")
           error_log_write(e)
           sys.exit()

def load_hata_code():
      try:
           with open("datas/data/hata_codes.json","r",encoding="utf-8") as hc:
                return json.load(hc)
      except FileNotFoundError as e:
           print(f"{clr.mn}║\n║\n╚════════════╝{clr.r} 'hata_codes.json' {clr.k}hata kodu dosyası bulunamadı!{clr.r}")
           helper_func.error_log_write(e)
           sys.exit()

def load_categori(file_categori):
       try:
           with open(file_categori,"r",encoding="utf-8") as fc:
                categories = [line.strip() for line in fc if line.strip()] 
           return categories
       except FileNotFoundError as e:
            print(f"{clr.mn}║\n║\n╚════════════╝{clr.r} '{file_categori}'{clr.k} kategori dosyası bulunamadı!{clr.r}")
            helper_func.error_log_write(e)
            sys.exit()

def load_keywords(keys):
       try:
           with open(keys,"r",encoding="utf-8") as ky:
               return json.load(ky)
       except FileNotFoundError as e:
           print(f"{clr.mn}║\n║\n╚════════════╝{clr.r} '{keys}' {clr.k}dosyası bulunamadı!{clr.r}")
           helper_func.error_log_write(e)
           sys.exit()