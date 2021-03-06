SQL queries

>>> Task 1: (system with small planets)

	select s.radius as sun_radius, p.radius as planet_radius from Star as s, Planet as p where s.kepler_id=p.kepler_id and s.radius/p.radius>1 order by s.radius desc;



>>> Task 2: (How many planets for big stars)

	select s.radius, count(p.koi_name) from Star as s, Planet as p where  s.kepler_id=p.kepler_id and s.radius>=1 group by s.kepler_id having count(p.koi_name)>1 order by s.radius desc;



>>> Task 3: (Lonely stars)

	select s.kepler_id, s.t_eff, s.radius from Star as s left outer join Planet as p using (kepler_id) where p.koi_name is null order by s.t_eff desc;



>>> Task 4: (Subquery joints stars and planets)

	select round(avg(p.t_eq),1), min(s.t_eff), max(t_eff) 
	from Star as s, Planet as p
	where s.kepler_id=p.kepler_id 
	and s.t_eff >(
  	select avg(s.t_eff) from Star as s
  	); 



>>> Task 5: (Correlated sizes?)

	select koi_name, p.radius, s.radius 
	from star as s, planet as p 
	where s.kepler_id=p.kepler_id 
	and s.radius in (
  		select radius 
  		from star 
  		order by  radius desc 
  		limit 5
	);