CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    role INTEGER NOT NULL
);

CREATE TABLE Courses (
    id SERIAL PRIMARY KEY,
    name TEXT,
    holes INTEGER,
    link TEXT
);

CREATE TABLE Reviews (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users,
    course_id INTEGER REFERENCES Courses,
    rating INTEGER,
    comment TEXT,
    sent_at TIMESTAMP
);

CREATE TABLE CoursePrices (
    id SERIAL PRIMARY KEY,
    course_id INTEGER REFERENCES Courses,
    key TEXT,
    value INTEGER
);

CREATE TABLE CourseLocations (
    id SERIAL PRIMARY KEY,
    course_id INTEGER REFERENCES Courses,
    address TEXT,
    latitude DECIMAL,
    longitude DECIMAL,
    municipality TEXT,
    distance INTEGER,
    drive_time INTEGER
);