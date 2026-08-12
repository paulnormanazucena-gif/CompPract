CREATE TABLE student (
	studentID	TEXT,
	name	TEXT NOT NULL,
	phoneNo	TEXT NOT NULL,
	PRIMARY KEY(studentID)
);

CREATE TABLE stall (
	stallID	INTEGER,
	stallName	TEXT NOT NULL,
	PRIMARY KEY(stallID)
);

CREATE TABLE dish (
	dishID	INTEGER,
	stallID	INTEGER,
	dishName	INTEGER,
	price	TEXT,
	availability	INTEGER,
	FOREIGN KEY(stallID) REFERENCES stall(stallID)
);

CREATE TABLE orderDish (
	studentID	TEXT,
	dishID	INTEGER,
	orderTime	TEXT,
	orderDate	TEXT,
	quantity	INTEGER,
	PRIMARY KEY(studentID,dishID,orderTime,orderDate),
	FOREIGN KEY(studentID) REFERENCES student(studentID)
);