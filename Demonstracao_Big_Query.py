# 1. Instalar no seu venv as bibliotecas necessarias do google: 
# pip install google-cloud-bigquery

# 2. importar modulos referentes ao bigquery e autenticação:

from google.cloud import bigquery
from google.oauth2 import service_account
import json
# 3. Configurar a autenticação com o arquivo de credenciais criado no Google Cloud Platform 
# e realizar a conexão com o BigQuery:

credenciais  = service_account.Credentials.from_service_account_file(
   "teste3-465312-1c683bdf8ce0.json"
)

cliente = bigquery.Client(credentials=credenciais)

exemplos = [
  {
    "_id": "1",
    "name": "João Silva",
    "created_at": "2025-06-20T11:15:00Z",
    "products": [
      { "name": "Coxinha", "sku": "CX-001", "price": 6.0, "quantity": 2 },
      { "name": "Guaraná 1L", "sku": "GUA-1L", "price": 6.5, "quantity": 1 }
    ]
  },
  {
    "_id": "2",
    "name": "Maria Oliveira",
    "created_at": "2025-06-22T13:30:00Z",
    "products": [
      { "name": "Pão de Queijo", "sku": "PQ-001", "price": 5.0, "quantity": 5 },
      { "name": "Coca-Cola 2L", "sku": "CC-2L", "price": 8.5, "quantity": 1 }
    ]
  },
  {
    "_id": "3",
    "name": "Carlos Lima",
    "created_at": "2025-06-25T18:00:00Z",
    "products": [
      { "name": "Coxinha", "sku": "CX-001", "price": 6.0, "quantity": 3 }
    ]
  },
  {
    "_id": "4",
    "name": "Ana Souza",
    "created_at": "2025-06-28T09:45:00Z",
    "products": [
      { "name": "Suco Natural", "sku": "SN-001", "price": 7.0, "quantity": 2 },
      {
        "name": "Esfiha de Carne",
        "sku": "EF-001",
        "price": 4.5,
        "quantity": 1
      }
    ]
  },
  {
    "_id": "5",
    "name": "João Silva",
    "created_at": "2025-06-30T17:30:00Z",
    "products": [
      { "name": "Coca-Cola 2L", "sku": "CC-2L", "price": 8.5, "quantity": 1 },
      { "name": "Pão de Queijo", "sku": "PQ-001", "price": 5.0, "quantity": 2 }
    ]
  },
  {
    "_id": "6",
    "name": "Bruna Rocha",
    "created_at": "2025-07-01T15:00:00Z",
    "products": [
      { "name": "Coxinha", "sku": "CX-001", "price": 6.0, "quantity": 2 },
      { "name": "Suco Natural", "sku": "SN-001", "price": 7.0, "quantity": 1 }
    ]
  },
  {
    "_id": "7",
    "name": "Maria Oliveira",
    "created_at": "2025-07-03T08:40:00Z",
    "products": [
      {
        "name": "Esfiha de Carne",
        "sku": "EF-001",
        "price": 4.5,
        "quantity": 3
      },
      { "name": "Guaraná 1L", "sku": "GUA-1L", "price": 6.5, "quantity": 1 }
    ]
  },
  {
    "_id": "8",
    "name": "Carlos Lima",
    "created_at": "2025-07-04T12:20:00Z",
    "products": [
      { "name": "Pão de Queijo", "sku": "PQ-001", "price": 5.0, "quantity": 1 },
      { "name": "Coxinha", "sku": "CX-001", "price": 6.0, "quantity": 1 }
    ]
  },
  {
    "_id": "9",
    "name": "João Silva",
    "created_at": "2025-07-05T18:10:00Z",
    "products": [
      { "name": "Coxinha", "sku": "CX-001", "price": 6.0, "quantity": 1 },
      { "name": "Guaraná 1L", "sku": "GUA-1L", "price": 6.5, "quantity": 2 }
    ]
  },
  {
    "_id": "10",
    "name": "Bruna Rocha",
    "created_at": "2025-07-06T10:00:00Z",
    "products": [
      {
        "name": "Esfiha de Carne",
        "sku": "EF-001",
        "price": 4.5,
        "quantity": 2
      },
      { "name": "Suco Natural", "sku": "SN-001", "price": 7.0, "quantity": 1 }
    ]
  },
  {
    "_id": "11",
    "name": "Pedro Santos",
    "created_at": "2025-07-07T09:30:00Z",
    "products": [
      { "name": "Pastel de Frango", "sku": "PF-001", "price": 5.5, "quantity": 2 },
      { "name": "Café Expresso", "sku": "CF-001", "price": 4.0, "quantity": 1 }
    ]
  },
  {
    "_id": "12",
    "name": "Lucia Costa",
    "created_at": "2025-07-08T14:20:00Z",
    "products": [
      { "name": "Açaí 500ml", "sku": "AC-500", "price": 12.0, "quantity": 1 }
    ]
  },
  {
    "_id": "13",
    "name": "João Silva",
    "created_at": "2025-07-09T16:45:00Z",
    "products": [
      { "name": "Coxinha", "sku": "CX-001", "price": 6.0, "quantity": 1 },
      { "name": "Água Mineral", "sku": "AG-001", "price": 3.0, "quantity": 2 }
    ]
  },
  {
    "_id": "14",
    "name": "Roberto Ferreira",
    "created_at": "2025-07-10T11:15:00Z",
    "products": [
      { "name": "Sanduíche Natural", "sku": "SN-002", "price": 9.0, "quantity": 1 },
      { "name": "Guaraná 1L", "sku": "GUA-1L", "price": 6.5, "quantity": 1 }
    ]
  },
  {
    "_id": "15",
    "name": "Fernanda Alves",
    "created_at": "2025-07-11T13:00:00Z",
    "products": [
      { "name": "Cappuccino", "sku": "CP-001", "price": 6.0, "quantity": 2 },
      { "name": "Croissant", "sku": "CR-001", "price": 7.5, "quantity": 1 }
    ]
  },
  {
    "_id": "16",
    "name": "Maria Oliveira",
    "created_at": "2025-07-12T08:30:00Z",
    "products": [
      { "name": "Pão de Queijo", "sku": "PQ-001", "price": 5.0, "quantity": 3 },
      { "name": "Café Expresso", "sku": "CF-001", "price": 4.0, "quantity": 1 }
    ]
  },
  {
    "_id": "17",
    "name": "Marcos Pereira",
    "created_at": "2025-07-13T15:40:00Z",
    "products": [
      { "name": "Torta de Frango", "sku": "TF-001", "price": 8.0, "quantity": 1 },
      { "name": "Coca-Cola 2L", "sku": "CC-2L", "price": 8.5, "quantity": 1 }
    ]
  },
  {
    "_id": "18",
    "name": "Carlos Lima",
    "created_at": "2025-07-14T12:10:00Z",
    "products": [
      { "name": "Coxinha", "sku": "CX-001", "price": 6.0, "quantity": 2 },
      { "name": "Suco Natural", "sku": "SN-001", "price": 7.0, "quantity": 1 }
    ]
  },
  {
    "_id": "19",
    "name": "Juliana Moreira",
    "created_at": "2025-07-15T17:25:00Z",
    "products": [
      { "name": "Vitamina de Frutas", "sku": "VF-001", "price": 8.5, "quantity": 1 },
      { "name": "Pastel de Frango", "sku": "PF-001", "price": 5.5, "quantity": 1 }
    ]
  },
  {
    "_id": "20",
    "name": "Ana Souza",
    "created_at": "2025-07-16T10:50:00Z",
    "products": [
      { "name": "Esfiha de Carne", "sku": "EF-001", "price": 4.5, "quantity": 4 },
      { "name": "Guaraná 1L", "sku": "GUA-1L", "price": 6.5, "quantity": 1 }
    ]
  },
  {
    "_id": "21",
    "name": "Bruna Rocha",
    "created_at": "2025-07-17T14:15:00Z",
    "products": [
      { "name": "Açaí 500ml", "sku": "AC-500", "price": 12.0, "quantity": 1 },
      { "name": "Água Mineral", "sku": "AG-001", "price": 3.0, "quantity": 1 }
    ]
  },
  {
    "_id": "22",
    "name": "Ricardo Barbosa",
    "created_at": "2025-07-18T09:20:00Z",
    "products": [
      { "name": "Sanduíche Natural", "sku": "SN-002", "price": 9.0, "quantity": 2 }
    ]
  },
  {
    "_id": "23",
    "name": "João Silva",
    "created_at": "2025-07-19T16:30:00Z",
    "products": [
      { "name": "Coxinha", "sku": "CX-001", "price": 6.0, "quantity": 3 },
      { "name": "Coca-Cola 2L", "sku": "CC-2L", "price": 8.5, "quantity": 1 }
    ]
  },
  {
    "_id": "24",
    "name": "Camila Rodrigues",
    "created_at": "2025-07-20T11:45:00Z",
    "products": [
      { "name": "Cappuccino", "sku": "CP-001", "price": 6.0, "quantity": 1 },
      { "name": "Croissant", "sku": "CR-001", "price": 7.5, "quantity": 2 }
    ]
  },
  {
    "_id": "25",
    "name": "Pedro Santos",
    "created_at": "2025-07-21T18:00:00Z",
    "products": [
      { "name": "Torta de Frango", "sku": "TF-001", "price": 8.0, "quantity": 1 },
      { "name": "Guaraná 1L", "sku": "GUA-1L", "price": 6.5, "quantity": 1 }
    ]
  },
  {
    "_id": "26",
    "name": "Diego Martins",
    "created_at": "2025-07-22T13:10:00Z",
    "products": [
      { "name": "Pastel de Frango", "sku": "PF-001", "price": 5.5, "quantity": 3 },
      { "name": "Suco Natural", "sku": "SN-001", "price": 7.0, "quantity": 1 }
    ]
  },
  {
    "_id": "27",
    "name": "Maria Oliveira",
    "created_at": "2025-07-23T08:45:00Z",
    "products": [
      { "name": "Pão de Queijo", "sku": "PQ-001", "price": 5.0, "quantity": 2 },
      { "name": "Café Expresso", "sku": "CF-001", "price": 4.0, "quantity": 2 }
    ]
  },
  {
    "_id": "28",
    "name": "Tatiana Reis",
    "created_at": "2025-07-24T15:20:00Z",
    "products": [
      { "name": "Vitamina de Frutas", "sku": "VF-001", "price": 8.5, "quantity": 1 }
    ]
  },
  {
    "_id": "29",
    "name": "Carlos Lima",
    "created_at": "2025-07-25T12:35:00Z",
    "products": [
      { "name": "Coxinha", "sku": "CX-001", "price": 6.0, "quantity": 1 },
      { "name": "Esfiha de Carne", "sku": "EF-001", "price": 4.5, "quantity": 2 }
    ]
  },
  {
    "_id": "30",
    "name": "Gabriel Nascimento",
    "created_at": "2025-07-26T17:50:00Z",
    "products": [
      { "name": "Açaí 500ml", "sku": "AC-500", "price": 12.0, "quantity": 1 },
      { "name": "Água Mineral", "sku": "AG-001", "price": 3.0, "quantity": 2 }
    ]
  },
  {
    "_id": "31",
    "name": "João Silva",
    "created_at": "2025-08-01T12:15:00Z",
    "products": [
      { "name": "Coxinha", "sku": "CX-001", "price": 6.0, "quantity": 4 },
      { "name": "Guaraná 1L", "sku": "GUA-1L", "price": 6.5, "quantity": 1 }
    ]
  },
  {
    "_id": "32",
    "name": "Maria Oliveira",
    "created_at": "2025-08-01T12:30:00Z",
    "products": [
      { "name": "Pão de Queijo", "sku": "PQ-001", "price": 5.0, "quantity": 6 },
      { "name": "Coca-Cola 2L", "sku": "CC-2L", "price": 8.5, "quantity": 1 }
    ]
  },
  {
    "_id": "33",
    "name": "Carlos Lima",
    "created_at": "2025-08-01T12:45:00Z",
    "products": [
      { "name": "Coxinha", "sku": "CX-001", "price": 6.0, "quantity": 2 },
      { "name": "Esfiha de Carne", "sku": "EF-001", "price": 4.5, "quantity": 3 }
    ]
  },
  {
    "_id": "34",
    "name": "Ana Souza",
    "created_at": "2025-08-01T13:00:00Z",
    "products": [
      { "name": "Sanduíche Natural", "sku": "SN-002", "price": 9.0, "quantity": 1 },
      { "name": "Suco Natural", "sku": "SN-001", "price": 7.0, "quantity": 1 }
    ]
  },
  {
    "_id": "35",
    "name": "João Silva",
    "created_at": "2025-08-01T15:30:00Z",
    "products": [
      { "name": "Açaí 500ml", "sku": "AC-500", "price": 12.0, "quantity": 1 },
      { "name": "Água Mineral", "sku": "AG-001", "price": 3.0, "quantity": 1 }
    ]
  },
  {
    "_id": "36",
    "name": "Bruna Rocha",
    "created_at": "2025-08-02T08:15:00Z",
    "products": [
      { "name": "Cappuccino", "sku": "CP-001", "price": 6.0, "quantity": 1 },
      { "name": "Croissant", "sku": "CR-001", "price": 7.5, "quantity": 1 }
    ]
  },
  {
    "_id": "37",
    "name": "Pedro Santos",
    "created_at": "2025-08-02T09:00:00Z",
    "products": [
      { "name": "Café Expresso", "sku": "CF-001", "price": 4.0, "quantity": 2 },
      { "name": "Pão de Queijo", "sku": "PQ-001", "price": 5.0, "quantity": 2 }
    ]
  },
  {
    "_id": "38",
    "name": "Maria Oliveira",
    "created_at": "2025-08-02T12:20:00Z",
    "products": [
      { "name": "Coxinha", "sku": "CX-001", "price": 6.0, "quantity": 3 },
      { "name": "Guaraná 1L", "sku": "GUA-1L", "price": 6.5, "quantity": 2 }
    ]
  },
  {
    "_id": "39",
    "name": "Carlos Lima",
    "created_at": "2025-08-02T12:35:00Z",
    "products": [
      { "name": "Torta de Frango", "sku": "TF-001", "price": 8.0, "quantity": 1 },
      { "name": "Coca-Cola 2L", "sku": "CC-2L", "price": 8.5, "quantity": 1 }
    ]
  },
  {
    "_id": "40",
    "name": "João Silva",
    "created_at": "2025-08-02T16:10:00Z",
    "products": [
      { "name": "Coxinha", "sku": "CX-001", "price": 6.0, "quantity": 2 },
      { "name": "Suco Natural", "sku": "SN-001", "price": 7.0, "quantity": 1 }
    ]
  },
  {
    "_id": "41",
    "name": "Lucia Costa",
    "created_at": "2025-08-03T10:45:00Z",
    "products": [
      { "name": "Vitamina de Frutas", "sku": "VF-001", "price": 8.5, "quantity": 1 },
      { "name": "Pastel de Frango", "sku": "PF-001", "price": 5.5, "quantity": 1 }
    ]
  },
  {
    "_id": "42",
    "name": "Roberto Ferreira",
    "created_at": "2025-08-03T11:30:00Z",
    "products": [
      { "name": "Pão de Queijo", "sku": "PQ-001", "price": 5.0, "quantity": 4 },
      { "name": "Café Expresso", "sku": "CF-001", "price": 4.0, "quantity": 1 }
    ]
  },
  {
    "_id": "43",
    "name": "Ana Souza",
    "created_at": "2025-08-03T12:00:00Z",
    "products": [
      { "name": "Coxinha", "sku": "CX-001", "price": 6.0, "quantity": 1 },
      { "name": "Esfiha de Carne", "sku": "EF-001", "price": 4.5, "quantity": 2 }
    ]
  },
  {
    "_id": "44",
    "name": "João Silva",
    "created_at": "2025-08-03T18:15:00Z",
    "products": [
      { "name": "Açaí 500ml", "sku": "AC-500", "price": 12.0, "quantity": 1 },
      { "name": "Guaraná 1L", "sku": "GUA-1L", "price": 6.5, "quantity": 1 }
    ]
  },
  {
    "_id": "45",
    "name": "Fernanda Alves",
    "created_at": "2025-08-04T09:20:00Z",
    "products": [
      { "name": "Sanduíche Natural", "sku": "SN-002", "price": 9.0, "quantity": 1 },
      { "name": "Agua Mineral", "sku": "AG-001", "price": 3.0, "quantity": 1 }
    ]
  },
  {
    "_id": "46",
    "name": "Maria Oliveira",
    "created_at": "2025-08-04T12:45:00Z",
    "products": [
      { "name": "Pão de Queijo", "sku": "PQ-001", "price": 5.0, "quantity": 5 },
      { "name": "Coca-Cola 2L", "sku": "CC-2L", "price": 8.5, "quantity": 1 }
    ]
  },
  {
    "_id": "47",
    "name": "Carlos Lima",
    "created_at": "2025-08-04T13:10:00Z",
    "products": [
      { "name": "Coxinha", "sku": "CX-001", "price": 6.0, "quantity": 3 },
      { "name": "Suco Natural", "sku": "SN-001", "price": 7.0, "quantity": 1 }
    ]
  },
  {
    "_id": "48",
    "name": "Marcos Pereira",
    "created_at": "2025-08-04T15:00:00Z",
    "products": [
      { "name": "Cappuccino", "sku": "CP-001", "price": 6.0, "quantity": 2 },
      { "name": "Croissant", "sku": "CR-001", "price": 7.5, "quantity": 1 }
    ]
  },
  {
    "_id": "49",
    "name": "João Silva",
    "created_at": "2025-08-05T11:30:00Z",
    "products": [
      { "name": "Coxinha", "sku": "CX-001", "price": 6.0, "quantity": 5 },
      { "name": "Guaraná 1L", "sku": "GUA-1L", "price": 6.5, "quantity": 2 }
    ]
  },
  {
    "_id": "50",
    "name": "Bruna Rocha",
    "created_at": "2025-08-05T14:20:00Z",
    "products": [
      { "name": "Torta de Frango", "sku": "TF-001", "price": 8.0, "quantity": 1 },
      { "name": "Vitamina de Frutas", "sku": "VF-001", "price": 8.5, "quantity": 1 }
    ]
  }
]


