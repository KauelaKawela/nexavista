import clr,requests,os
from datas.func import usec,formated,extract,helper_func
from bs4 import BeautifulSoup

def baslik_getir(url):
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup.title.string.strip() if soup.title else "(başlık yok)"
    except Exception as e:
        return f"(hata: {e})"
        
def baslık_cek():
      print(rf"""{clr.nm}╠═════════════════════════════════════╗
{clr.mg}║       Linklerden Başlık Çek        ║
{clr.nm}╠═════════════════════════════════════╣""")
      link_file = input(f"{clr.pm}╠═══════ > Link dosya yolu: {clr.r}")
      if not os.path.exists(link_file):
          print(f"{clr.mn}║\n{clr.mom}║\n{clr.mam}╚════════════╝ '{link_file}' {clr.k}link dosyası bulunamadı{clr.r}")
          sys.exit()
      uzantı = usec.uzantı_sec()
      helper_func.int_kontrol()
      title_yolu = f"output/titles.{uzantı}"
      links = extract.extract_links(link_file)
      with open(title_yolu,"a",encoding="utf-8") as cıktı_file:
           for link in links:
                 baslık = baslik_getir(link)
                 formatted = formated.formatla(link,uzantı,baslık)
                 print(f"{clr.k}[{clr.r}{link}{clr.k}]{clr.r} >>> {baslık}\n----")
                 if uzantı == "json":
                     json.dump(formatted,cıktı_file,ensure_ascii=False)
                     cıktı_file.write("\n")
                 else:
                     cıktı_file.write(f"{formatted}\n")