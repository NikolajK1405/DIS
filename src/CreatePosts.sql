DROP TABLE IF EXISTS posts;

CREATE TABLE posts(pid int, title varchar(50),
    rating float, uid char(3), kid char(3),
    date char(8), status varchar(300),
    CONSTRAINT post_pk PRIMARY KEY (pid));

copy posts(pid,title,rating,uid,kid,date,status)
            from 'PATH TO/tmp/posts.csv'
            WITH (FORMAT CSV, delimiter ',',HEADER, ENCODING 'UTF8');
