UPDATE Departamento
	SET nome = 'XXXXXX',
		nome_diretor = 'XXXXX',
		ramal = 0
WHERE id = 0

-- Versão usando a sigla
UPDATE UF
	SET nome = 'XXXXX',
		populacao = 0
WHERE sigla = 'XX';
-- Versão usando o nome
UPDATE UF
	SET sigla = 'XX',
		populacao = 0
WHERE nome = 'XXXXX'

UPDATE Produto
	SET descricao = 'XXXXXXXXXX',
		valor_unitario = 0.00,
		quantidade_estoque = 0
WHERE id = 0

UPDATE Aluno
	SET nome = 'XXXXXXXXX',
		telefones = 'DD 9XXXX-XXXX',
		idade = 0,
		data_nascimento = 'AAAA-MM-DD'
WHERE id = 0


