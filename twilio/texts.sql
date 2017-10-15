CREATE DATABASE specially;
CREATE ROLE Alice WITH LOGIN;
GRANT INSERT ON specially TO Alice;
CREATE TABLE messages(

 id serial PRIMARY KEY,
 number varchar(12)NOT NULL, 
 datetime timestamp NOT NULL,
 
 occasion varchar(50), 
 message varchar(280), 
 giphyurl varchar(50) 
);
	