dataset_id = "teste3-465312.TesteBigQuery.VendasLBC"

# 4. Inserir dados no BigQuery:
def inserir_dados_bigquery():
   try:
      
      # Nao possui controle de ids, logo e bom gerar uma flag no banco que gera os dados para nao salvar ids repetidos
      # para nao perder a eficiencia do insert_rows_json
      cliente.insert_rows_json(
         dataset_id,
         exemplos,
         
      )
    
      print("Dados inseridos com sucesso")
   except Exception as e:
      print(f"Erro ao inserir dados: {e}")

# 4.1 Inserir dados usando Job Loading (permite UPDATE/DELETE imediatos)
def inserir_dados_bigquery_job_loading():
    """Insere dados usando job loading - permite UPDATE/DELETE imediatos"""
    try:
        # Buscar o schema da tabela para evitar conflitos
        table_schema = cliente.get_table(dataset_id).schema
       
        
        with open("exemplos.json", 'rb') as source_file:
            job = cliente.load_table_from_file(
                source_file,
                dataset_id,
                job_config=bigquery.LoadJobConfig(
                    source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
                    schema=table_schema,  # Schema definido manualmente
                    write_disposition=bigquery.WriteDisposition.WRITE_APPEND  # Adiciona aos dados existentes
                )
            )
        
        # Aguardar o job terminar
        job.result()
        
        
        print("✓ Dados inseridos via Job Loading - UPDATE/DELETE disponíveis imediatamente!")
        
    except Exception as e:
        print(f"✗ Erro ao inserir dados via job loading: {e}")

