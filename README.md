# Demonstração Big Query - CRUD com Python

Este projeto demonstra como trabalhar com Google Big Query em Python, carregando dados de um arquivo JSON e realizando operações CRUD (Create, Read, Update, Delete).

## 📋 Pré-requisitos

1. **Conta Google Cloud Platform** com Big Query habilitado
2. **Arquivo de credenciais JSON** do Google Cloud
3. **Python 3.7+** instalado
4. **Ambiente virtual (venv)** configurado

## 🚀 Configuração Inicial

### 1. Criar e ativar ambiente virtual

```bash
# Criar venv
python -m venv venv

# Ativar venv (Windows)
venv\Scripts\activate

# Ativar venv (Linux/Mac)
source venv/bin/activate
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Configurar credenciais

- Coloque seu arquivo de credenciais JSON na raiz do projeto
- Atualize o caminho no arquivo `Demonstracao_Big_Query.py` se necessário

## 📁 Estrutura do Projeto

```
Demonstracao_Big_Query/
├── Demonstracao_Big_Query.py    # Código principal com funções CRUD
├── requirements.txt             # Dependências do projeto
└── README.md                    # Este arquivo
```

## 📊 Dados de Exemplo

- **ID do pedido**
- **Nome do cliente**
- **Data de criação**
- **Lista de produtos** (nome, SKU, preço, quantidade)

## 🔧 Como Usar

### Execução Automática (Recomendado)

```bash
python Demonstracao_Big_Query.py
```

Executa toda a demonstração automaticamente.

## 🗃️ Operações CRUD Disponíveis

### 1. **CREATE** - Criar e Inserir Dados

- `criar_dataset_e_tabelas()` - Cria dataset e tabelas no Big Query
- `inserir_dados(dados_json)` - Insere dados do JSON nas tabelas

### 2. **READ** - Consultar Dados

- `consultar_pedidos()` - Lista todos os pedidos com totais
- `consultar_produtos_por_pedido(id)` - Produtos de um pedido específico
- Consultas avançadas (vendas por cliente, produtos mais vendidos, etc.)

### 3. **UPDATE** - Atualizar Dados

- `atualizar_preco_produto(sku, novo_preco)` - Atualiza preço de produto
- Funções para atualizar nomes de clientes, aplicar descontos, etc.

### 4. **DELETE** - Deletar Dados

- `deletar_por_id(id)` - Remove pedido específico por ID
- `deletar_por_cliente(nome)` - Remove todos os pedidos de um cliente
- `deletar_por_data(data)` - Remove pedidos de uma data específica
- `deletar_por_produto(produto)` - Remove pedidos que contêm produto específico
- `deletar_por_multiplas_condicoes()` - Remove com múltiplas condições
- `deletar_com_confirmacao()` - Remove após mostrar o que será deletado
- `deletar_dados_bigquery()` - Remove TODA a tabela (cuidado!)

## 📈 Análises Disponíveis

- **Vendas por cliente** - Total de pedidos e valor por cliente
- **Produtos mais vendidos** - Ranking de produtos por quantidade
- **Receita mensal** - Análise temporal das vendas
- **Ticket médio** - Valor médio por cliente
- **Backup de dados** - Exportação para CSV

## 🛠️ Funções Principais

### Carregar dados do JSON

```python
dados = carregar_exemplos()
```

### Inserir novo pedido

```python
novo_pedido = {
    "_id": "11",
    "name": "Cliente Novo",
    "created_at": "2025-01-15T14:30:00Z",
    "products": [
        {"name": "Produto", "sku": "SKU-001", "price": 10.0, "quantity": 1}
    ]
}
inserir_dados([novo_pedido])
```

### Consultar dados específicos

```python
# Todos os pedidos
consultar_pedidos()

# Produtos de um pedido
consultar_produtos_por_pedido("1")
```

### Atualizar preços

```python
atualizar_preco_produto("CX-001", 7.50)
```

### Deletar dados específicos

```python
# Deletar por ID específico
deletar_por_id("3")

# Deletar todos os pedidos de um cliente
deletar_por_cliente("João Silva")

# Deletar pedidos de uma data
deletar_por_data("2025-06-20")

# Deletar pedidos de um período
deletar_por_data("2025-06-20", "2025-06-25")

# Deletar pedidos que contêm produto específico
deletar_por_produto("Coxinha")

# Deleção segura com confirmação
deletar_com_confirmacao("name = 'Carlos Lima'")
```

## 📝 Consultas SQL de Exemplo

### Vendas por cliente:

```sql
SELECT
    name as cliente,
    COUNT(*) as total_pedidos,
    SUM(pp.preco * pp.quantidade) as valor_total
