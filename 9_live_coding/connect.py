import psycopg2
import names
conn = psycopg2.connect(dbname= 'qa_students_1',
                        user = 'qa_student_1_u_1',
                        password= '123',
                        host='159.69.151.13',
                        port='5056')
cursor = conn.cursor()
# if conn:
#     print('Connect -- !')
#
#     select_query = "select * from students;"
#
#     sql_select = '''select * from students'''
#
#     exeq_query = cursor.execute(select_query)
#
#     f_query = cursor.fetchall()
#     print(f_query)
#
#
#     for i in f_query:
#         u_name = "Name = " + i[1]
#         u_email = "Email = " + i[2]
#         u_reg_time = "Time = " + str(i[4])
#
#         print(i)
#         print(u_name, u_email, u_reg_time)
#
#     conn.commit()
#     conn.close()

# for i in range (0, 10)
# if conn:
#
#     print('Connected -- !')
#     create_query =  'create table users_python (' \
#                     'id serial primary key' \
#                     'name varchar (40)'\
#                     'phone varchar(24)'\
#                     'country varchar(40)'\
#                     'city varchar(40)'\
#                     'salary int'\
#                     ')'
#     cursor.exequte(create_query)
#     conn.comit()
#     conn.close()

cities = ['Bavaria', 'Koln', 'Berlin']
for i in range (0, 10)
if conn:

    print('Connected -- !')

    name = names.get_first_name()
    phone = '+38 066 69 000 59'+ str(i)
    country = 'Germany'
    city =



    create_query =  'insert into barinova_python(name,)'\
                    'email,'\
                    'phone,'\
                    'country,'\
                    'city,'\
                    'salary)'\
                    'values ()'




    cursor.exequte(create_query)
    conn.comit()
    conn.close()




