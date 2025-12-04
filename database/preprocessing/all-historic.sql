CREATE TABLE combined AS
SELECT
	*,
	'LaGuardia' AS Location
FROM
	S725030
UNION ALL 
		SELECT
	*,
	'CentralPark' AS Location
FROM
	S725033
UNION ALL 
		SELECT
	*,
	'JFK' AS Location
FROM
	S744860

	
	
	
