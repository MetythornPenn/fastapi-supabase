import os      
from dotenv import load_dotenv
from typing import Optional
from supabase import create_client, Client 

load_dotenv()

# retrieve supabase url and key from env var 
SUPABASE_URL: Optional[str] = os.getenv('SUPABASE_URL')
SUPABASE_KEY: Optional[str] = os.getenv('SUPABASE_KEY')

# create supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# execute query
results = supabase.table('demo-table').select('*').execute() 

print(results)

