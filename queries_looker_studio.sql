-- ===============================================
-- QUERIES PARA LOOKER STUDIO - ANÁLISE DE VENDAS
-- Dataset: probable-bebop-386417.TesteBigQuery.VendasLBC
-- ===============================================

-- 📊 QUERY 1: RESUMO GERAL (KPIs)
-- Use para criar cards/indicadores principais
SELECT 
    COUNT(_id) as total_pedidos,
    COUNT(DISTINCT name) as clientes_unicos,
    SUM(ARRAY_LENGTH(products)) as total_itens_vendidos,
    ROUND(SUM(
        (SELECT SUM(p.price * p.quantity) FROM UNNEST(products) as p)
    ), 2) as receita_total,
    ROUND(AVG(
        (SELECT SUM(p.price * p.quantity) FROM UNNEST(products) as p)
    ), 2) as ticket_medio,
    MIN(DATE(created_at)) as primeira_venda,
    MAX(DATE(created_at)) as ultima_venda
FROM `probable-bebop-386417.TesteBigQuery.VendasLBC`;

-- ===============================================

-- 📈 QUERY 2: VENDAS DIÁRIAS
-- Use para gráfico de linhas temporal
SELECT 
    DATE(created_at) as data,
    EXTRACT(YEAR FROM created_at) as ano,
    EXTRACT(MONTH FROM created_at) as mes,
    EXTRACT(DAY FROM created_at) as dia,
    FORMAT_DATE('%A', DATE(created_at)) as dia_semana,
    COUNT(DISTINCT _id) as num_pedidos,
    SUM(ARRAY_LENGTH(products)) as total_itens,
    ROUND(SUM(
        (SELECT SUM(p.price * p.quantity) FROM UNNEST(products) as p)
    ), 2) as receita_dia
FROM `probable-bebop-386417.TesteBigQuery.VendasLBC`
GROUP BY data, ano, mes, dia, dia_semana
ORDER BY data;

-- ===============================================

-- 🏆 QUERY 3: TOP PRODUTOS MAIS VENDIDOS
-- Use para gráfico de barras
SELECT 
    produto.name as produto,
    produto.sku,
    SUM(produto.quantity) as total_vendido,
    COUNT(DISTINCT _id) as num_pedidos,
    ROUND(AVG(produto.price), 2) as preco_medio,
    ROUND(SUM(produto.price * produto.quantity), 2) as receita_total
FROM `probable-bebop-386417.TesteBigQuery.VendasLBC`,
UNNEST(products) as produto
GROUP BY produto.name, produto.sku
ORDER BY total_vendido DESC;

-- ===============================================

-- 💰 QUERY 4: RANKING DE CLIENTES
-- Use para tabela ou gráfico de barras horizontais
SELECT 
    name as cliente,
    COUNT(_id) as num_pedidos,
    SUM(ARRAY_LENGTH(products)) as total_itens,
    ROUND(SUM(
        (SELECT SUM(p.price * p.quantity) FROM UNNEST(products) as p)
    ), 2) as total_gasto,
    ROUND(AVG(
        (SELECT SUM(p.price * p.quantity) FROM UNNEST(products) as p)
    ), 2) as ticket_medio
FROM `probable-bebop-386417.TesteBigQuery.VendasLBC`
GROUP BY name
ORDER BY total_gasto DESC;

-- ===============================================

-- 🕐 QUERY 5: VENDAS POR HORA E DIA DA SEMANA
-- Use para mapa de calor (heatmap)
SELECT 
    FORMAT_DATE('%A', DATE(created_at)) as dia_semana,
    EXTRACT(HOUR FROM created_at) as hora,
    COUNT(_id) as num_pedidos,
    ROUND(SUM(
        (SELECT SUM(p.price * p.quantity) FROM UNNEST(products) as p)
    ), 2) as receita,
    ROUND(AVG(
        (SELECT SUM(p.price * p.quantity) FROM UNNEST(products) as p)
    ), 2) as ticket_medio
FROM `probable-bebop-386417.TesteBigQuery.VendasLBC`
GROUP BY dia_semana, hora
ORDER BY 
    CASE dia_semana
        WHEN 'Monday' THEN 1
        WHEN 'Tuesday' THEN 2 
        WHEN 'Wednesday' THEN 3
        WHEN 'Thursday' THEN 4
        WHEN 'Friday' THEN 5
        WHEN 'Saturday' THEN 6
        WHEN 'Sunday' THEN 7
    END, hora;

-- ===============================================

-- 📅 QUERY 6: VENDAS DOS ÚLTIMOS 30 DIAS
-- Use para dashboards em tempo real
SELECT 
    DATE(created_at) as data,
    FORMAT_DATE('%A', DATE(created_at)) as dia_semana,
    COUNT(_id) as pedidos,
    SUM(ARRAY_LENGTH(products)) as itens,
    ROUND(SUM(
        (SELECT SUM(p.price * p.quantity) FROM UNNEST(products) as p)
    ), 2) as receita,
    STRING_AGG(DISTINCT name, ', ' LIMIT 3) as clientes_exemplo
