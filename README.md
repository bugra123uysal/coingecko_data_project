Bu Python projesi, CoinGecko API'si üzerinden birçok kripto paranın fiyat, hacim, piyasa değeri ve fiyat değişim yüzdelerini (7 gün, 30 gün, 1 yıl) manuel olarak güncellenmektedir PostgreSQL veritabanına ve csv dosyasına kaydeder.

##  Toplanan Veri Özellikleri

Her coin için aşağıdaki veriler toplanır:

| Sütun Adı         | Açıklama                              |
|------------------|--------------------------------------- |
| Coin             | Kripto para adı (örnek: bitcoin)       |
| Price            | Anlık fiyat (USD)                      |
| price_change_1y  | 1 yıllık değişim (%)                   |
| price_change_30d | 30 günlük değişim (%)                  |
| price_change_7d  | 7 günlük değişim (%)                   |
| hours_24_change  | 24 saatlik değişim (%)                 |
| high             | 24 saatteki en yüksek fiyat            |
| low              | 24 saatteki en düşük fiyat             |
| volume           | 24 saatlik işlem hacmi                 |
| market_cap       | Güncel piyasa değeri                   |
| timestamp        | Verinin çekildiği tarih ve saat        |

## 🚀 Özellikler

- Anlık fiyat verisi çekme (current_price)
- 24 saatlik en yüksek, en düşük ve yüzdesel değişim verileri
- 7 gün, 30 gün ve 1 yıllık fiyat değişim yüzdeleri
- CoinGecko API kullanımı
- PostgreSQL veritabanına veri yazma
- CSV dosyasına yedekleme
- Pandas ile veri işleme
- Görselleştirme (Bar Chart, Line Plot vs.)

## kütüphane
-import pandas as pd (  veri analizi ve veri işleme için kullanılır)
-import requests  (API'sine istek göndermek ve kripto para verilerini JSON formatında almak için kullanılır)
-import time   (Programın belirli aralıklarla çalışmasını sağlamak için kullanılır.  time.sleep(60) )
-from datetime import datetime  (Anlık tarih ve saat bilgisini almak için kullanılır. ve Her veri kaydının hangi yıl, ay, gün ve saat alındığını belirlemek için datetime.now() kullanılır.)

-from sqlalchemy import create_engine  (Pandas ile doğrudan PostgreSQL veritabanına veri yazmak için create_engine() fonksiyonu kullanılır.)
-import psycopg2 (SQL sorguları yazmak, tabloları manuel kontrol etmek veya veritabanı üzerinde işlemler yapmak için kullanılır.)

## postgresSQL'e bağlanmak için
DB_HOST=localhost
DB_PORT=5432
DB_NAME=coin_db
DB_USER=postgres
DB_PASS=****


## görselleştirme
 (images/price_chart.png)
Toplanan veriler   pandas, matplotlib.pyplot , seaborn  kütüphaneleri kullanarak görselleştirildi


## 🤝 Katkıda Bulunmak
Projeye katkıda bulunmak isterseniz, pull request gönderebilir veya issue açabilirsiniz.

## 📫 İletişim
Mesut Buğra UYSAL  
📧 uysalbugra134@gmail.com  
🔗 GitHub: [github.com/bugra123uysal](https://github.com/bugra123uysal)

