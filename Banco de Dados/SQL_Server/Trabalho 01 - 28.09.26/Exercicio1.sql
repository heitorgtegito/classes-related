Create Table Departamento(
	id INT IDENTITY(1,1) NOT NULL,
	nome VARCHAR(30) NOT NULL,
	nome_diretor VARCHAR(90),
	ramal INT,
	PRIMARY KEY(id)
)

Create Table Funcionario(
	id INT IDENTITY(1,1) NOT NULL,
	nome VARCHAR(90) NOT NULL,
	telefones VARCHAR(20),
	idade INT,
	data_nascimento DATE,
	endereco VARCHAR(200),
	departamento_id INT NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(departamento_id) references Departamento(id)
)

INSERT INTO Departamento(nome, nome_diretor, ramal)
	Values ('DIATINF', 'Alessandro José', 01)

INSERT INTO Departamento(nome, nome_diretor, ramal)
	Values ('DIACIN', 'Jacques Cousteau', 02)

INSERT INTO Departamento(nome, nome_diretor, ramal)
	Values ('DIACON', 'Alexandre Spotti', 03)

INSERT INTO Funcionario(nome, telefones, idade, data_nascimento, endereco, departamento_id)
	Values ('João', NULL, NULL, '19980327', NULL, 01)
INSERT INTO Funcionario(nome, telefones, idade, data_nascimento, endereco, departamento_id)
	Values ('José', '84 99969-6760', 35, NULL, NULL, 01)
INSERT INTO Funcionario(nome, telefones, idade, data_nascimento, endereco, departamento_id)
	Values ('Lucas', NULL, 41, NULL, 'Ponta Negra', 02)
INSERT INTO Funcionario(nome, telefones, idade, data_nascimento, endereco, departamento_id)
	Values ('Mariana', NULL, NULL, '19890112', NULL, 02)
INSERT INTO Funcionario(nome, telefones, idade, data_nascimento, endereco, departamento_id)
	Values ('Rebeca', NULL, 66, NULL, NULL, 03)


Select dep.nome as 'departamento_nome',
	fun.nome as 'funcionario_nome',
	fun.telefones as 'funcionario_telefones'

From Departamento dep
Inner Join Funcionario fun on dep.id = fun.departamento_id

order by dep.nome, fun.nome