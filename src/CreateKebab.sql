CREATE TABLE IF NOT EXISTS Kebabsted(kid char(3),
name char(20),
rating float,
adresse char(50),
menu char(40),
CONSTRAINT kebab_pk PRIMARY KEY (kid));

copy  Kebabsted(kid,name,rating,adresse,menu)
            from 'C:\Users\Mit PC\OneDrive\Skrivebord\Library\Python\DiS\tmp\kebab.csv'
            WITH (FORMAT CSV, delimiter ',', HEADER, ENCODING 'UTF8');
