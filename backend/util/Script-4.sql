DROP EXTENSION IF EXISTS intarray;
CREATE EXTENSION intarray;
--DROP TABLE IF EXISTS booked_tours;
DROP TABLE IF EXISTS tours;
--DROP TABLE IF EXISTS tour_availability;
DROP TABLE IF EXISTS tour_routes;
DROP TABLE IF EXISTS route_points_of_interest;
--DROP TABLE IF EXISTS guide_profiles;
DROP TABLE IF EXISTS users;
--DROP TABLE IF EXISTS user_roles;


--CREATE TABLE user_roles (
--	id SERIAL PRIMARY KEY,
--	role_name VARCHAR(30) UNIQUE NOT NULL
--);

CREATE TABLE users(
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(30) NOT NULL,
	last_name VARCHAR(30),
	email VARCHAR(30) NOT NULL,
	pass BYTEA NOT NULL,
	phone VARCHAR(12) NOT NULL,
	role_name VARCHAR(20) NOT NULL,
	description VARCHAR(500) DEFAULT NULL,
	photo_url VARCHAR(100) DEFAULT NULL
--	CONSTRAINT fk_user_roles_id
--  		FOREIGN KEY (role_id) REFERENCES "user_roles" (id)
);

--CREATE TABLE guide_profiles(
--	id SERIAL PRIMARY KEY,
--	guide_id INT NOT NULL,
--	description VARCHAR(500) NOT NULL,
--	photo_url VARCHAR(100) NOT NULL,
--	CONSTRAINT fk_guide_id
--  		FOREIGN KEY (guide_id) REFERENCES "users" (id)
--);

