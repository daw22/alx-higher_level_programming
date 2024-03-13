-- creates a table 'unique_id' with unique id column

CREATE TABLE IF NOT EXIST unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));
