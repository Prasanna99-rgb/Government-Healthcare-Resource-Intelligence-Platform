CREATE DATABASE government_healthcare;

USE government_healthcare;

COMMIT;

SELECT *
FROM healthcare_master
LIMIT 10;

#1)Which districts have the highest healthcare demand?
SELECT district,
       state,
       population_per_health_centre
FROM healthcare_master
ORDER BY population_per_health_centre DESC
LIMIT 20;

#2)Which states require the highest healthcare investment?
SELECT state,
       ROUND(AVG(population_per_health_centre),2) AS avg_pressure
FROM healthcare_master
GROUP BY state
ORDER BY avg_pressure DESC;

#3)Which districts have poor infrastructure despite high population?
SELECT district,
       state,
       population,
       health_centres,
       population_per_health_centre
FROM healthcare_master
WHERE population > (
        SELECT AVG(population)
        FROM healthcare_master
)
AND health_centres < (
        SELECT AVG(health_centres)
        FROM healthcare_master
)
ORDER BY population DESC;

#4)Which districts should receive immediate government funding?
SELECT district,
       state,
       healthcare_density,
       population_per_health_centre
FROM healthcare_master
WHERE healthcare_density='Critical'
ORDER BY population_per_health_centre DESC;

#5)Which states have the best healthcare accessibility?
SELECT state,
       ROUND(AVG(population_per_health_centre),2) accessibility
FROM healthcare_master
GROUP BY state
ORDER BY accessibility;

#6)Which districts have the best healthcare infrastructure?
SELECT district,
       health_centres,
       population_per_health_centre
FROM healthcare_master
ORDER BY population_per_health_centre
LIMIT 20;

#7)Which districts have poor vaccination coverage?
SELECT district,
       vaccination,
       state
FROM healthcare_master
ORDER BY vaccination
LIMIT 20;

#8)Which districts have the highest anaemia burden?
SELECT district,
	   state,
       anaemia
FROM healthcare_master
ORDER BY anaemia DESC
LIMIT 20;

#9)Which districts have poor maternal healthcare?
SELECT district,
	   state,
       antenatal_care,
       institutional_birth
FROM healthcare_master
ORDER BY antenatal_care
LIMIT 20;

#10)Which districts have poor child nutrition?
SELECT district,
	   state,
       stunted,
       underweight
FROM healthcare_master
ORDER BY stunted DESC;

#11)Which states have the highest female literacy?
SELECT state,
       ROUND(AVG(female_literacy),2)
FROM healthcare_master
GROUP BY state
ORDER BY AVG(female_literacy) DESC;

#12)Which districts have high literacy but low vaccination?
SELECT district,
	   state,
       literacy,
       vaccination
FROM healthcare_master
WHERE literacy > 80
AND vaccination < 70;

#13)Rank all districts based on healthcare demand.
SELECT district,
	   state,
       population_per_health_centre,
       RANK() OVER(
       ORDER BY population_per_health_centre DESC
       ) demand_rank
FROM healthcare_master;

#14)Top 5 populated districts in every state.
SELECT * FROM(
	SELECT state,
		   district,
		   population,
		   ROW_NUMBER() OVER( PARTITION BY state ORDER BY population DESC)
		   rn
		   FROM healthcare_master
		   )t 
WHERE rn<=5;

#15)Which states contribute the highest share of India's population?
SELECT state,SUM(population),
				ROUND(100*SUM(population) / (
					SELECT SUM(population)
					FROM healthcare_master ),2)
				AS contribution
				FROM healthcare_master
				GROUP BY state
ORDER BY contribution DESC;

#16)Government Healthcare Priority Classification
SELECT district,
	   population_per_health_centre,
	   CASE
			WHEN population_per_health_centre>50000 THEN 'Critical'
			WHEN population_per_health_centre>25000 THEN 'High'
			WHEN population_per_health_centre>10000 THEN 'Medium'
	   ELSE 'Low'
END priority
FROM healthcare_master;

#17)Government Recommendation Engine
SELECT district,
	   population_per_health_centre,
	   vaccination,
	   anaemia,
	   CASE
			WHEN population_per_health_centre>50000 THEN 'Build 5 PHCs'
			WHEN population_per_health_centre>30000 THEN 'Build 3 PHCs'
			WHEN vaccination<70 THEN 'Strengthen Vaccination'
			WHEN anaemia>50 THEN 'Launch Nutrition Program'
	  ELSE 'Current Infrastructure Adequate'
END recommendation
FROM healthcare_master;

#18)Find districts above their state's average population.
SELECT district,
       state,
       population
FROM healthcare_master h
WHERE population >
(
SELECT AVG(population)
FROM healthcare_master
WHERE state=h.state
);

#19)Create Healthcare Priority Index
SELECT district,
	   state,
		ROUND((population_per_health_centre/1000) + anaemia - vaccination - female_literacy,2)
AS healthcare_priority_index
FROM healthcare_master
ORDER BY healthcare_priority_index DESC;

#20)Top 5 populated districts in every state.
SELECT *
	FROM(
		SELECT state,
			   district,
			   population,
			   ROW_NUMBER() OVER( PARTITION BY state ORDER BY population DESC) rn
		FROM healthcare_master )t
WHERE rn<=5;

#21)Calculate cumulative population.
SELECT district,
	   population,
	   SUM(population) OVER( ORDER BY population DESC) running_population
