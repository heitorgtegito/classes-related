create table Categoria(
	id int identity(1,1) NOT NULL,
	descricao varchar(20) NOT NULL,
	primary key(id)
)

create table Contato(
	id INT identity(1,1) NOT NULL,
	nome varchar(90) NOT NULL,
	telefones varchar(50),
	email varchar(100),
	dataNascimento DATE,
	categoria_id int not null,
	primary key(id),
	foreign key(categoria_id) references Categoria(id)
)