CREATE TABLE route_points_of_interest (
	id SERIAL PRIMARY KEY,
	poi_name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE tour_routes (
	id SERIAL PRIMARY KEY,
	poi_arr INT[] NOT NULL
);

--CREATE TABLE tour_availability (
--	id SERIAL PRIMARY KEY,
--	day_name VARCHAR(10) UNIQUE NOT NULL
--);

CREATE TABLE tours(
	id SERIAL PRIMARY KEY,
	route_id INT NOT NULL,
	guide_id INT NOT NULL,
	day_of_week INT DEFAULT NULL,
	price_per_person_in_cents BIGINT NOT NULL,
	title VARCHAR(50) NOT NULL,
--	capacity INT NOT NULL,
--	duration_minutes INT NOT NULL,
	inactive BOOLEAN DEFAULT FALSE,
	CONSTRAINT fk_route_id
  		FOREIGN KEY (route_id) REFERENCES "tour_routes" (id),
  	CONSTRAINT fk_tour_guide_id
  		FOREIGN KEY (guide_id) REFERENCES "users" (id)
--  	CONSTRAINT fk_availability_id
--  		FOREIGN KEY (availability_id) REFERENCES "tour_availability" (id)
);

--CREATE TABLE booked_tours(
--	tour_id SERIAL NOT NULL,
--	user_id INT NOT NULL,
--	start_at TIMESTAMP NOT NULL,
--	start_location VARCHAR(5) NOT NULL,
--	no_of_persons INT NOT NULL,
--	user_rating INT DEFAULT NULL,
--	user_comment VARCHAR(100) DEFAULT NULL,
--	PRIMARY KEY (tour_id, user_id, start_at),
--	CONSTRAINT fk_tour_id
--  		FOREIGN KEY (tour_id) REFERENCES "tours" (id),
--  	CONSTRAINT fk_tour_user_id
--  		FOREIGN KEY (user_id) REFERENCES "users" (id)
--);

-----------------------------------------------------INSERTS----------------------------------------

--INSERT INTO user_roles (role_name) VALUES ('user'), ('guide'), ('site manager');

--INSERT INTO users (first_name, last_name, email, pass, phone, role_id) VALUES 
--	('John', 'Doe', 'jd80@a.ca', 'password','555-555-5000', 1),
--	('Jane', 'Doe', 'jd81@a.ca', 'password','555-555-5001', 1),
--	('Johny', 'Doe', 'jd03@a.ca', 'password','555-555-5002', 1),
--	('Morty', 'Christo', 'mc@a.ca', 'password','555-555-5003', 2),
--	('Vali', 'Vlad', 'vv@a.ca', 'password','555-555-5004', 2),
--	('Mahwish', NULL, 'm@a.ca', 'password','555-555-5005', 2),
--	('Grace', 'Kim', 'gk@a.ca', 'password','555-555-5006', 3);

INSERT INTO users (first_name, last_name, email, pass, phone, role_name) VALUES 
	('John', 'Doe', 'jd80@a.ca', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2','555-555-5000', 'user'),
	('Jane', 'Doe', 'jd81@a.ca', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2','555-555-5001', 'user'),
	('Johny', 'Doe', 'jd03@a.ca', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2','555-555-5002', 'user'),
	('Brian', 'Johnson', 'mc@a.ca', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2','555-555-5003', 'guide'),
	('Jenny', 'Richmond', 'vv@a.ca','$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2','555-555-5004', 'guide'),
	('Revere', 'Paully', 'm@a.ca', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2','555-555-5005', 'guide'),
	('Mason', 'Free', 'gk@a.ca', '$2b$12$k9bUr82TcF2uT27PCUs4Z.F/yYB.beSzSiaH4I0OUI0MhloqyGXf2','555-555-5006', 'site manager');

UPDATE users SET 
	description = 'Great story teller',
	photo_url = 'link to Chris photo'
	WHERE id = 4;

UPDATE users SET 
	description = 'Aspiring guide',
	photo_url = 'link to Valis photo'
	WHERE id = 5;

UPDATE users SET 
	description = 'Aspiring guide',
	photo_url = 'link to Valis photo'
	WHERE id = 6;
	
--INSERT INTO guide_profiles (guide_id, description, photo_url) VALUES 
--	(4,'Great story teller', 'link to Morty photo'),
--	(5,'Aspiring guide', 'link to Valis photo'),
--	(6,'Best traffic navigator', 'link to Mahwish photo');
	
INSERT INTO route_points_of_interest (poi_name) VALUES 
	('Statue of Liberty'),
	('Central Park'),
	('Rockefeller Center'),
	('Metropolitan Museum of Art'),
	('Broadway and the Theater District'),
	('Empire State Building'),
	('9/11 Memorial and Museum'),
	('High Line'),
	('American Museum of Natural History'),
	('Times Square'),
	('Brooklyn Bridge'),
	('Fifth Avenue');

INSERT INTO tour_routes (poi_arr) VALUES 
	('{1,2,3}'),
	('{1,3,5}'),
	(array[4,7,9,11]),
	('{1,2,7,11}');

--INSERT INTO tour_availability (day_name) VALUES
--	('Daily'), ('Mondays'), ('Tuesdays'), ('Wednesdays'), 
--	('Thursdays'), ('Fridays'), ('Saturdays'), ('Sundays');

INSERT INTO tours (route_id, guide_id, price_per_person_in_cents, title, day_of_week) VALUES 
	(1,4,9000, 'First Tour', 1),
	(2,4,9000, 'Second Tour', 2),
	(1,5,9900, 'Third Tour', 3),
	(4,5,9900, 'Fourth Tour', 4),
	(1,6,7700, 'Fifth Tour', 5),
	(4,6,7700, 'Sixth Tour', 6),
	(2,6,7700, 'Seventh Tour', 7),
	(3,6,7700, 'Eighth Tour', 6);
	
--INSERT INTO booked_tours (tour_id, user_id, start_at, start_location, no_of_persons) VALUES 
--	(8,1, '2022-08-01 16:00:00','zip01', 4);

------------------------------------------------SELECTS-------------------------------------------


SELECT poi_name 
	FROM route_points_of_interest 
	WHERE id IN(1,2,3);

SELECT poi_arr 
			FROM tour_routes  
			WHERE id = 1;

		--Example of SQL statement for dao layer get_route_name_by_route_id(self, route_id)
SELECT STRING_AGG(poi_name, '--') AS route_name
	FROM route_points_of_interest 
	WHERE array[id] <@ -- true when left array is contained in the right array
		(SELECT poi_arr 
			FROM tour_routes  
			WHERE id = 4);
		
--SELECT * FROM booked_tours;
		
--returns the string of all POI for a route that contains a specific POI here 1, and price < $80 and the tour id
SELECT STRING_AGG(poi_name, '--') AS route_name, t.id
	FROM route_points_of_interest rpoi
	JOIN tour_routes tr ON rpoi.id = ANY(tr.poi_arr)
	JOIN tours t ON t.route_id = tr.id
	WHERE idx(poi_arr,1) > 0 AND t.price_per_person_in_cents < 8000
	GROUP BY tr.id, t.id;


--Site visitors table
SELECT STRING_AGG(poi_name, '--') AS route_name,  t.title, CONCAT(u.first_name, ' ', u.last_name) AS guide_name, t.day_of_week, t.price_per_person_in_cents, t.id
	FROM route_points_of_interest rpoi
	JOIN tour_routes tr ON rpoi.id = ANY(tr.poi_arr)
	JOIN tours t ON t.route_id = tr.id
	JOIN users u ON u.id = t.guide_id
	WHERE guide_id = 4 --idx(poi_arr,1) > 0 AND t.price_per_person_in_cents < 8000
	GROUP BY  t.guide_id, t.day_of_week, t.price_per_person_in_cents, u.first_name, u.last_name, t.title, t.id;

select * from users;
select * From tours;