DROP TABLE IF EXISTS lokale; -- hjælper på test, men slet senere

CREATE TABLE IF NOT EXISTS lokale( uid char(3), kid char(3) NOT NULL,
    PRIMARY KEY (uid));