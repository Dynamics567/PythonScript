import requests
import six
import psycopg2


conn = None

try:
    conn = psycopg2.connect(database="Testdb", user="postgres",
                            password="1155", host="127.0.0.1", port="5432")

    print("Database opened successfully")
    # except:
    #     pass
except (Exception, psycopg2.DatabaseError) as error:
    print(error)

try:
    cur = conn.cursor()

    cur.execute('''drop table if exists News;''')
    conn.commit()

    cur.execute('''CREATE TABLE IF NOT EXISTS News
        (id SERIAL PRIMARY KEY NOT NULL,
        title VARCHAR(200) DEFAULT NULL,
        description TEXT DEFAULT NULL,
        url TEXT DEFAULT NULL,
        image TEXT DEFAULT NULL,
        publishedAt TIMESTAMPTZ DEFAULT NULL,
        source_name VARCHAR(200),
        source_url TEXT );''')

    print("Table created successfully")

    conn.commit()
    # conn.close()
except:
    pass

print("Starting insertion of records")

try:
    cur = conn.cursor()

    response = requests.get(
        'https://gnews.io/api/v3/search?q=none&token=16d422f0d4bfe835e0c18d5dd580b3e5')

    json_response = response.json()

    # print(json_response)

    # print(len(json_response["articles"]))

    # for entry in range(0, len(json_response["articles"])):
    #     print(json_response["articles"][entry]["title"])
    #     print(json_response["articles"][entry]["description"])
    #     print(json_response["articles"][entry]["url"])
    #     print(json_response["articles"][entry]["image"])
    #     print(json_response["articles"][entry]["publishedAt"])
    #     print(json_response["articles"][entry]["source"]["name"])
    #     print(json_response["articles"][entry]["source"]["url"])
    #     print("\n\n")

    for entry in range(0, len(json_response["articles"])):
        sql = """INSERT INTO News (title, description, url, image, publishedat, source_name, source_url) \
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
        cur.execute(sql, (json_response["articles"][entry]["title"],
                          json_response["articles"][entry]["description"],
                          json_response["articles"][entry]["url"],
                          json_response["articles"][entry]["image"],
                          json_response["articles"][entry]["publishedAt"],
                          json_response["articles"][entry]["source"]["name"],
                          json_response["articles"][entry]["source"]["url"]
                          )
                    )

    conn.commit()
    print("%s records inserted successfully" % len(json_response["articles"]))
    conn.close()

except (Exception, psycopg2.DatabaseError) as error:
    print(error)

finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')
