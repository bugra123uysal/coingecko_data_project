Data was retrieved from CoinGecko API and saved to csv file 
<<<<<<< HEAD
Bu Python projesi, CoinGecko API'si üzerinden birçok kripto paranın fiyat, hacim, piyasa değeri ve fiyat değişim yüzdelerini (7 gün, 30 gün, 1 yıl) belirli aralıklarla alarak PostgreSQL veritabanına kaydeder.

---

## 🚀 Özellikler

- Anlık fiyat verisi çekme (`current_price`)
- 24 saatlik en yüksek, en düşük ve yüzdesel değişim verileri
- 7 gün, 30 gün ve 1 yıllık fiyat değişim yüzdeleri
- CoinGecko API kullanımı
- Verilerin PostgreSQL veritabanına otomatik aktarımı
- CSV dosyasına yedekleme (append modunda)
=======

Data was retrieved from CoinGecko API and saved to csv file Bu Python projesi, CoinGecko API'si üzerinden birçok kripto paranın fiyat, hacim, piyasa değeri ve fiyat değişim yüzdelerini (7 gün, 30 gün, 1 yıl) belirli aralıklarla alarak PostgreSQL veritabanına kaydeder.

🚀 Özellikler
Anlık fiyat verisi çekme (current_price)
24 saatlik en yüksek, en düşük ve yüzdesel değişim verileri
7 gün, 30 gün ve 1 yıllık fiyat değişim yüzdeleri
CoinGecko API kullanımı
Verilerin PostgreSQL veritabanına otomatik aktarımı
CSV dosyasına yedekleme (append modunda)



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
>>>>>>> 738b43c ( Description of columns in the data set)
