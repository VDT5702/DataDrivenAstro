SQL Queries



>>> Task 1: (Adding Stars)

	insert into Star (kepler_id, t_eff, radius) values (7115384, 3789, 27.384), (8106973, 5810, 0.811), (9391817,6200,0.958);



>>> Task 2: (A messed up table)

	update Planet
	set kepler_name=NULL
	where NOT status = 'CONFIRMED';

	delete from Planet
	where radius < 0; 


>>> Task 3: (Make your own table)

	create table Planet ( 
  		kepler_id INTEGER NOT NULL,
  		koi_name VARCHAR(15) NOT NULL UNIQUE,
  		kepler_name VARCHAR(15),
  		status VARCHAR(20) NOT NULL,
  		radius FLOAT NOT NULL);
  
	insert into Planet
	values
	(6862328, 'K00865.01', NULL, 'CANDIDATE', 119.021),
	(10187017, 'K00082.05', 'Kepler-102 b','CONFIRMED',5.286),
	(10187017, 'K00082.04', 'Kepler-102 c','CONFIRMED',7.071);



>>> Task 4: (DIY exoplanet archive)

	create table Star (
  		kepler_id INTEGER PRIMARY KEY,
  		t_eff INTEGER NOT NULL,
  		radius FLOAT NOT NULL);
 
	create table Planet (
  		kepler_id INTEGER REFERENCES Star (kepler_id),
  		koi_name VARCHAR(20) PRIMARY KEY,
  		kepler_name VARCHAR(20),
  		status VARCHAR(20) NOT NULL,
  		period FLOAT,
  		radius FLOAT,
  		t_eq INTEGER);
  
	copy Star (kepler_id, t_eff, radius) from 'stars.csv' CSV;

	copy Planet (kepler_id, koi_name, kepler_name, status, period, radius, t_eq) from 'planets.csv' CSV;



>>> Task 5: (Star Coordinates)


	delete from Star;

	alter table Star
	add column ra FLOAT,
	add column decl FLOAT;

	copy Star(kepler_id, t_eff, radius, ra, decl)
	from 'stars_full.csv' CSV;




