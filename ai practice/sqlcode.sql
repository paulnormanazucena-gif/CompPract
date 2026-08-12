CREATE TABLE student (
	studentID	TEXT,
	name	TEXT,
	phoneNo	TEXT,
	PRIMARY KEY(studentID)
);

CREATE TABLE category (
	categoryID	TEXT,
	categoryName	TEXT,
	PRIMARY KEY(categoryID)
);

CREATE TABLE equipment (
	equipID	TEXT,
	categoryID	TEXT,
	equipName	TEXT,
	brand	TEXT,
	availability	INTEGER,
	PRIMARY KEY(equipID),
	FOREIGN KEY(categoryID) REFERENCES category(categoryID)
);


CREATE TABLE loanRecord (
	studentID	INTEGER,
	equipID	INTEGER,
	loanDate	TEXT,
	returnDate	TEXT,
	quantity	INTEGER,
	PRIMARY KEY(studentID,equipID),
	FOREIGN KEY(studentID) REFERENCES student(studentID),
	FOREIGN KEY(equipID) REFERENCES equipment(equipID)
);