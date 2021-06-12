USE sql5418609;
/*
DROP TABLE sql5418609.method;
DROP TABLE sql5418609.category;
*/
CREATE TABLE sql5418609.account(
	user_id 	INT  AUTO_INCREMENT NOT NULL,
	name    	VARCHAR(500) NOT NULL,
	email    	VARCHAR(500) NOT NULL UNIQUE,
    password	VARCHAR(500) NOT NULL,
	CONSTRAINT pk_user PRIMARY KEY(user_id)
);

CREATE TABLE sql5418609.category(
	category_id 	INT AUTO_INCREMENT NOT NULL,
	name			VARCHAR(500) NOT NULL UNIQUE,
	CONSTRAINT pk_category PRIMARY KEY(category_id)
);

CREATE TABLE sql5418609.method(
	 method_id	 	INT AUTO_INCREMENT NOT NULL,
	 name			VARCHAR(500) NOT NULL UNIQUE,
	 code			VARCHAR(500) NOT NULL,
     description	VARCHAR(50)  NOT NULL,
	 user_id		INT NOT NULL,
     category_id	INT NOT NULL,
     CONSTRAINT pk_method PRIMARY KEY(method_id),
     CONSTRAINT fk_method_user FOREIGN KEY(user_id) REFERENCES account(user_id) ON DELETE CASCADE ON UPDATE CASCADE,
     CONSTRAINT fk_method_category FOREIGN KEY(category_id) REFERENCES category(category_id) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO sql5418609.account(name,email,password) VALUES('Jefferson Torres','jefersontorres000@gmail.com','1234');
INSERT INTO sql5418609.account(name,email,password) VALUES('Jose Okon','okon@gmail.com','1234');
INSERT INTO sql5418609.category(name) VALUES ('Backend');
INSERT INTO sql5418609.category(name) VALUES ('FrontEnd');
INSERT INTO sql5418609.category(name) VALUES ('IA');
INSERT INTO sql5418609.method(name,code,description,user_id,category_id) VALUES('primera funcion','var1=2;var2=3;return var1+var2','descripción miedo',1,1);
INSERT INTO sql5418609.method(name,code,description,user_id,category_id) VALUES('segunda','var1=2;var2=3;return var1+var2','descripción miedo',2,3);
INSERT INTO sql5418609.method(name,code,description,user_id,category_id) VALUES('ultima prueba','var1=2;var2=3;return var1+var2','descripción miedo',1,1);

SELECT m.name as method_name, m.code as method_code, m.description as method_description,a.name as user_name,c.name as category_name FROM sql5416726.method as m 
INNER JOIN sql5416726.account as a ON a.user_id = m.user_id
INNER JOIN sql5416726.category as c ON c.category_id = m.category_id
WHERE m.name LIKE '%%' OR a.name LIKE "%%" OR c.name LIKE "%%";
SELECT * FROM sql5416726.account;
SELECT * FROM sql5416726.category;
SELECT * FROM sql5416726.method;