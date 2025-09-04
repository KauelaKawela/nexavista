import clr,re
from datas.func import helper_func,formated
from datetime import datetime

def wltf(link, kategori, uzantı, durum=None):
    timestep = datetime.now().strftime("%Y%m%d_%H%M%S")
    try:
        if not link.startswith("http://") and not link.startswith("https://"):
            link = "https://" + link
        kategori = re.sub(r'[^\w\-_.]', '_', kategori)
        filename = f"output/{kategori}_{timestep}.{uzantı.lstrip('.')}"
        formatted = formated.formatla(link, uzantı, durum)
        with open(filename, "a", encoding="utf-8") as wf:
            if uzantı == "json":
                json.dump(formatted, wf, ensure_ascii=False)
                wf.write("\n")
            else:
                wf.write(f"{formatted}\n")
    except Exception as e:
        print(f"'{kategori}' {clr.k}kategorisine ait link dosyaya yazılamadı: {clr.r}{e}")
        helper_func.error_log_write(e)