SELECT sub.month_incidents, sub.category
	FROM ( 
	SELECT *	

	FROM sf_crime_incidents_2014_01
	WHERE AVG(incidnt_num) AS avg_incidents
)
WHERE category



SELECT sub.category_incidents, AVG(sub.incidnt_num) AS sub.avg_incidents
	FROM ( 
	SELECT category, date, COUNT(*) AS  sub.avg_incidents
	FROM sf_crime_incidents_2014_01
) AS  sub.avg_incidents


SELECT sub.category, AVG(incidnt_num) AS avg_incidents
FROM (
	SELECT MONTH(date) as month_num, COUNT(*) AS avg_incidents, category
	FROM sf_crime_incidents_2014_01
	GROUP BY category, MONTH(date)
) AS sub
GROUP BY sub.category;
