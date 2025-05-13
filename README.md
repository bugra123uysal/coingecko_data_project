Bu Python projesi, CoinGecko API'si üzerinden birçok kripto paranın fiyat, hacim, piyasa değeri ve fiyat değişim yüzdelerini (7 gün, 30 gün, 1 yıl) belirli aralıklarla alarak PostgreSQL veritabanına ve csv dosyasına kaydeder.

Toplanan Veriler
Her coin için aşağıdaki veriler toplanır:

Coin: Kripto para adı (örneğin "bitcoin")

Price: Anlık USD fiyatı

price_change_1y: 1 yıllık fiyat değişimi (%)

price_change_30d: 30 günlük fiyat değişimi (%)

price_change_7d: 7 günlük fiyat değişimi (%)

hours_24_change: 24 saatlik fiyat değişimi (%)

high: 24 saatteki en yüksek fiyat

low: 24 saatteki en düşük fiyat

volume: 24 saatlik işlem hacmi

market_cap: Güncel piyasa değeri

## 🚀 Özellikler

- Anlık fiyat verisi çekme (`current_price`)
- 24 saatlik en yüksek, en düşük ve yüzdesel değişim verileri
- 7 gün, 30 gün ve 1 yıllık fiyat değişim yüzdeleri
- CoinGecko API kullanımı
- Verilerin PostgreSQL veritabanına otomatik aktarımı
- CSV dosyasına yedekleme (append modunda)
-pgAdmin4 kullanılıyor

## kütüphane
-import pandas as pd (  veri analizi ve veri işleme için kullanılır)
-import requests  (API'sine istek göndermek ve kripto para verilerini JSON formatında almak için kullanılır)
-import time   (Programın belirli aralıklarla çalışmasını sağlamak için kullanılır.  time.sleep(60) )
-from datetime import datetime  (Anlık tarih ve saat bilgisini almak için kullanılır. ve Her veri kaydının hangi yıl, ay, gün ve saat alındığını belirlemek için datetime.now() kullanılır.)

-from sqlalchemy import create_engine  (Pandas ile doğrudan PostgreSQL veritabanına veri yazmak için create_engine() fonksiyonu kullanılır.)
-import psycopg2 (SQL sorguları yazmak, tabloları manuel kontrol etmek veya veritabanı üzerinde işlemler yapmak için kullanılır.)


