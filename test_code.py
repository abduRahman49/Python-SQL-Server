from database import DatabaseInterface


db_instance = DatabaseInterface(server='GSIETECHP005\SQLEXPRESS',
                                database='AdventureWorksLT2012',
                                username='Lynx',
                                password='passer@123')

result = db_instance.call_proc(proc_name='my_proc', params=('680'))

print("Ceci est le result set retourné par la procédure stockée")
print()
print(result)
print()
print("Nous pouvons parcourir le result et afficher les valeurs des propriétés du dictionnaire")
print()
for item in result:
    print(item.get("name"))