import requests,time

HTTP_HATA_MESAJLARI = {}

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