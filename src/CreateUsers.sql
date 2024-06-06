DROP TABLE IF EXISTS users; -- hjælper på test, men slet senere

CREATE TABLE IF NOT EXISTS users( uid char(3), username char(20) NOT NULL,
    password char(20) NOT NULL, kebabnum int,
    CONSTRAINT user_pk PRIMARY KEY (uid));


-- (chat)
INSERT INTO users VALUES ('001', 'tis', 'mand', 23);

INSERT INTO users VALUES ('002', 'simon', 'sion', 100);