FROM healthcare_master;

#22)Divide districts into four healthcare priority groups.
SELECT district,
	   population_per_health_centre,
	   NTILE(4) OVER(ORDER BY population_per_health_centre DESC) priority_group
FROM healthcare_master;
#Interpretation
#Group 1 → Highest Priority
#Group 4 → Lowest Priority

#23)Compare a district's population with the previous district within the same state.
SELECT district,
	   state,
	   population,
	   LAG(population) OVER(PARTITION BY state ORDER BY population DESC) previous_population
FROM healthcare_master;

#24)Which are the Top 20 districts requiring immediate government intervention?
WITH healthcare_score AS (
	SELECT district,
		   state,
		   population_per_health_centre,
		   vaccination,
		   anaemia,
		  ((population_per_health_centre/1000) + anaemia - vaccination) AS healthcare_priority_index
FROM healthcare_master
)
SELECT district,
	   state,
	   ROUND(healthcare_priority_index,2),
	   RANK() OVER(ORDER BY healthcare_priority_index DESC) priority_rank
FROM healthcare_score
LIMIT 20;

#25)Which states have the lowest healthcare coverage?
SELECT
    state,
    SUM(health_centres) AS total_health_centres,
    SUM(population) AS total_population,
    ROUND(SUM(population)/SUM(health_centres),2) AS people_per_health_centre
FROM healthcare_master
GROUP BY state
HAVING SUM(health_centres)>0
ORDER BY people_per_health_centre DESC;

#26)Which districts have more than double the national average population per health centre?
SELECT
    district,
    state,
    population_per_health_centre
FROM healthcare_master
WHERE population_per_health_centre >
(
SELECT AVG(population_per_health_centre)*2
FROM healthcare_master
);

#27)Which states have the highest average vaccination coverage?
SELECT
    state,
    ROUND(AVG(vaccination),2) avg_vaccination
FROM healthcare_master
GROUP BY state
ORDER BY avg_vaccination DESC;

#28)Which states have the worst anaemia problem?
SELECT
    state,
    ROUND(AVG(anaemia),2) avg_anaemia
FROM healthcare_master
GROUP BY state
ORDER BY avg_anaemia DESC;

#29)Which districts perform better than the national average in all health indicators?
SELECT
    district,
    state
FROM healthcare_master
WHERE vaccination >
(
SELECT AVG(vaccination)
FROM healthcare_master
)
AND anaemia <
(
SELECT AVG(anaemia)
FROM healthcare_master
)
AND female_literacy >
(
SELECT AVG(female_literacy)
FROM healthcare_master
);

#30)Which districts have low health centres and poor literacy?
SELECT district,
	   state,
	   health_centres,
	   literacy
FROM healthcare_master
WHERE health_centres<5
AND literacy<70;

#31)Top 10 districts with highest health insurance coverage
SELECT district,
	   state,
	   health_insurance
FROM healthcare_master
ORDER BY health_insurance DESC
LIMIT 10;

#32)Which districts require women's health awareness campaigns?
SELECT district, 
	   state,
	   female_literacy,
	   anaemia
FROM healthcare_master
WHERE female_literacy<70
AND anaemia>50;

#33)Which districts have excellent healthcare infrastructure but poor maternal care?
SELECT district,
	   state,
	   health_centres,
	   antenatal_care,
	   institutional_birth
FROM healthcare_master
WHERE health_centres>( SELECT AVG(health_centres) FROM healthcare_master) AND antenatal_care<60;

#34)Which states have the highest average healthcare rank?
SELECT state,
	ROUND(AVG(healthcare_rank),2) avg_rank
FROM healthcare_master
GROUP BY state
ORDER BY avg_rank;

#35)Which districts have above-average health centres but below-average vaccination?
SELECT district,
	   state,
	   health_centres,
	   vaccination
FROM healthcare_master
WHERE health_centres >( SELECT AVG(health_centres) FROM healthcare_master) AND vaccination < ( SELECT AVG(vaccination) FROM healthcare_master
);

#36)Which states have the best institutional birth rates?
SELECT state,
	ROUND(AVG(institutional_birth),2) avg_birth
FROM healthcare_master
GROUP BY state
ORDER BY avg_birth DESC;

#37)Which districts should receive additional healthcare workers?
SELECT district,
	   state,
	   population,
	   health_centres,
	   population_per_health_centre
FROM healthcare_master
WHERE population_per_health_centre>40000
ORDER BY population_per_health_centre DESC;

#38)Which districts have balanced healthcare performance?
SELECT district,
	   state,
	   vaccination,
	   anaemia,
	   female_literacy
	FROM healthcare_master
	WHERE vaccination>80
	AND anaemia<40
AND female_literacy>80;

#39)Which states have the greatest gap between literacy and female literacy?
SELECT state,
	   ROUND(AVG(literacy-female_literacy),2) literacy_gap
	   FROM healthcare_master
GROUP BY state
ORDER BY literacy_gap DESC;

#40)Executive Summary Query
SELECT COUNT(*) total_districts,
	   COUNT(DISTINCT state) total_states,
	   SUM(population) total_population,
	   SUM(health_centres) total_health_centres,
	   ROUND(AVG(literacy),2) avg_literacy,
	   ROUND(AVG(vaccination),2) avg_vaccination,
	   ROUND(AVG(anaemia),2) avg_anaemia
FROM healthcare_master;