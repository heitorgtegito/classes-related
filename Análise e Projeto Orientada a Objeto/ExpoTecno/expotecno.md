# ExpoTecno


## 1. Regras de Negócio

| ID  | Regra | Descrição |
| :-: | :---: | :-------: |
| RN01 | Limite da Equipe | Cada equipe tem no máximo 4 alunos e no mínimo 2. |
| RN02 | Limite de Projeto | Cada aluno só pode participar de um único projeto no ano. |
| RN03 | Avaliadores | No dia do evento, haverá avaliadores que vão andar pela feira julgando os projetos. |

## 2. Requisitos Funcionais

| Código | Nome | Descrição | Prioridade |
| :----: | :--: | :-------: | :--------: |
| RF01 | Login | Login e Senha (Utilizando integração via API).| Alta |
| RF02 | Propostas | Envio de proposta de um projeto (com título, área de conhecimento e resumo). | Alta |
| RF03 | Convite | Convite de outros colegas para integrar a equipe do projeto (busca por nome ou matrícula). | Média |
| RF04 | Restrição Convite | Impedir o aluno de ser convidado para outras equipes. | Baixa |
| RF05 | Limite | O sistema deve fechar as inscrições 15 dias antes do dia do evento. | Média |
| RF06 | Orientadores | Os professores orientadores devem ser capazes de visualizar os projetos enviados em sua área de conhecimento. | Alta |
| RF07 | Avaliação | Os professores orientadores devem ser capazes de avaliar a proposta enviada e decidir se ela é aprovada ou recusada. Se for recusada, o professor é obrigado a preencher um campo de justificativa. | Média |
| RF08 | Aviso de rejeição | Caso a proposta seja recusada, um email será enviado para os alunos da equipe com a justificativa. | Baixa |
| RF09 | Notas | Os Avaliadores serão capazes de acessar os projetos pelo sistema e atribuir notas de 0 a 10 para os critérios de Inovação, Execução Técnica e Apresentação. | Alta |
| RF10 | Encerramento | A Coordenação deve possuir um painel que pode encerrar as avaliações. | Alta |
| RF11 | Média & Ranking | Ao fim das avaliações, o sistema deve calcular a média de cada equipe e gerar um ranking por área de conhecimento. | Média |
| RF12 | PDF | O resultado deve ser possível de ser exportado em PDF. | Baixa |

## 3. Requisitos Não-funcionais

| Código | Nome | Descrição | Categoria | Classificação |
| :----: | :--: | :-------: | :-------: | :-----------: |
| NF01 | Responsividade | Responsividade do sistema para dispositivos móveis.| Suportabilidade | Desejável |
| NF02 | Funcionalidade Offline | O sistema deve ser capaz de salvar as notas offline no navegador do avaliador caso e sincronizar com o servidor assim que a conexão voltar. | Confiabilidade | Obrigatório |