FROM `demonstracao_vendas.pedidos` p
JOIN `demonstracao_vendas.produtos_pedido` pp ON p.id = pp.pedido_id
GROUP BY name
ORDER BY valor_total DESC
```

### Produtos mais vendidos:

```sql
SELECT
    produto_nome,
    SUM(quantidade) as total_vendido,
    AVG(preco) as preco_medio
FROM `demonstracao_vendas.produtos_pedido`
GROUP BY produto_nome
ORDER BY total_vendido DESC
```

### Exemplos de Deleção:

```sql
-- Deletar por ID específico
DELETE FROM `tabela` WHERE _id = '3'

-- Deletar por cliente
DELETE FROM `tabela` WHERE name = 'João Silva'

-- Deletar por data
DELETE FROM `tabela` WHERE DATE(created_at) = '2025-06-20'

-- Deletar por período
DELETE FROM `tabela` WHERE created_at BETWEEN '2025-06-01' AND '2025-06-30'

-- Deletar múltiplos IDs
DELETE FROM `tabela` WHERE _id IN ('1', '2', '3')

-- Deletar com condições complexas
DELETE FROM `tabela` WHERE name = 'João' AND DATE(created_at) >= '2025-06-01'
```

## ⚠️ Observações Importantes

1. **Custos**: Big Query cobra por consultas. Use dados pequenos para testes.
2. **Credenciais**: Nunca commite arquivos de credenciais no Git.
3. **Região**: Dataset é criado na região US por padrão.
4. **Tabelas**: O código cria automaticamente as tabelas necessárias.

## 🚨 Cuidados Especiais com Deleção

⚠️ **ATENÇÃO**: Big Query não tem UNDO! Uma vez deletado, os dados são perdidos permanentemente.

### Dicas Importantes:

- **Sempre faça backup** antes de deletar dados importantes
- **Use deleção segura** (`deletar_com_confirmacao()`) para ver o que será deletado
- **Teste com dados pequenos** primeiro
- **Big Query cobra** por operações DML (DELETE/UPDATE/INSERT)
- **DELETE processa toda a tabela**, mesmo com WHERE específico

### Boas Práticas:

- Use condições específicas no WHERE
- Confirme sempre antes de executar
- Para deletar muitos dados, faça em lotes pequenos
- Monitore o número de linhas afetadas
- Use partições de tabelas para reduzir custos

## 📄 Licença

Este projeto é apenas para fins educacionais e demonstração.

---

## 💰 Considerações de Custos - BigQuery

### ✅ LIMITES GRATUITOS (Free Tier):

- **Consultas**: Primeiros 1 TB de processamento por mês **GRÁTIS**
- **Armazenamento**: Primeiros 10 GB por mês **GRÁTIS**
- **Carregamento de dados**: **GRÁTIS** (via Cloud Storage)
- **Exportação de dados**: **GRÁTIS**
- **Consultas em cache**: **GRÁTIS**
- **Consultas com erro**: **GRÁTIS**

### 💰 PREÇOS DE CONSULTAS (On-Demand):

- **Após 1 TB gratuito**: $6.25 por TB processado
- **Mínimo**: 10 MB processados por consulta
- **Cobrança**: Por dados processados, não por resultados retornados
- **Slots**: Acesso a até 2.000 slots concorrentes

### 📁 PREÇOS DE ARMAZENAMENTO:

- **Armazenamento Ativo**: $0.02 por GB/mês
- **Armazenamento Long-term** (90+ dias): $0.01 por GB/mês
- **Redução automática**: 50% após 90 dias sem modificação

### 🔄 PREÇOS DE STREAMING:

- **Legacy Streaming**: $0.01 por 200 MB
- **Storage Write API**: $0.025 por 1 GB (primeiros 2 TB/mês grátis)

### 🏢 PREÇOS ALTERNATIVOS (Capacity Pricing):

- **Standard Edition**: $0.04 por slot/hora
- **Enterprise Edition**: $0.06 por slot/hora
- **Enterprise Plus**: $0.10 por slot/hora
- _Mínimo 100 slots, descontos para contratos de 1-3 anos_

### 🌐 TRANSFERÊNCIA DE DADOS:

- **Mesma região**: **GRÁTIS**
- **Entre regiões**: $0.02-$0.14 por GiB (varia por região)
- **Dentro do Google Cloud**: **GRÁTIS** ou baixo custo

### 💡 DICAS PARA ECONOMIZAR:

- ✅ Use `SELECT` com colunas específicas (não `SELECT *`)
- ✅ Use `WHERE` para filtrar dados
- ✅ Particione tabelas por data
- ✅ Use clustering em colunas frequentemente consultadas
- ✅ Cache consultas frequentes
- ✅ Use views materializadas
- ✅ Monitore uso com alertas de orçamento

### 🎯 QUANDO CADA MODELO É MELHOR:

- **📊 On-Demand**: Workloads variáveis, desenvolvimento, experimentação
- **🏢 Capacity**: Workloads previsíveis, ETL constante, alta concorrência

---

## ❓ Dúvidas Frequentes sobre BigQuery

### 🆔 "BigQuery não tem geração de ID automático?"

**Resposta**: **Correto**, BigQuery é diferente de bancos relacionais tradicionais:

- ❌ **Não tem AUTO_INCREMENT** como MySQL/PostgreSQL
- ❌ **Não tem chaves primárias** tradicionais
- ❌ **Não gera IDs automaticamente**

**📝 Soluções disponíveis**:

- **GENERATE_UUID()** - Gera IDs únicos aleatórios
- **ROW_NUMBER()** - Numeração sequencial em consultas
- **FARM_FINGERPRINT()** - Hash determinístico
- **Combinar colunas** - Criar IDs compostos
- **Controlar via aplicação** - Gerar IDs no Python

```sql
-- Exemplos de criação de IDs
SELECT GENERATE_UUID() as id_unico
SELECT ROW_NUMBER() OVER (ORDER BY created_at) as id_sequencial
SELECT CONCAT(cliente, '_', DATE(created_at)) as id_composto
```

### 🔗 "BigQuery é feito para relacionamentos entre tabelas?"

**Resposta**: **Sim e não** - é diferente de bancos relacionais:

**❌ O que BigQuery NÃO tem:**

- Chaves estrangeiras (Foreign Keys)
- Constraints de integridade referencial
- JOINs otimizados como bancos relacionais
- Índices tradicionais

**✅ O que BigQuery OFERECE:**

- **JOINs funcionam normalmente** (mas podem ser caros)
- **Dados desnormalizados** são preferidos (JSON, arrays)
- **Nested e Repeated fields** - relacionamentos dentro da tabela
- **Partitioning e Clustering** para performance

**🎯 Melhor prática no BigQuery:**

```sql
-- ❌ Evite muitos JOINs (caro)
SELECT * FROM pedidos p JOIN produtos pr ON p.id = pr.pedido_id

