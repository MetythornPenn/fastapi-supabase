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

"""--- insert a record into table ---"""
new_row = {'first_name': 'xyber'}
supabase.table('demo-table').insert(new_row).execute()

"""---update record---"""
new_row = {'first_name': 'punk'}
supabase.table('demo-table').update(new_row).eq('id', 2).execute()

"""---delete record"""
supabase.table('demo-table').delete().eq('id', 4).execute()


"""--- fetch all records---"""
results = supabase.table('demo-table').select('*').execute() 

print(results)

