DROP TABLE IF EXISTS posts; -- hjælper på test, men slet senere

CREATE TABLE IF NOT EXISTS posts(pid char(3), title varchar(25),
    rating float, uid char(3), kid char(3),
    date char(8), status varchar(300),
    CONSTRAINT post_pk PRIMARY KEY (pid));

