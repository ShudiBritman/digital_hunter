from db.connection import DataBase


conn = DataBase.get_connection()


def attack_update(data):
    cursor = conn.cursor()
    query = '''INSERT INTO attack
        (attack_id, timestamp, entity_id, weapon_type)
        VALUES(%s, %s, %s, %s)'''
    cursor.execute(query, (
        data['attack_id'], 
        data['timestamp'],
        data['entity_id'],
        data['weapon_type']))
    return