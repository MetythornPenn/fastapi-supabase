from supabase import create_client, Client

SUPABASE_URL=''
SUPABASE_KEY=''

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Select all rows from the table
results = supabase.table('demo-table').select('*').execute()
print(results)

# Insert a new row into the table
# new_row = {'first_name': 'John Doe'}
# results = supabase.table('demo-table').insert(new_row).execute()
# print(results)

# Update a row in the table
# updated_row = {'first_name': 'Jane Doe'}
# results = supabase.table('demo-table').update(updated_row).eq('id', 2).execute()
# print(results)

# Delete a row from the table
# results = supabase.table('demo-table').delete().eq('id', 2).execute()
# print(results)    

# response = supabase.storage.from_('demo-bucket').get_public_url('eric-image.png')


# response = supabase.storage.from_('demo-bucket').get_public_url('eric-image.png')

# print(response)


# image: UploadFile = File(...)
# file_contents = await image.read()
# supabase.storage.from_('demo-bucket').upload("new-image.png", file_contents)
