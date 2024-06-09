DROP TABLE IF EXISTS posts; -- hjælper på test, men slet senere

CREATE TABLE IF NOT EXISTS posts(pid char(3), title varchar(25),
    rating float, uid char(3), kid char(3),
    date char(8), status varchar(300),
    CONSTRAINT post_pk PRIMARY KEY (pid));

-- (chat)
INSERT INTO posts VALUES ('1', 'dk doner',2.5, '2', '1','07/06-24', 'Jeg fik en pita med kebab, den var lidt tør...');

