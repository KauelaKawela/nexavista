def classify(link, keywords):
    for kategori, kelimeler in keywords.items():
        for kelime in kelimeler:
            if kelime.lower() in link.lower():
                return kategori
    return "Bilinmiyor"
