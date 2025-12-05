CREATE TABLE nyc_weather_historic AS SELECT
	"Year",
	"Month",
	"Day",
	"Hour",
	"Minute",
	"Ta" AS Temperature,
	"RH" AS Humidity
	FROM combined;