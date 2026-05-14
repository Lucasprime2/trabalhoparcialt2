
CREATE DATABASE primeiro_teste;

USE primeiro_teste;


CREATE TABLE tarefas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(255) NOT NULL
);

SELECT * FROM tarefas;