# 🌐 NexaVista

**NexaVista**, bağlantı (link) listelerini analiz ederek her bir bağlantının **durum kodunu**, **erişilebilirliğini** ve **içerik türünü** kontrol eden terminal tabanlı bir Python uygulamasıdır. Ayrıca bağlantıları işlevlerine göre sınıflandırmak üzere geliştirilebilir bir altyapıya sahiptir.

## 🚀 Özellikler

- 🔎 HTTP/HTTPS bağlantılarını kontrol eder (200, 404, 403, vb.).
- ⚙️ Bağlantıların içeriğini tarayarak **kategori sınıflandırması** (örnek: alışveriş, haber, eğitim, vs.).
- 📂 Linkleri dosya içinden okuma ve çıktıyı JSON formatında kaydetme.
- 💡 Geliştirilebilir anahtar kelime sistemi ile özelleştirilebilir sınıflandırma.
- 📊 Bağlantıların başarı/başarısız durumlarına göre istatistiksel raporlama.

## 📦 Gereksinimler

- Python 3.x
- Gerekli kütüphaneler:
  ```bash
  pip install requests beautifulsoup4

## Kullanım
```bash
git clone https://github.com/KauelaKawela/nexavista
cd nexavista
python3 nexavista.py
```


# 🌐 NexaVista

**NexaVista** is a terminal-based Python tool designed to analyze and classify a list of web links based on their **HTTP status codes**, **reachability**, and **content type**. It also supports intelligent keyword-based **categorization** of URLs.

## 🚀 Features

- 🔎 Checks HTTP/HTTPS links for accessibility (e.g., 200, 404, 403, etc.).
- 🧠 Classifies links into categories (e.g., shopping, news, education).
- 📂 Reads links from a `.txt` file and saves results as `.json`.
- ⚙️ Customizable keyword system for defining new categories.
- 📊 Displays summary statistics after analysis.

## 📦 Requirements

- Python 3.x
- Required libraries:
  ```bash
  pip install requests beautifulsoup4

## Installation
```bash
git clone https://github.com/KauelaKawela/nexavista
cd nexavista
python3 nexavista.py
```