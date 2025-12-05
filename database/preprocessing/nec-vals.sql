CREATE TABLE nyc_weather_historic AS SELECT
	Location,
	"Year",
	"Month",
	"Day",
	"Hour",
	"Minute",
	"Ta" AS Temperature,
	"RH" AS Humidity
	FROM combined;