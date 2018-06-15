"""A basic (single function) API with pokemon written using hug"""
import hug
import mysql.connector, json

cnx = mysql.connector.Connect(user='root', password='root', host='127.0.0.1', database="pokemon")

@hug.get('/', output=hug.output_format.json)
def getPokemon():
    """Return All pokemons or filter pokemons lists"""
    cursor = cnx.cursor()
    cursor.execute("""SELECT t.*, p.*
    FROM pokemon AS p
    LEFT JOIN pokemon_type AS pt ON pt.pokemon_id  = p.id
    LEFT JOIN type AS t ON pt.type_id  = t.id""")
    result = cursor.fetchall()

    return json.dumps(result)

@hug.post('/', output=hug.output_format.json)
def postPokemon(body):
    """Generate new pokemon"""
    values = []
    for element in body.values():
        values.append(element)

    cursor = cnx.cursor()
    try:
        cursor.execute("""INSERT INTO pokemon (attack, defense, hp, name, pokemon_id, sp_atk, sp_def, speed, total) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""", sorted(values))
        cnx.commit()
    except:
        return "ERROR"

    return json.dumps("it work")

@hug.put('/', output=hug.output_format.json)
def putPokemon(body):
    """Update a pokemon"""
    query = ""
    for key, val in body.items():
        if key != 'id':
            query = query + ", " + str(key) + " = " + "'" + str(val.decode('utf-8').splitlines()[0]) + "'"
    query = query[1:]
    cursor = cnx.cursor()
    try:
        cursor.execute("""UPDATE pokemon SET name = %s WHERE id = %s""", [query, body.get("id")])
        cnx.commit()
    except:
        return "ERROR"

    return json.dumps("it work")

@hug.delete('/', output=hug.output_format.json)
def deletePokemon(body):
    """Delete a pokemon"""
    cursor = cnx.cursor()
    print(body.get("id"))
    try:
        cursor.execute("""DELETE FROM pokemon WHERE pokemon.id = %s""", [str(body.get("id"))])
        cnx.commit()
    except:
        return "ERROR"

    return json.dumps("it work")
