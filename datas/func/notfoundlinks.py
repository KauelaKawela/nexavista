import clr,sys,os
from datas.func import usec,formated,helper_func,extract,urlstus

def gecersiz_links():
      print(rf"""{clr.nm}╠═════════════════════════════════════╗
{clr.mg}║      Geçersiz Linkleri Listele      ║
{clr.nm}╠═════════════════════════════════════╣""")
      link_file = input(f"{clr.pm}╠═══════ > Link dosya yolu: {clr.r}")
      if not os.path.exists(link_file):
          print(f"{clr.mn}║\n{clr.mom}║\n{mam}╚════════════╝ '{link_file}' {clr.k}link dosyası bulunamadı!{clr.r}")
          sys.exit()
      uzantı = usec.uzantı_sec()
      helper_func.int_kontrol()
      links = extract.extract_links(link_file)
      gecersiz_path = f"output/gecersiz_links.{uzantı}"
      with open(gecersiz_path, "a", encoding="utf-8") as outfile:
             for link in links:
                  durum = urlstus.url_status_cek(link)
                  if durum:
                      formatted = formated.formatla(link,uzantı,durum)
                      print(f"{clr.k}[{clr.r}{link}{clr.k}]{clr.r} >>> {durum}\n----")
                      if uzantı == "json":
                          json.dump(formatted,outfile,ensure_ascii=False)
                          outfile.write("\n")
                      else:
                          outfile.write(f"{formatted}\n")
      print(f"\n{clr.y}Geçersiz linkler '{gecersiz_path}' dosyasına kaydedildi{clr.r}")