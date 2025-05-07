Data was retrieved from CoinGecko API and saved to csv file 
Bu Python projesi, CoinGecko API'si üzerinden birçok kripto paranın fiyat, hacim, piyasa değeri ve fiyat değişim yüzdelerini (7 gün, 30 gün, 1 yıl) belirli aralıklarla alarak PostgreSQL veritabanına kaydeder.

---

## 🚀 Özellikler

- Anlık fiyat verisi çekme (`current_price`)
- 24 saatlik en yüksek, en düşük ve yüzdesel değişim verileri
- 7 gün, 30 gün ve 1 yıllık fiyat değişim yüzdeleri
- CoinGecko API kullanımı
- Verilerin PostgreSQL veritabanına otomatik aktarımı
- CSV dosyasına yedekleme (append modunda)
