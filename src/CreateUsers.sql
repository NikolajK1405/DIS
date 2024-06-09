DROP TABLE IF EXISTS users;

CREATE TABLE users( uid char(3), username char(20) NOT NULL,
    password char(20) NOT NULL, kebabnum int,
    CONSTRAINT user_pk PRIMARY KEY (uid));


-- (chat)
INSERT INTO users VALUES ('1', 'Simon', 'KebabLover', 1200);

INSERT INTO users VALUES ('2', 'Emil', 'kebab4Eva', 55);

INSERT INTO users VALUES ('3', 'Nikolaj', 'YayKebab', 333);
