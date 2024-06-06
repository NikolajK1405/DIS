CREATE TABLE IF NOT EXISTS Kebabsted(kid char(3),
name char(20),
rating float,
adresse char(50),
menu char(40),
CONSTRAINT kebab_pk PRIMARY KEY (kid));

copy  Kebabsted(kid,name,rating,adresse,menu)
            from '/Users/nikolajkrarup/Documents/DocsNikospro/Noter/DIS/grup/DIS/tmp/kebab.csv'
            delimiter ','
            CSV HEADER;
