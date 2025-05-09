SELECT * FROM crypto_prices ;

SELECT "Price" FROM crypto_prices ORDER BY "Price" DESC
SELECT "Price" FROM  crypto_prices ORDER BY "Price" ASC

SELECT "market_cap" FROM crypto_prices ORDER BY "market_cap" DESC
SELECT "market_cap" FROM crypto_prices ORDER BY "market_cap" ASC

SELECT "hours_24_change" FROM crypto_prices ORDER BY "hours_24_change" DESC
SELECT "hours_24_change" FROM crypto_prices ORDER BY "hours_24_change" ASC

SELECT "price_change_30d" FROM crypto_prices ORDER BY "price_change_30d" DESC
SELECT "price_change_30d" FROM crypto_prices  ORDER BY "price_change_30d"  ASC

SELECT "Date" FROM "crypto_prices" order by "Date" ASC 

SELECT "Coin", "Price", "market_cap" "hours_24_change"  FROM crypto_prices

SELECT "hours_24_change"  FROM crypto_prices WHERE hours_24_change > 0  ORDER BY hours_24_change DESC
SELECT "hours_24_change"  FROM crypto_prices WHERE hours_24_change > 0 ORDER BY hours_24_change ASC

SELECT "hours_24_change" FROM crypto_prices WHERE hours_24_change < 0 ORDER BY hours_24_change ASC
SELECT "hours_24_change" FROM crypto_prices WHERE hours_24_change < 0 ORDER BY hours_24_change DESC
 
SELECT "Date",
EXTRACT(YEAR FROM "Date")AS year,
EXTRACT(MONTH FROM "Date" )AS month,
EXTRACT(DAY FROM "Date") AS day
FROM "crypto_prices"
ORDER BY "Date" ASC






