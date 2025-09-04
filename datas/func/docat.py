import clr,os,sys
from datas.func import usec,helper_func,extract,urlstus,csf,wltf

def kategorize_et():
      print(rf"""{clr.nm}╠═════════════════════════════════════╗
{clr.mg}║       Linkleri Kategorize Et        ║
{clr.nm}╠═════════════════════════════════════╣""")
      link_file = input(f"{clr.pm}╠═══════ > Link dosya yolu: {clr.r}")
      if not os.path.exists(link_file):
          print(f"{clr.mn}║\n{clr.mom}║\n{clr.mam}╚════════════╝ '{link_file}' {clr.k}link dosyası bulunamadı{clr.r}")
          helper_func.error_log_write("link dosyası bulunamadı")
          sys.exit()
      uzantı = usec.uzantı_sec()
      helper_func.int_kontrol()
      keywords = helper_func.load_keywords("datas/data/keywords.json")
      links = extract.extract_links(link_file)
      for link in links:
            durum = urlstus.url_status_cek(link)
            kategori = csf.classify(link, keywords)
            wltf.wltf(link, kategori,uzantı,durum)
            if durum:
                print(f"{clr.k}[{clr.r}{kategori}{clr.k}]{clr.r} >>> {link} >>> {durum}\n----")
            else:
                print(f"{clr.k}[{clr.r}{kategori}{clr.k}]{clr.r} >>> {link}\n----")
      input(f"{clr.mn}║\n║\n╚════════════╝Menüye dönmek için herhangi bir tuşa basın")
      main()