# 4.2 Inserir dados usando query INSERT (permite UPDATE/DELETE imediatos)
def inserir_dados_bigquery_via_query():
    """Insere dados usando INSERT query - permite UPDATE/DELETE imediatos"""
    try:
        
        valores_insert = []
        for exemplo in exemplos: 
            # Converter products para formato JSON string
            struct = f"STRUCT('{exemplo['name']}' as name, '{exemplo['sku']}' as sku, {exemplo['price']} as price, {exemplo['quantity']} as quantity)"
            products_json = str(exemplo['products']).replace("'", '"')
            
            valor = f"""(
                '{exemplo['_id']}',
                '{exemplo['name']}',
                TIMESTAMP('{exemplo['created_at']}'),
                PARSE_JSON('{products_json}')
            )"""
            valores_insert.append(valor)
        
        valores_str = ',\n'.join(valores_insert)
        
        query = f"""
        INSERT INTO `{dataset_id}` (_id, name, created_at, products)
        VALUES {valores_str}
        """
        
        
        job = cliente.query(query)
        result = job.result()
        
        print("✓ Dados inseridos via INSERT query - UPDATE/DELETE disponíveis imediatamente!")
        
    except Exception as e:
        print(f"✗ Erro ao inserir dados via query: {e}")

      
# 5. Ler dados da tabela - FORMA SIMPLES SEM PANDAS:

