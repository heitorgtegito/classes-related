# Tema 3: Manipulação de Dados, Validações e Ciclo de Vida do Objeto (Peewee ORM)

**Disciplina:** Análise e Projeto Orientados a Objetos (APOO) / Desenvolvimento de Sistemas  
**Foco:** Operações CRUD clássicas, persistência de estado dos objetos e garantia de integridade de dados  
**Tecnologias:** Python 3, Peewee ORM, SQLite  

---

## 1. Introdução e Conceitos Principais

Na Orientação a Objetos, manipulamos objetos em memória que representam entidades do mundo real. No entanto, o estado desses objetos é volátil. Para torná-lo persistente em um Banco de Dados Relacional, utilizamos um **ORM (Object-Relational Mapping)** como o **Peewee**.

Este guia aborda todo o **ciclo de vida de uma entidade**: desde sua instanciação e gravação no banco, passando por buscas, atualizações e validações de regras de negócio, até a exclusão com logs de auditoria.

---

## 2. Inserção de Dados (Criação e Persistência)

Existem três formas principais de inserir dados no Peewee:

### 2.1. `Model.create()`
Instancia o objeto e executa a instrução `INSERT` imediatamente no banco de dados. Retorna a instância salva com a Chave Primária (ID) já feita.

```python
usuario = Usuario.create(nome="Alice Silva", email="alice@email.com", idade=25)
print(usuario.id)  # ID gerado automaticamente pelo banco
```

### 2.2. `Model.save()`
Permite instanciar o objeto em memória, modificar seus atributos e só então persistir no banco. Se o objeto não possui ID, o Peewee executa um `INSERT`; se já possui, executa um `UPDATE`.

```python
usuario = Usuario(nome="Bob Santos", email="bob@email.com", idade=30)
# Regras em memória podem ser aplicadas aqui...
usuario.save()  # Executa INSERT no banco
```

### 2.3. Inserção em Lote (`insert_many()`)
Utilizada para alta performance quando se precisa inserir múltiplos registros de uma vez. Reduz drasticamente o número de conexões/transações com o banco.

```python
novos_usuarios = [
    {"nome": "Carlos Oliveira", "email": "carlos@email.com", "idade": 40},
    {"nome": "Diana Souza", "email": "diana@email.com", "idade": 22}
]
Usuario.insert_many(novos_usuarios).execute()
```

> **Obs:** O `insert_many()` executa SQL direto no banco para ganho de desempenho, **não** disparando sinais do Peewee (`pre_save`/`post_save`).

---

## 3. Leitura e Busca de Registros

### 3.1. `Model.get(...)`
Busca um **único** registro que atenda ao filtro. Se não encontrar nada ou encontrar múltiplos registros, lança uma exceção.

```python
try:
    user = Usuario.get(Usuario.email == "alice@email.com")
except Usuario.DoesNotExist:
    print("Usuário não encontrado.")
```

### 3.2. `Model.get_or_none(...)`
Retorna a instância se encontrada, ou `None` caso não exista registro correspondente. Evita que a aplicação pare por exceção.

```python
user = Usuario.get_or_none(Usuario.email == "inexistente@email.com")
if user is None:
    print("Registro não localizado.")
```

### 3.3. `Model.get_or_create(...)`
Tenta buscar o registro pelo filtro. Se não encontrar, cria um novo registro utilizando os valores padrão informados no parâmetro `defaults`. Retorna uma tupla `(instancia, foi_criado)`.

```python
user, created = Usuario.get_or_create(
    email="eva@email.com",
    defaults={"nome": "Eva Lima", "idade": 28}
)
if created:
    print(f"Novo usuário criado com sucesso: {user.nome}")
else:
    print(f"Usuário já existente: {user.nome}")
```

---

## 4. Atualização e Remoção de Dados

### 4.1. Atualização via Instância (`save()`)
Atualiza uma instância previamente carregada na memória. Dispara os sinais do Peewee (`pre_save` e `post_save`).

```python
user = Usuario.get(Usuario.id == 1)
user.idade = 26
user.save()  # Executa UPDATE no banco
```

### 4.2. Atualização em Lote (`update().execute()`)
Executa uma instrução `UPDATE` SQL diretamente no banco de dados. É performático para grandes volumes, mas não carrega instâncias para a memória nem dispara hooks/sinais.

```python
linhas_afetadas = Usuario.update(idade=Usuario.idade + 1).where(Usuario.idade >= 30).execute()
print(f"Registros atualizados: {linhas_afetadas}")
```

### 4.3. Exclusão de Instância (`delete_instance()`)
Remove o registro do banco referente àquela instância e dispara o sinal `pre_delete`.

```python
user = Usuario.get(Usuario.id == 2)
user.delete()  # Remove do banco
```

---

## 5. Sinais/Hooks do Peewee (Ciclo de Vida e Regras de Negócio)

Os sinais (`playhouse.signals`) permitem desacoplar regras de validação e logs de auditoria dos métodos de controle da aplicação.

* **`@pre_save`**: Executado imediatamente antes do registro ser inserido ou atualizado. Serve para **validações de integridade e regras de negócio de APOO**.
* **`@post_save`**: Executado logo após a gravação no banco. Ideal para **logs de auditoria** e disparos de eventos.
* **`@pre_delete`**: Executado antes da remoção de uma instância do banco.

---

## 6. O código da prática está nesse repositório.

---

## 7. Resumo e Pontos-Chave para Lembrete

1. **CRUD Básico:** Utilize `create()`, `get()`, `save()` e `delete()` para operar sobre instâncias individuais ativando o ciclo de vida e hooks do Peewee.
2. **Performance:** Operações em massa como `insert_many()` e `update()` são rápidas porque rodam direto no SQL, mas ignoram os sinais/hooks do Python.
3. **Integridade de Dados:** Validações de formato e regras do domínio devem ser colocadas em `@pre_save` ou tratadas com exceções como `IntegrityError`.
4. **Auditoria:** Use o sinal `@post_save` e `@pre_delete` para registrar histórico de modificações sem poluir o código principal das rotas ou regras de negócio.
