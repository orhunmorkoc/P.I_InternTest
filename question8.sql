
WITH MedianValues AS (
    SELECT 
        country,
        PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY daily_vaccinations) AS median_vaccination
    FROM 
        country_vaccination_stats
    WHERE 
        daily_vaccinations IS NOT NULL
    GROUP BY 
        country
),
FilledData AS (
    SELECT 
        cvs.country,
        cvs.date,
        CASE 
            WHEN cvs.daily_vaccinations IS NOT NULL THEN cvs.daily_vaccinations
            WHEN mv.median_vaccination IS NOT NULL THEN mv.median_vaccination
            ELSE 0
        END AS daily_vaccinations,
        cvs.vaccines
    FROM 
        country_vaccination_stats cvs
    LEFT JOIN 
        MedianValues mv ON cvs.country = mv.country
)
SELECT * FROM FilledData;
