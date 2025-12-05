SELECT count(*) FROM nyc_weather_historic;

SELECT min("Year"), max("Year") FROM nyc_weather_historic;

SELECT * FROM nyc_weather_historic WHERE "Minute" <> 0; --returns none (get rid of minute column)