
CREATE DATABASE IF NOT EXISTS atv;
USE atv;

-- Aqui vai ser cadastrado todas as pessoas, idades e pesos que vc colocar no terminal rodando
CREATE TABLE IF NOT EXISTS pessoas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    idade INT,
    peso FLOAT
);


CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(20),
    senha VARCHAR(100)
    -- varchar de 100 pq o código encriptado é grande, como por exemplo, senha 123 ($2b$12$3B4lgTShJ/tg7a8SbYOXGOem2iLKu6/9FcO.gjQQhRcxKvVNWPz5G)
);


INSERT INTO usuarios (usuario, senha)
VALUES
('pedro', '123'),
('neto', '123'),
('professora', '123');

-- Usuário      Senha
-- pedro	    $2b$12$3B4lgTShJ/tg7a8SbYOXGOem2iLKu6/9FcO.gjQQhRcxKvVNWPz5G
-- neto	        $2b$12$5HrwZ3/SgF4083w1u3IX4.5AGj47cXB.XFVzZDBGu.BbRScE.fFcq
-- professora	$2b$12$6FkXM.9ZH6Ol1U1JoCPxNecNvT2F.CC3Pjh4ymFTlFtD1/4/2sle2

-- Visualizar tabelas
SELECT * FROM pessoas;
SELECT * FROM usuarios;