def ler_dados_bigquery():
   """Visualização simples dos dados - SEM pandas"""
   try:
      query = f"""
      SELECT * FROM `{dataset_id}`
      ORDER BY created_at
      """
      job = cliente.query(query)
      results = job.result()
      
      print("📊 DADOS DA TABELA:")
      print("=" * 100)
      
      contador = 0
      for row in results:
          contador += 1
          print(f"\n🔖 REGISTRO {contador}:")
          print(f"   ID: {row._id}")
          print(f"   Cliente: {row.name}")
          print(f"   Data: {row.created_at}")
          
          # Mostrar produtos de forma simples
          if row.products:
              print(f"   Produtos: {row.products}")
          else:
              print(f"   Produtos: Nenhum")
          
          print("-" * 60)
      
      print(f"\n📊 Total de registros encontrados: {contador}")
      
   except Exception as e:
      print(f"Erro ao ler dados: {e}")


# 5.1. Visualização ainda mais simples - só os valores
def ler_dados_simples():
   """Mostra apenas os valores básicos"""
   try:
      query = f"""
      SELECT _id, name, created_at FROM `{dataset_id}`
      ORDER BY created_at
      """
      job = cliente.query(query)
      results = job.result()
      
      print("📋 RESUMO DOS PEDIDOS:")
      print("=" * 60)
      print(f"{'ID':<5} {'CLIENTE':<20} {'DATA':<25}")
      print("-" * 60)
      
      contador = 0
      for row in results:
          contador += 1
          data_str = str(row.created_at) if row.created_at else "N/A"
          print(f"{row._id:<5} {row.name:<20} {data_str:<25}")
      
      print("-" * 60)
      print(f"Total: {contador} registros")
      
   except Exception as e:
      print(f"Erro ao ler dados simples: {e}")


