-- creates a table 'unique_id' with unique id column

CREATE TABLE IF NOT EXIST unique_id (id DEFAULT 1 UNIQUE, name VARCHAR(256));
