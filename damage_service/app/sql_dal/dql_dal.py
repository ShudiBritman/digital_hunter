from db.connection import DataBase


conn = DataBase.get_connection()


def update_table(data, table_name="damage"):
    cursor = conn.cursor()
    query = f'''INSERT INTO {table_name}
        (attack_id, timestamp, entity_id, weapon_type)
        VALUES(%s, %s, %s, %s)'''
    cursor.execute(query, (
        data['timestamp'],
        data['attack_id'],
        data['entity_id'],
        data['result']
    ))
    return