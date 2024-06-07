DROP TABLE IF EXISTS postAbout; -- hjælper på test, men slet senere

CREATE TABLE IF NOT EXISTS postAbout( pid char(3), kid char(3) NOT NULL,
    PRIMARY KEY (pid));