# 5.2. Mostrar apenas um registro para teste
def ler_um_registro():
   """Mostra apenas um registro para verificar se está funcionando"""
   try:
      query = f"""
      SELECT * FROM `{dataset_id}`
      LIMIT 1
      """
      job = cliente.query(query)
      results = job.result()
      
      print("🔍 TESTANDO - APENAS 1 REGISTRO:")
      print("=" * 50)
      
      for row in results:
          print(f"ID: {row._id}")
          print(f"Cliente: {row.name}")
          print(f"Data: {row.created_at}")
          print(f"Produtos: {row.products}")
          break
      
   except Exception as e:
      print(f"Erro ao ler um registro: {e}")


# 5.3. Contar quantos registros existem
def contar_registros():
   """Apenas conta quantos registros existem na tabela"""
   try:
      query = f"""
      SELECT COUNT(*) as total FROM `{dataset_id}`
      """
      job = cliente.query(query)
      results = job.result()
      
      for row in results:
          print(f"📊 Total de registros na tabela: {row.total}")
          break
      
   except Exception as e:
      print(f"Erro ao contar registros: {e}")


# 5.4. Buscar pedido específico - FORMA SIMPLES
def buscar_pedido_simples(id_pedido):
   """Busca um pedido específico sem pandas"""
   try:
      query = f"""
      SELECT * FROM `{dataset_id}`
      WHERE _id = '{id_pedido}'
      """
      job = cliente.query(query)
      results = job.result()
      
      encontrou = False
      for row in results:
          encontrou = True
          print(f"🔍 PEDIDO ENCONTRADO - ID: {id_pedido}")
          print("=" * 50)
          print(f"Cliente: {row.name}")
          print(f"Data: {row.created_at}")
          print(f"Produtos: {row.products}")
          break
      
      if not encontrou:
          print(f"❌ Nenhum pedido encontrado com ID '{id_pedido}'")
      
   except Exception as e:
      print(f"Erro ao buscar pedido: {e}")


