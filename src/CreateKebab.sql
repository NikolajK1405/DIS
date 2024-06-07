drop table if exists kebabsted;

CREATE TABLE IF NOT EXISTS Kebabsted(kid char(3),
name varchar(100),
rating float,
adresse char(50),
menu varchar(100),
CONSTRAINT kebab_pk PRIMARY KEY (kid));

copy  Kebabsted(kid,name,rating,adresse,menu)
<<<<<<< HEAD
            from '/Users/nikolajkrarup/Documents/DocsNikospro/Noter/DIS/grup/DIS/tmp/kebab.csv'
            WITH (FORMAT CSV, delimiter ',',HEADER, ENCODING 'UTF8');
=======
            from 'C:\Users\Mit PC\OneDrive\Skrivebord\Library\Python\DiS\tmp\kebab.csv'
            WITH (FORMAT CSV, delimiter ',', HEADER, ENCODING 'UTF8');
>>>>>>> origin
