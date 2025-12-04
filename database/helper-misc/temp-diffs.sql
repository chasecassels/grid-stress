SELECT avg(a."Ta" - b."Ta")
FROM S744860 a 
INNER JOIN S725030 b 
ON a."Year" = b."Year" 
AND a."Month" = b."Month" 
AND a."Day" = b."Day" 
AND a."Minute" = b."Minute" 