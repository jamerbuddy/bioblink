
# BioBlink
## Prerequisites
- [Python](https://www.python.org/downloads/)
- [MySQL](https://dev.mysql.com/downloads/installer/)


## Setup (Windows)

Setup virtual environment
```
$ cd bioblink
$ py -3 -m venv venv
$ venv/Scripts/activate
```

Install flask and dependencies
```
$ py -m pip install Flask
$ py -m pip install flask-mysqldb
$ py -m pip install flask-cors
```

Run flask app
```
$ export FLASK_APP=hello.py
$ export FLASK_ENV=development
$ py -m flask run
```

Endpoints should now available with `localhost:5000`




## Database queries
These queries can be test run on `MySQL Workbench` or `MySQL Command Line Client`

#### Initial seed
```
CREATE DATABASE bioblink;

USE bioblink;

CREATE TABLE blinks(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	rising_time INT unsigned NOT NULL,
	falling_time INT unsigned NOT NULL,
	PRIMARY KEY (id)
); 

INSERT INTO blinks (rising_time, falling_time) VALUES
(1, 5),
(8,16),
(20, 23),
(30, 35),
(40, 47);

```

####Average duration
```
SELECT AVG(falling_time - rising_time) as avg_duration FROM blinks;
```

