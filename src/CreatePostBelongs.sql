DROP TABLE IF EXISTS postBelongs; -- hjælper på test, men slet senere

CREATE TABLE IF NOT EXISTS postBelongs( uid char(3), pid char(3) NOT NULL,
    PRIMARY KEY (pid));