SELECT con.id,
	con.nome,
	con.email
FROM Contato con
order by con.nome

Select con.nome,
	con.email,
	cat.descricao as categoria_descricao
FROM Contato con
INNER JOIN Categoria cat ON cat.id = con.categoria_id

Select con.nome,
	con.telefones,
	cat.descricao as categoria_descricao
FROM Contato con
INNER JOIN Categoria cat ON cat.id = con.categoria_id
ORDER BY cat.descricao DESC
