SELECT sub.* 			# with * it retrieves all columns from a table and creates a subquery names sub
      FROM (
            SELECT *
              FROM sf_crime_incidents_2014_01
             WHERE descript = 'WARRANT ARREST'
           ) sub
     WHERE sub.resolution = 'NONE'

---------------------------------------------------------------------------------------------------------------

SELECT sub.ID1, sub.descript, sub.resolution	#it retrieves three columns and creates a subquery called sub
      FROM (
            SELECT *
              FROM sf_crime_incidents_2014_01
             WHERE descript = 'WARRANT ARREST'	#inner query
           ) sub				# it locates the result in sub
     WHERE sub.resolution = 'NONE'		#outer query

----------------------------------------------------------------------------------------------------------

SELECT *
FROM sf_crime_incidents_2014_01
WHERE ID1 IN (
    SELECT ID1
    FROM sf_crime_incidents_2014_01
    WHERE descript = 'WARRANT ARREST'
)
AND resolution = 'NONE';

-------------------------------------------------------------------------------------------------------------

SELECT ID1, descript, resolution		#it does not create a subquery
FROM sf_crime_incidents_2014_01
WHERE ID1 IN (
    SELECT ID1
    FROM sf_crime_incidents_2014_01
    WHERE descript = 'WARRANT ARREST'
)						#it just displays the result without creating the subquery
AND resolution = 'NONE';
