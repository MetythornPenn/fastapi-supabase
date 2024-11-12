# Supabase + FastAPI

> Tech Stack:
>
>   backend : Supabase + FastAPI
>
>   frontend : NextJS 


```bash
create table employees(
    id serial primary key,
    first_name text not null,
    last_name text not null,
    email text unique not null,
    salary numeric not null,
    image_url text,
    is_active boolean default true
)

```

## Reference 
- [youtube tutorial](https://www.youtube.com/watch?v=PlZcgIMk3aw)
- [supabase project](https://supabase.com/dashboard/project/aqauiqkknxcunkuimzfo/editor/29183?schema=public)
- [supabase python doc](https://supabase.com/docs/reference/python/introduction)