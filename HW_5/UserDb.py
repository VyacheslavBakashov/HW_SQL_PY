import psycopg2
from psycopg2 import Error


class UserDb:
    """Класс для пользователя базой данных клиентов"""
    columns = ['last_name', 'first_name', 'email', 'phone_num']

    def __init__(self, name_db_, login_, password):
        self.name_db = name_db_
        self.login = login_
        self.password = password
        self.conn = psycopg2.connect(database=self.name_db, user=self.login, password=self.password)
        self.cur = self.conn.cursor()

    def create_tables(self):
        self.cur.execute("""
                /*DROP TABLE IF EXISTS phone;
                DROP TABLE IF EXISTS client;*/
                CREATE TABLE IF NOT EXISTS client(
                    client_id SERIAL PRIMARY KEY,
                    last_name VARCHAR(20) NOT NULL,
                    first_name VARCHAR(20) NOT NULL,
                    email VARCHAR(30) NOT NULL UNIQUE,
                        CONSTRAINT email_check
                        CHECK (email LIKE '%_@_%.__%'),
                    UNIQUE (last_name, first_name, email)
                );
                CREATE TABLE IF NOT EXISTS phone(
                    id SERIAL PRIMARY KEY,
                    client_id INTEGER NOT NULL REFERENCES client(client_id) ON DELETE CASCADE,
                    phone_num VARCHAR(20) NOT NULL,
                        CONSTRAINT check_num_phone
                        CHECK (phone_num LIKE '+7(___) ___-__-__')
                );
                """)
        self.conn.commit()

    def delete_tables(self):
        self.cur.execute("""
                DROP TABLE IF EXISTS phone;
                DROP TABLE IF EXISTS client;
                """)
        self.conn.commit()

    def add_client(self, last_name, first_name, email, phone_num=None):
        """Метод добавляет одного клиента"""
        try:
            self.cur.execute("""
                    INSERT INTO client(last_name, first_name, email)
                    VALUES (%s, %s, %s);
                    """, (last_name.title(), first_name.title(), email.lower()))
        except Error as err:
            print(f'--> {err}')
            self.conn.rollback()
        else:
            self.conn.commit()
            print(f'+ Клиент {last_name.title()} {first_name.title()} добавлен в базу')
        if phone_num:
            try:
                self.cur.execute("""
                        INSERT INTO phone(client_id, phone_num)
                        VALUES ((SELECT client_id 
                                   FROM client
                                  WHERE last_name = %s
                                    AND first_name = %s
                                    AND email = %s
                                ), %s);
                        """, (last_name.title(), first_name.title(), email.lower(), phone_num))
            except psycopg2.errors.CheckViolation:
                print(f'\n--> Номер не добавлен для клиента {last_name.title()} {first_name.title()}\n'
                      f'    Неверный формат номера телефона. Должен быть в виде +7(XXX) XXX-XX-XX <--\n')
                self.conn.rollback()
            else:
                self.conn.commit()

    def add_clients_list(self, clients):
        """Метод добавляет клиентов из словаря или списка"""
        if not isinstance(clients[0], dict):
            clients_list = [dict(zip(self.columns, i)) for i in clients]
        else:
            clients_list = clients
        for client in clients_list:
            self.add_client(**client)

    def _check_phone_num(self, client_id, phone_num):
        """Метод проверяет наличие телефона в базе данных"""
        self.cur.execute("""
                        SELECT (client_id, phone_num)
                          FROM phone
                         WHERE client_id = %s AND phone_num = %s;
                        """, (client_id, phone_num))
        return self.cur.fetchone()

    def add_phone_num(self, client_id, phone_number):
        if self._check_phone_num(client_id, phone_number):
            print(f'--> Номер не добавлен, {phone_number} для клиента с ID={client_id} уже существует в базе данных')
            return
        try:
            self.cur.execute("""
                            INSERT INTO phone(client_id, phone_num)
                            VALUES (%s, %s);
                            """, (client_id, phone_number))
        except Error as err:
            print(f'\n--> {err}')
            self.conn.rollback()
        else:
            print(f'+ Номер телефона для клиента с ID={client_id} успешно добавлен')
            self.conn.commit()

    def delete_phone_num(self, client_id, phone_num):
        if not self._check_phone_num(client_id, phone_num):
            return print(f'\n--> Ошибка. Номер не удалён. Проверьте входные данные\n')
        else:
            print(f'+ Номер {phone_num} для клиента с ID={client_id} успешно удален')
        self.cur.execute("""
                        DELETE FROM phone
                         WHERE client_id = %s
                           AND phone_num = %s;
                        """, (client_id, phone_num))
        self.conn.commit()

    def change_client(self, client_id, last_name=None, first_name=None, email=None, phone_num=None):
        """Изменение данных клиента, для номера телефона можно удалить или добавить"""
        new_data = (last_name, first_name, email)
        cur_data = self.get_data(client_id)
        if any(new_data) and cur_data:
            upd = dict((c[0], n) if n else (c[0], c[1]) for c, n in zip(cur_data.items(), new_data))
            try:
                self.cur.execute("""
                            UPDATE client
                               SET last_name = %s, first_name = %s, email =  %s
                             WHERE client_id = %s;
                            """, (upd['last_name'].title(), upd['first_name'].title(), upd['email'].lower(), client_id))
            except Error as err:
                print(f'\n--> {err}')
                self.conn.rollback()
            else:
                print(f'\t+ Данные для клиента с ID={client_id} успешно обновлены')
                self.conn.commit()
        if phone_num:
            com_desc = {'a': 'add_phone', 'd': 'delete_phone', 'q': 'exit (do nothing)'}
            print('\tЧто вы хотите сделать с введённым телефоном:', *[f'\t{k}: {v}' for k, v in com_desc.items()],
                  sep='\n')
            while True:
                command = input('\tВведите команду: ').strip().lower()
                if command not in com_desc:
                    print('Неверная команда',)
                    continue
                elif command in 'a':
                    self.add_phone_num(client_id, phone_num)
                    break
                elif command in 'd':
                    self.delete_phone_num(client_id, phone_num)
                    break
                elif command in 'q':
                    break

    def get_data(self, client_id):
        """Получение всех данных клиента по ID в виде словаря"""
        self.cur.execute("""
                        SELECT last_name, first_name, email FROM client
                        WHERE client_id = %s;
                        """, (client_id,))
        some_data = self.cur.fetchone()
        if not some_data:
            print('\n--> Неверный client ID для получения данных клиента<--\n')
            return
        self.cur.execute("""
                                SELECT phone_num FROM phone WHERE client_id = %s;
                                """, (client_id,))
        phones = list(map(lambda x: x[0], self.cur.fetchall()))
        full_data = some_data + (phones,)
        return {k: v for k, v in zip(self.columns, full_data)}

    def delete_client(self, client_id):
        """Удаление всех данных клиента по id"""
        try:
            self.cur.execute("""
                                 DELETE FROM client WHERE client_id = %s;
                             """, (client_id,))
        except Error as err:
            print(f'\n--> {err}')
        else:
            print(f'+ Клиент с ID={client_id} успешно удалён.')
            self.conn.commit()

    def find_client(self, last_name=None, first_name=None, email=None, phone_num=None):
        """Метод находит клиента по одному из данных или по сочетанию фамилии и имени"""
        sql_1 = """SELECT client_id
                     FROM client
                     JOIN phone USING(client_id)
                    WHERE last_name = %s AND first_name = %s OR email = %s OR phone_num = %s"""
        sql_2 = """SELECT client_id
                     FROM client
                     JOIN phone USING(client_id)
                 WHERE last_name = %s OR first_name = %s OR email = %s OR phone_num = %s"""
        try:
            if last_name and first_name:
                self.cur.execute(sql_1, (last_name, first_name, email, phone_num))
            else:
                self.cur.execute(sql_2, (last_name, first_name, email, phone_num))
        except Error as err:
            print(f'\n--> {err}')
        else:
            return list(map(lambda x: x[0], self.cur.fetchall()))

    def close(self):
        self.cur.close()
        self.conn.close()