FROM `probable-bebop-386417.TesteBigQuery.VendasLBC`
WHERE DATE(created_at) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
GROUP BY DATE(created_at), dia_semana
ORDER BY data DESC;

-- ===============================================

-- 🎯 QUERY 7: MAIOR VENDA POR DIA
-- Use para análise de picos de vendas
WITH vendas_diarias AS (
    SELECT 
        _id,
        name as cliente,
        DATE(created_at) as data,
        ROUND(
            (SELECT SUM(p.price * p.quantity) FROM UNNEST(products) as p), 2
        ) as valor_pedido,
        ARRAY_LENGTH(products) as itens_pedido
    FROM `probable-bebop-386417.TesteBigQuery.VendasLBC`
),
maiores_vendas AS (
    SELECT 
        data,
        MAX(valor_pedido) as maior_valor
    FROM vendas_diarias
    GROUP BY data
)
SELECT 
    v.data,
    v._id as pedido_id,
    v.cliente,
    v.valor_pedido as maior_venda,
    v.itens_pedido
FROM vendas_diarias v
JOIN maiores_vendas m ON v.data = m.data AND v.valor_pedido = m.maior_valor
ORDER BY v.data DESC;

-- ===============================================

-- 👤 QUERY 8: PRODUTOS POR CLIENTE
-- Use para análise de preferências
SELECT 
    name as cliente,
    produto.name as produto,
    SUM(produto.quantity) as qtd_comprada,
    COUNT(DISTINCT _id) as vezes_comprou,
    ROUND(SUM(produto.price * produto.quantity), 2) as valor_gasto_produto,
    ROUND(AVG(produto.price), 2) as preco_medio_pago
FROM `probable-bebop-386417.TesteBigQuery.VendasLBC`,
UNNEST(products) as produto
GROUP BY name, produto.name
ORDER BY name, qtd_comprada DESC;

-- ===============================================

-- 📈 QUERY 9: CRESCIMENTO MENSAL
-- Use para análise de tendências
WITH vendas_mensais AS (
    SELECT 
        FORMAT_DATE('%Y-%m', DATE(created_at)) as mes,
        COUNT(_id) as pedidos,
        ROUND(SUM(
            (SELECT SUM(p.price * p.quantity) FROM UNNEST(products) as p)
        ), 2) as receita
    FROM `probable-bebop-386417.TesteBigQuery.VendasLBC`
    GROUP BY mes
    ORDER BY mes
),
vendas_com_lag AS (
    SELECT 
        mes,
        pedidos,
        receita,
        LAG(receita) OVER (ORDER BY mes) as receita_mes_anterior
    FROM vendas_mensais
)
SELECT 
    mes,
    pedidos,
    receita,
    receita_mes_anterior,
    CASE 
        WHEN receita_mes_anterior IS NOT NULL THEN
            ROUND(((receita - receita_mes_anterior) / receita_mes_anterior) * 100, 2)
        ELSE NULL
    END as crescimento_percentual
FROM vendas_com_lag
ORDER BY mes;

-- ===============================================

-- ⏰ QUERY 10: VENDAS POR HORA (SIMPLES)
-- Use para gráfico de barras por horário
SELECT 
    EXTRACT(HOUR FROM created_at) as hora,
    COUNT(_id) as num_pedidos,
    ROUND(SUM(
        (SELECT SUM(p.price * p.quantity) FROM UNNEST(products) as p)
    ), 2) as receita_hora,
    ROUND(AVG(
        (SELECT SUM(p.price * p.quantity) FROM UNNEST(products) as p)
    ), 2) as ticket_medio_hora
FROM `probable-bebop-386417.TesteBigQuery.VendasLBC`
GROUP BY hora
ORDER BY hora;

-- ===============================================

-- 🔍 QUERY 11: ANÁLISE DETALHADA POR PERÍODO
-- Use para filtros avançados no Looker Studio
SELECT 
    DATE(created_at) as data,
    EXTRACT(YEAR FROM created_at) as ano,
    EXTRACT(MONTH FROM created_at) as mes,
    EXTRACT(DAY FROM created_at) as dia,
    EXTRACT(HOUR FROM created_at) as hora,
    FORMAT_DATE('%A', DATE(created_at)) as dia_semana,
    FORMAT_DATE('%B', DATE(created_at)) as nome_mes,
    _id as pedido_id,
    name as cliente,
    ARRAY_LENGTH(products) as num_itens,
    ROUND(
        (SELECT SUM(p.price * p.quantity) FROM UNNEST(products) as p), 2
    ) as valor_pedido
FROM `probable-bebop-386417.TesteBigQuery.VendasLBC`
ORDER BY created_at DESC;
