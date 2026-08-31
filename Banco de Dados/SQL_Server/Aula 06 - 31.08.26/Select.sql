select con.nome,
	con.telefones,
	cat.descricao as 'categoria_descricao'

from Contato con
inner join Categoria cat on cat.id = con.categoria_id

order by con.nome