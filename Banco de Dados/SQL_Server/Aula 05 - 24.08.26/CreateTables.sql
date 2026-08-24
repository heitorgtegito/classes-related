create table Departamento(
	id INT identity(1,1) NOT NULL,
	nome VARCHAR(50) NOT NULL,
	nome_diretor VARCHAR(100) NOT NULL, 
	ramal INT NOT NULL,
	PRIMARY KEY(id)
)

create table UF(
	sigla CHAR(2) NOT NULL,
	nome VARCHAR(80) NOT NULL,
	populacao INT NOT NULL,
	PRIMARY KEY (sigla)
)

create table Produto(
	id INT identity(1,1) NOT NULL,
	descricao VARCHAR(150) NOT NULL,
	valor_unitario NUMERIC(10,2) NOT NULL,
	quantidade_estoque INT NOT NULL,
	PRIMARY KEY (id)
)

create table Aluno(
	id INT identity(1,1) NOT NULL,
	nome VARCHAR(100) NOT NULL,
	telefones VARCHAR(30) NOT NULL, 
	idade INT NOT NULL,
	data_nascimento DATE NOT NULL
	PRIMARY KEY (id)
)