-- ✅ Prefira dados aninhados (mais eficiente)
SELECT
  cliente,
  (SELECT SUM(price * quantity) FROM UNNEST(products)) as total
FROM pedidos
```

### ↩️ "BigQuery não tem UNDO para operações?"

**Resposta**: **Correto** - operações são **irreversíveis**:

**❌ O que NÃO existe:**

- ROLLBACK para DELETE/UPDATE/INSERT
- UNDO para operações DML
- Recuperação automática de dados deletados

**✅ O que BigQuery OFERECE como proteção:**

- **Time Travel** - consultar dados de até 7 dias atrás
- **Table Snapshots** - backups manuais
- **Fail-safe** - recuperação de emergência (7 dias adicionais)

**🛡️ Estratégias de proteção:**

```sql
-- 1. Backup antes de deletar
CREATE TABLE backup_pedidos AS SELECT * FROM pedidos;

-- 2. Time Travel para recuperar
SELECT * FROM pedidos FOR SYSTEM_TIME AS OF '2025-01-14 10:00:00'

-- 3. Teste com WHERE primeiro
SELECT COUNT(*) FROM pedidos WHERE cliente = 'João'; -- Conferir
DELETE FROM pedidos WHERE cliente = 'João'; -- Só depois deletar

-- 4. Use transações quando possível
BEGIN TRANSACTION;
  UPDATE pedidos SET status = 'cancelado' WHERE id = '123';
  -- Se der erro, faz ROLLBACK automaticamente
COMMIT TRANSACTION;
```

### 🏗️ "Como BigQuery foi projetado para ser usado?"

**BigQuery é otimizado para:**

- **📊 Análise de dados** (OLAP) - não transações (OLTP)
- **🗃️ Dados desnormalizados** - menos JOINs, mais arrays/JSON
- **📈 Consultas grandes** - processar muitos dados de uma vez
- **⏱️ Batch processing** - não para updates frequentes
- **📱 BI e Analytics** - relatórios, dashboards, ML

**Não é ideal para:**

- ❌ Sistemas transacionais de alta frequência
- ❌ Updates constantes de registros individuais
- ❌ Aplicações que precisam de consistência imediata
- ❌ Sistemas que dependem muito de relacionamentos complexos

---

**Desenvolvido para demonstrar integração Python + Google Big Query**
