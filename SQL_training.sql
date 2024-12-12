SELECT LEFT (Portal_rodents_19772002.plot) AS Total_plot
FROM Portal_rodents_19772002 as Each_plot
SELECT
	Each_plot.plot, CountOfrecordID.recordID
	Each_plot/CountOfrecordID = EachID
FROM
	(
	Portal_rodents_19772002 
	INNER JOIN PortalMammals_plots ON Portal_rodents_19772002.plot = PortalMammals_plots.PlotID
	)


SELECT
	Portal_rodents_19772002.plot, 
	Portal_rodents_19772002.yr, 
	Count(Portal_rodents_19772002.recordID) AS CountOfrecordID
FROM 
	(
	Portal_rodents_19772002 
	INNER JOIN PortalMammals_plots ON Portal_rodents_19772002.plot = PortalMammals_plots.PlotID
	)
	INNER JOIN PortalMammals_species ON Portal_rodents_19772002.species = 	PortalMammals_species.new_code
GROUP BY Portal_rodents_19772002.plot, Portal_rodents_19772002.yr
HAVING (((Portal_rodents_19772002.plot)=1));



SELECT DISTINCT Each_plot.plot
FROM Portal_rodents_19772002 AS Each_plot;