# 5.5. Mostrar produtos de um pedido específico
def ver_produtos_pedido(id_pedido):
   """Mostra apenas os produtos de um pedido específico"""
   try:
      query = f"""
      SELECT 
          produto.name as produto,
          produto.sku,
          produto.price as preco,
          produto.quantity as quantidade
      FROM `{dataset_id}`,
      UNNEST(products) as produto
      WHERE _id = '{id_pedido}'
      """
      job = cliente.query(query)
      results = job.result()
      
      print(f"🛒 PRODUTOS DO PEDIDO {id_pedido}:")
      print("=" * 50)
      
      contador = 0
      total_pedido = 0
      for row in results:
          contador += 1
          valor_item = row.preco * row.quantidade
          total_pedido += valor_item
          
          print(f"{contador}. {row.produto}")
          print(f"   SKU: {row.sku}")
          print(f"   Preço: R$ {row.preco:.2f}")
          print(f"   Quantidade: {row.quantidade}")
          print(f"   Subtotal: R$ {valor_item:.2f}")
          print()
      
      if contador == 0:
          print(f"❌ Nenhum produto encontrado para o pedido '{id_pedido}'")
      else:
          print(f"💰 TOTAL DO PEDIDO: R$ {total_pedido:.2f}")
      
   except Exception as e:
      print(f"Erro ao ver produtos do pedido: {e}")




