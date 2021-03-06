SQL queries


>>> Task1: (Large Stars)
	
	select radius, t_eff from Star where radius > 1;



>>> Task 2: (Range of Hot stars)

	select kepler_id, t_eff from Star where t_eff BETWEEN 5000 AND 6000;



>>> Task 3: (Confirmed Exoplanets)

	select kepler_name, radius from Planet where status='CONFIRMED' AND radius BETWEEN 1 AND 3;



>>> Task 4: (Planet Statistics)

	select min(radius), max(radius), avg(radius), stddev(radius) from Planet where kepler_name IS NULL



>>> Task 5: (Planets in multi-planet systems)

	select kepler_id, count(koi_name) from Planet group by kepler_id having count(koi_name)>1 order by count(koi_name) desc;



