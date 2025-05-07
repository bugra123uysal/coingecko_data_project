SELECT * FROM crypto_prices ;

SELECT "Price" FROM crypto_prices ORDER BY "Price" DESC
SELECT "Price" FROM  crypto_prices ORDER BY "Price" ASC

SELECT "market_cap" FROM crypto_prices ORDER BY "market_cap" DESC
SELECT "market_cap" FROM "crypto_price" ORDER BY "market_cap" ASC



SELECT "Date" FROM "crypto_prices" order by "Date" ASC 

SELECT "Date",
EXTRACT(YEAR FROM "Date")AS year,
EXTRACT(MONTH FROM "Date" )AS month,
EXTRACT(DAY FROM "Date") AS day
FROM "crypto_prices"
ORDER BY "Date" ASC