# 5. Deletar dados da tabela de maneira geral: 

def deletar_dados_bigquery():
   try:
      cliente.delete_table(dataset_id)
      print("Dados deletados com sucesso")
   except Exception as e:
      print(f"Erro ao deletar dados: {e}")


# 5.1.1 Deletar um registro específico por ID
def deletar_por_id(id_pedido):
    """Deleta um pedido específico pelo ID"""
    try:
        query = f"""
        DELETE FROM `{dataset_id}`
        WHERE _id = '{id_pedido}'
        """
        
        job = cliente.query(query)
        result = job.result()
        
        print(f"✓ Pedido com ID '{id_pedido}' deletado com sucesso!")
        print(f"Total de linhas afetadas: {job.num_dml_affected_rows}")
        
    except Exception as e:
        print(f"✗ Erro ao deletar pedido: {e}")


# 5.1.2 Deletar por nome do cliente
def deletar_por_cliente(nome_cliente):
    """Deleta todos os pedidos de um cliente específico"""
    try:
        query = f"""
        DELETE FROM `{dataset_id}`
        WHERE name = '{nome_cliente}'
        """
        
        job = cliente.query(query)
        result = job.result()
        
        print(f"✓ Todos os pedidos do cliente '{nome_cliente}' foram deletados!")
        print(f"Total de linhas afetadas: {job.num_dml_affected_rows}")
        
    except Exception as e:
        print(f"✗ Erro ao deletar pedidos do cliente: {e}")


# 5.1.3 Deletar por data específica
def deletar_por_data(data_inicio, data_fim=None):
    """Deleta pedidos dentro de um período específico"""
    try:
        if data_fim:
            # Deletar entre duas datas
            query = f"""
            DELETE FROM `{dataset_id}`
            WHERE created_at BETWEEN '{data_inicio}' AND '{data_fim}'
            """
            print(f"Deletando pedidos entre {data_inicio} e {data_fim}")
        else:
            # Deletar apenas de uma data específica
            query = f"""
            DELETE FROM `{dataset_id}`
            WHERE DATE(created_at) = '{data_inicio}'
            """
            print(f"Deletando pedidos da data {data_inicio}")
        
        job = cliente.query(query)
        result = job.result()
        
        print(f"✓ Pedidos deletados com sucesso!")
        print(f"Total de linhas afetadas: {job.num_dml_affected_rows}")
        
    except Exception as e:
        print(f"✗ Erro ao deletar pedidos por data: {e}")


