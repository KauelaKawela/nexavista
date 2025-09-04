import clr

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
        print(f"{clr.nm}║\n║\n{clr.mg}╚═══════════╝ {k}Hatalı seçim türü! Geçerli uzantı girin{clr.r}")
        sys.exit()