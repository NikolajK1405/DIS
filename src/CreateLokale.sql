DROP TABLE IF EXISTS lokale;

CREATE TABLE lokale( uid char(3), kid char(3) NOT NULL, visits int,
    PRIMARY KEY (uid));


INSERT INTO lokale VALUES ('1', '001', 32);

INSERT INTO lokale VALUES ('2', '010', 50);

INSERT INTO lokale VALUES ('3', '031', 17);