# 5.1.4 Deletar pedidos com produtos específicos
def deletar_por_produto(nome_produto):
    """Deleta pedidos que contêm um produto específico"""
    try:
        # Primeiro, vamos consultar os IDs dos pedidos que contêm o produto
        query_consulta = f"""
        SELECT DISTINCT _id
        FROM `{dataset_id}`,
        UNNEST(products) AS produto
        WHERE produto.name = '{nome_produto}'
        """
        
        # Executar consulta para obter os IDs
        job_consulta = cliente.query(query_consulta)
        results = job_consulta.result()
        
        ids_para_deletar = [row._id for row in results]
        
        if not ids_para_deletar:
            print(f"Nenhum pedido encontrado com o produto '{nome_produto}'")
            return
        
        # Criar lista de IDs para a query DELETE
        ids_str = "', '".join(ids_para_deletar)
        
        query_delete = f"""
        DELETE FROM `{dataset_id}`
        WHERE _id IN ('{ids_str}')
        """
        
        job_delete = cliente.query(query_delete)
        result = job_delete.result()
        
        print(f"✓ Pedidos com produto '{nome_produto}' deletados com sucesso!")
        print(f"IDs deletados: {ids_para_deletar}")
        print(f"Total de linhas afetadas: {job_delete.num_dml_affected_rows}")
        
    except Exception as e:
        print(f"✗ Erro ao deletar pedidos por produto: {e}")


# 5.1.5 Deletar com múltiplas condições
def deletar_por_multiplas_condicoes(nome_cliente=None, data_inicio=None, valor_minimo=None):
    """Deleta pedidos baseado em múltiplas condições"""
    try:
        # Construir a query dinamicamente baseada nos parâmetros fornecidos
        condicoes = []
        
        if nome_cliente:
            condicoes.append(f"name = '{nome_cliente}'")
        
        if data_inicio:
            condicoes.append(f"created_at >= '{data_inicio}'")
        
        if valor_minimo:
            # Para valor, precisamos calcular o total dos produtos
            condicoes.append(f"""
            (SELECT SUM(produto.price * produto.quantity) 
             FROM UNNEST(products) AS produto) >= {valor_minimo}
            """)
        
        if not condicoes:
            print("❌ Nenhuma condição fornecida!")
            return
        
        where_clause = " AND ".join(condicoes)
        
        query = f"""
        DELETE FROM `{dataset_id}`
        WHERE {where_clause}
        """
        
        print(f"Executando query: {query}")
        
        job = cliente.query(query)
        result = job.result()
        
        print(f"✓ Pedidos deletados com base nas condições especificadas!")
        print(f"Total de linhas afetadas: {job.num_dml_affected_rows}")
        
    except Exception as e:
        print(f"✗ Erro ao deletar com múltiplas condições: {e}")


# 6 Atualizar os dados da tabela: 
def atualizar_dados_bigquery_setar_novo_nome_no_pedido(id_pedido, novo_nome):
   try:
      query = f"""
      UPDATE `{dataset_id}`
      SET name = '{novo_nome}'
      WHERE _id = '{id_pedido}'
      """
      
      print("executando query: ", query)
      
      job = cliente.query(query)
      result = job.result()
      
      print("Dados atualizados com sucesso")
      

   except Exception as e:
      print(f"Erro ao atualizar dados: {e}")
   

if __name__ == "__main__":
    
    inserir_dados_bigquery()
    inserir_dados_bigquery_job_loading()
    inserir_dados_bigquery_via_query()
    ler_dados_bigquery()
    ler_dados_simples()
    contar_registros()
    buscar_pedido_simples("1")
    ver_produtos_pedido("1")
    atualizar_dados_bigquery_setar_novo_nome_no_pedido("1", "João Silva Atualizado")
    buscar_pedido_simples("1")
    deletar_por_id("2")
    contar_registros()

