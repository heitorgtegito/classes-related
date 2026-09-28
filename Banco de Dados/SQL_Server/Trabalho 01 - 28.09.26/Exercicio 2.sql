Create Table Turma(
	id INT IDENTITY(1,1) NOT NULL,
	nome VARCHAR(30) NOT NULL,
)

Create Table Aluno(
	id INT IDENTITY(1,1) NOT NULL,
	nome VARCHAR(90) NOT NULL,
	telefones VARCHAR(20),
	idade INT,
	data_nascimento DATE,
	turma_id INT NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY(turma_id) references Turma(id)
)

INSERT INTO Turma(nome)
	Values ('INFOWEB 1')

INSERT INTO Turma(nome)
	Values ('INFOWEB 2')

INSERT INTO Turma(nome)
	Values ('MSI 2')

INSERT INTO Aluno(nome, telefones, idade, data_nascimento, turma_id)
	Values ('Ravi', NULL, NULL, NULL, NULL, 01)
INSERT INTO Aluno(nome, telefones, idade, data_nascimento, turma_id)
	Values ('Pedro', NULL, NULL, NULL, NULL, 01)
INSERT INTO Aluno(nome, telefones, idade, data_nascimento, turma_id)
	Values ('Daniel', NULL, NULL, NULL, NULL, 01)
INSERT INTO Aluno(nome, telefones, idade, data_nascimento, turma_id)
	Values ('Eulla', NULL, NULL, NULL, NULL, 01)
INSERT INTO Aluno(nome, telefones, idade, data_nascimento, turma_id)
	Values ('Davi', NULL, NULL, NULL, NULL, 01)
INSERT INTO Aluno(nome, telefones, idade, data_nascimento, turma_id)
	Values ('Vitor', NULL, NULL, NULL, NULL, 01)
INSERT INTO Aluno(nome, telefones, idade, data_nascimento, turma_id)
	Values ('Douglas', NULL, NULL, NULL, NULL, 01)
INSERT INTO Aluno(nome, telefones, idade, data_nascimento, turma_id)
	Values ('Ian', NULL, NULL, NULL, NULL, 01)
INSERT INTO Aluno(nome, telefones, idade, data_nascimento, turma_id)
	Values ('Kristhyan', NULL, NULL, NULL, NULL, 01)
INSERT INTO Aluno(nome, telefones, idade, data_nascimento, turma_id)
	Values ('Lorena', NULL, NULL, NULL, NULL, 01)

INSERT INTO Aluno(nome, telefones, idade, data_nascimento, turma_id)
	Values ('Matheus', NULL, NULL, NULL, NULL, 02)
INSERT INTO Aluno(nome, telefones, idade, data_nascimento, turma_id)
	Values ('Egito', NULL, NULL, NULL, NULL, 02)
INSERT INTO Aluno(nome, telefones, idade, data_nascimento, turma_id)
	Values ('Yasmim', NULL, NULL, NULL, NULL, 02)
INSERT INTO Aluno(nome, telefones, idade, data_nascimento, turma_id)
	Values ('Samara', NULL, NULL, NULL, NULL, 02)
INSERT INTO Aluno(nome, telefones, idade, data_nascimento, turma_id)
	Values ('Elverty', NULL, NULL, NULL, NULL, 02)
INSERT INTO Aluno(nome, telefones, idade, data_nascimento, turma_id)
	Values ('Julia', NULL, NULL, NULL, NULL, 02)
INSERT INTO Aluno(nome, telefones, idade, data_nascimento, turma_id)
	Values ('Juan', NULL, NULL, NULL, NULL, 02)
INSERT INTO Aluno(nome, telefones, idade, data_nascimento, turma_id)
	Values ('Talia', NULL, NULL, NULL, NULL, 02)
INSERT INTO Aluno(nome, telefones, idade, data_nascimento, turma_id)
	Values ('José', NULL, NULL, NULL, NULL, 02)
INSERT INTO Aluno(nome, telefones, idade, data_nascimento, turma_id)
	Values ('João Rafael', NULL, NULL, NULL, NULL, 02)

INSERT INTO Aluno(nome, telefones, idade, data_nascimento, turma_id)
	Values ('Gabriel', NULL, NULL, NULL, NULL, 03)
INSERT INTO Aluno(nome, telefones, idade, data_nascimento, turma_id)
	Values ('Abraão', NULL, NULL, NULL, NULL, 03)
INSERT INTO Aluno(nome, telefones, idade, data_nascimento, turma_id)
	Values ('Ana', NULL, NULL, NULL, NULL, 03)
INSERT INTO Aluno(nome, telefones, idade, data_nascimento, turma_id)
	Values ('Antônio', NULL, NULL, NULL, NULL, 03)
INSERT INTO Aluno(nome, telefones, idade, data_nascimento, turma_id)
	Values ('Aquiles', NULL, NULL, NULL, NULL, 03)
INSERT INTO Aluno(nome, telefones, idade, data_nascimento, turma_id)
	Values ('Heitor', NULL, NULL, NULL, NULL, 03)
INSERT INTO Aluno(nome, telefones, idade, data_nascimento, turma_id)
	Values ('Jonatas', NULL, NULL, NULL, NULL, 03)
INSERT INTO Aluno(nome, telefones, idade, data_nascimento, turma_id)
	Values ('Samuel', NULL, NULL, NULL, NULL, 03)
INSERT INTO Aluno(nome, telefones, idade, data_nascimento, turma_id)
	Values ('José', NULL, NULL, NULL, NULL, 03)
INSERT INTO Aluno(nome, telefones, idade, data_nascimento, turma_id)
	Values ('Miguel', NULL, NULL, NULL, NULL, 03)




Select trm.nome as 'turma_nome',
	aln.nome as 'aluno_nome',
	aln.telefones as 'aluno_telefones'

From Turma trm
Inner Join Aluno aln on trm.id = aln.turma_id

order by trm.nome, aln.nome