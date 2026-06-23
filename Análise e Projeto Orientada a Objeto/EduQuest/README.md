# EduQuest
## Visão Geral
A direção do campus quer incentivar a ajuda mútua entre os estudantes do curso técnico através de uma plataforma web gamificada chamada EduQuest. O sistema funciona como um mercado de monitoria, onde alunos que estão com dificuldades em matérias (como Algoritmos ou Português) podem solicitar ajuda, e alunos que dominam o assunto podem oferecer suporte. Para tornar o sistema atraente, a escola adotou uma roupagem de jogo de RPG (Role-Playing Game), onde os alunos acumulam pontos para subir de nível e obter certificados de horas complementares no fim do ano.

Na plataforma, cada estudante possui um único perfil, mas pode atuar em dois papéis: como um Aventureiro (quando precisa de ajuda em alguma matéria) ou como um Guia (quando vai dar a monitoria). O "Mundo" do sistema é composto pelos Pergaminhos de Conhecimento, que nada mais são do que as disciplinas do curso (ex.: Programação Web, Banco de Dados, Matemática). Toda a interação se baseia na criação e resolução de Missões de Resgate, que representam os agendamentos de monitoria para sanar dúvidas acadêmicas.

## Caso de Uso 01 - Publicar Missão de Resgate (Solicitar Monitoria)
- Atores: Aluno (no papel de Aventureiro)
- Fluxo Principal:
	
    0. O aluno acessa o mural eletrônico do EduQuest e solicita a criação de uma nova Missão de Resgate.
	1. O sistema solicita o Pergaminho de Conhecimento (a disciplina afetada), uma descrição curta do "monstro" (a dúvida específica ou o conteúdo do trabalho) e a quantidade de Cristais de Mana oferecidos (horas de estudo que a monitoria deve durar).
	2. O aluno seleciona a disciplina, digita a dúvida e define o tempo (ex.: 2 horas).
	3. O sistema valida se o aluno possui saldo de tempo suficiente em seu perfil para abrir aquela missão.
	4. O sistema registra a Missão de Resgate com o status "Disponível no Mural", gerando um código identificador único e associando-a ao perfil do aluno solicitante.

## Caso de Uso 02 - Reivindicar e Concluir Missão (Realizar Monitoria)
- Atores: Aluno (no papel de Guia)
- Fluxo Principal:
	
    0. O aluno (Guia) navega pelo mural de missões disponíveis e filtra pelo Pergaminho de Conhecimento (disciplina) que ele domina.
	1. O Guia seleciona uma Missão de Resgate específica e clica em "Aceitar Desafio".
	2. O sistema altera os status da missão para "Em Andamento" e vincula o perfil do Guia àquela missão, bloqueando-a para outros usuários
	3. Após realizarem o encontro de monitoria no mundo real, o Guia acessa o sistema e clica em "Missão Cumprida", inserindo um breve resumo do que foi estudado.
	4. O sistema envia uma confirmação para o Aluno que pediu a ajuda (Aventureiro), que valida a conclusão.
	5. O sistema altera o status da missão para "Finalizada", debita os Cristais de Mana (horas) do Aluno ajudado e credita esses pontos como Pontos de Prestígio (horas complementares) no saldo do Guia.