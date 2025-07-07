import os
from google.cloud import bigquery
from google.oauth2 import service_account

class BigQuery:
    
    def __init__(self, credentials_path: str = None):
        if credentials_path is None or (not os.path.exists(credentials_path)):
            raise ValueError("credentials_path is required")
        
        self.__credentials_path = credentials_path
        self.__client: bigquery.Client = None
     
    def __del__(self):
        self.terminate()
    
    def terminate(self) -> None:
        if self.__client:
            self.__client.close()
            self.__client = None
        print("BigQuery client terminated")
        
            
    def initialize(self, project_id: str = None) -> bool:
        try:
            credentials = service_account.Credentials.from_service_account_file(self.__credentials_path)
            self.__client = bigquery.Client(credentials=credentials, project=project_id)
            print("BigQuery client initialized")
            return True
        except Exception as e:
            print(e)
            raise Exception("Error initializing BigQuery client", e)
    
        
    def get_client(self) -> bigquery.Client:
        if self.__client is None:
            raise Exception("BigQuery client not initialized")
        
        return self.__client
    
    def get_dataset(self, dataset_id: str) -> bigquery.Dataset:
        try:
            return self.get_client().get_dataset(dataset_id)
        except Exception as e:
            print(e)
            raise Exception("Error getting BigQuery dataset", e)
        
    
    def get_table(self, dataset_id: str, table_id: str) -> bigquery.Table:
        try:
            table_ref = f"{dataset_id}.{table_id}"  
            return self.get_client().get_table(table_ref)
        except Exception as e:
            raise RuntimeError(f"Error getting table '{table_id}' from dataset '{dataset_id}'") from e
    
    def make_query(self, query: str) -> bigquery.table.RowIterator:
        try:
            job = self.get_client().query(query)
            result = job.result()
            return result.to_dataframe()
        except Exception as e:
            raise RuntimeError("Error executing BigQuery query") from e
        
    def set_label(self, table: bigquery.Table, labels: dict) -> None:
        try:
            table.labels = labels
            self.get_client().update_table(table, ["labels"])
        except Exception as e:
            raise RuntimeError(f"Error setting labels for table {table.table_id}") from e
        
        
    def set_data(self, table: bigquery.Table, data: list) -> None:
        try:
            client = self.get_client()
            client.insert_rows_json(table, data)
        except Exception as e:
            raise RuntimeError(f"Error setting data for table {table.table_id}") from e
        
        
    def get_data(self, table: bigquery.Table) -> list:
        try:
            return self.get_client().list_rows(table)
        except Exception as e:
            raise RuntimeError(f"Error getting data for table {table.table_id}") from e
        
        
    def saveLoginLogsInBigQuery(self, logs: list) -> None:
        try:
            print(f"🔧 BigQuery: Iniciando salvamento de {len(logs)} logs de login...")
            
            if not logs:
                print("⚠️ BigQuery: Nenhum log de login para salvar")
                return
                
            print("🔧 BigQuery: Obtendo tabela GASMONITOR_APP_LOGIN_LOGS...")
            login_table = self.get_table(dataset_id="GasMonitorLogs", table_id="GASMONITOR_APP_LOGIN_LOGS")
            print(f"✅ BigQuery: Tabela obtida - {login_table.table_id}")
            
            print("🔧 BigQuery: Inserindo dados...")
            errors = self.get_client().insert_rows_json(login_table, logs)
            
            if errors:
                print(f"❌ BigQuery: Erros ao inserir logs de login: {errors}")
                raise RuntimeError(f"Erros ao inserir logs de login no BigQuery: {errors}")
            else:
                print(f"✅ BigQuery: Logs de login salvos com sucesso: {len(logs)} registros")
                
        except Exception as e:
            print(f"❌ BigQuery: Erro ao salvar logs de login: {e}")
            raise RuntimeError(f"Error saving login logs in big query: {e}")
        
    
    def saveFrequencyLogsInBigQuery(self, logs: list) -> None:
        try:
            print(f"🔧 BigQuery: Iniciando salvamento de {len(logs)} logs de frequência...")
            
            if not logs:
                print("⚠️ BigQuery: Nenhum log de frequência para salvar")
                return

            print("🔧 BigQuery: Obtendo tabela GASMONITOR_APP_FREQUECY_LOGS...")
            frequency_table = self.get_table(dataset_id="GasMonitorLogs", table_id="GASMONITOR_APP_FREQUECY_LOGS")
            print(f"✅ BigQuery: Tabela obtida - {frequency_table.table_id}")
            
            print("🔧 BigQuery: Inserindo dados...")
            errors = self.get_client().insert_rows_json(frequency_table, logs)
            
            if errors:
                print(f"❌ BigQuery: Erros ao inserir logs de frequência: {errors}")
                raise RuntimeError(f"Erros ao inserir logs de frequência no BigQuery: {errors}")
            else:
                print(f"✅ BigQuery: Logs de frequência salvos com sucesso: {len(logs)} registros")
                
        except Exception as e:
            print(f"❌ BigQuery: Erro ao salvar logs de frequência: {e}")
            raise RuntimeError(f"Error saving frequency logs in big query: {e}")
        
    def saveUsersInBigQuery(self, users: list) -> None:
        try:
            print(f"🔧 BigQuery: Iniciando salvamento de {len(users)} usuários...")
            
            if not users:
                print("⚠️ BigQuery: Nenhum usuário para salvar")
                return
            schema  = self.get_table_schema(dataset_id="GasMonitorLogs", table_id="GASMONITOR_LOGS_USUARIOS")
            print(schema)
            
            users_table = self.get_table(dataset_id="GasMonitorLogs", table_id="GASMONITOR_LOGS_USUARIOS")
            print(f"✅ BigQuery: Tabela obtida - {users_table.table_id}")
            
            print("🔧 BigQuery: Inserindo dados...")
            errors = self.get_client().insert_rows_json(users_table, users)
            
            if errors:
                print(f"❌ BigQuery: Erros ao inserir usuários: {errors}")
            else: 
                print(f"✅ BigQuery: Usuários salvos com sucesso: {len(users)} registros")
                
        except Exception as e:
            print(f"❌ BigQuery: Erro ao salvar usuários: {e}")
            raise RuntimeError(f"Error saving users in big query: {e}")
        
        
    def test_connection(self) -> bool:
        """Testa se a conexão com BigQuery está funcionando"""
        try:
            print("🔧 BigQuery: Testando conexão...")
            
            # Testa se consegue listar datasets
            datasets = list(self.get_client().list_datasets())
            print(f"✅ BigQuery: Conexão OK - {len(datasets)} datasets encontrados")
            
            # Testa se consegue acessar o dataset específico
            try:
                dataset = self.get_dataset("GasMonitorLogs")
                print(f"✅ BigQuery: Dataset GasMonitorLogs acessível")
                
                # Testa se consegue listar tabelas
                tables = list(self.get_client().list_tables(dataset))
                print(f"✅ BigQuery: {len(tables)} tabelas encontradas no dataset")
                
                for table in tables:
                    print(f"  - {table.table_id}")
                    
                return True
                
            except Exception as e:
                print(f"❌ BigQuery: Erro ao acessar dataset GasMonitorLogs: {e}")
                return False
                
        except Exception as e:
            print(f"❌ BigQuery: Erro na conexão: {e}")
            return False

    def get_table_schema(self, dataset_id: str, table_id: str) -> list:
        """Obtém o esquema (campos) de uma tabela específica"""
        try:
            table = self.get_table(dataset_id, table_id)
            schema = table.schema
            
            print(f"📋 BigQuery: Esquema da tabela {table_id}:")
            fields = []
            for field in schema:
                field_info = {
                    "name": field.name,
                    "type": field.field_type,
                    "mode": field.mode
                }
                fields.append(field_info)
                print(f"  - {field.name} ({field.field_type}, {field.mode})")
            
            return fields
            
        except Exception as e:
            print(f"❌ BigQuery: Erro ao obter esquema da tabela {table_id}: {e}")
            return []
        


