CREATE TABLE Clubs(
    Club_ID NUMBER(10) Primary key,
    Team_name CHAR(50) not null,
    Stadium_name CHAR(50) not null,
    Capacity NUMBER(10),
    Community NUMBER(10),
    Foundation DATE not null
);
CREATE TABLE Stats(
    Stat_ID NUMBER(10) Primary key,
    Goals NUMBER(20),
    Matches NUMBER(20),
    Minutes NUMBER(20),
    Yellow_Card NUMBER(20),
    Red_Card NUMBER(20)
);
CREATE TABLE Players(
    Player_ID NUMBER(10) Primary key,
    Name CHAR(50) not null,
    Club_ID NUMBER(10),
    Date_of_Birth DATE not null,
    Weight NUMBER(3),
    Number_team NUMBER(2) not null,
    Position CHAR(50) not null,
    Stat_ID NUMBER(10),
    CONSTRAINT stat_fk FOREIGN KEY (Stat_ID) REFERENCES Stats (Stat_ID),
    CONSTRAINT club_fk FOREIGN KEY (Club_ID) REFERENCES Clubs (Club_ID)
);
CREATE TABLE Calendars(
    Calendar_ID NUMBER(10) Primary key,
    Day_Encounter DATE not null,
    Local_Team NUMBER(10),
    Foraign_Team NUMBER(10),
    Local_Goals NUMBER(2) not null,
    Foraign_Goals NUMBER(2) not null,
    CONSTRAINT l_team_fk FOREIGN KEY (Local_Team) REFERENCES Clubs (Club_id),
    CONSTRAINT f_team_fk FOREIGN KEY (Foraign_Team) REFERENCES Clubs (Club_id)
);