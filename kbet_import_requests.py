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

    cur.execute('''drop table if exists kbet;''')
    conn.commit()

    cur.execute('''CREATE TABLE IF NOT EXISTS kbet
        (ItemID  SERIAL PRIMARY KEY NOT NULL,
        OddType VARCHAR(200) DEFAULT NULL,
        OddName TEXT DEFAULT NULL,
        OddOutcomes TEXT DEFAULT NULL,
        MatchOddID VARCHAR(200) DEFAULT NULL,
        publishedAt TIMESTAMPTZ DEFAULT NULL,);''')

    print("Table created successfully")

    conn.commit()
    # conn.close()
except:
    pass

print("Starting insertion of records")

try:
    cur = conn.cursor()

    response = requests.get(
        'https://sb-btk-sportapi-cdn-micro-prod.azureedge.net/api/feeds/prematch/en/4/1619270/532/14')

    json_response = response.json()

    # print(json_response)

    print(len(json_response["AreaMarkets"]))

    for entry in range(0, len(json_response["AreaMarkets"])):
        print(json_response["AreaMarkets"][entry]["ItemID"])
        print(json_response["AreaMarkets"][entry]["OddType"])
        print(json_response["AreaMarkets"][entry]["OddName"])
        print(json_response["AreaMarkets"][entry]["OddOutcome"])
        print(json_response["AreaMarkets"][entry]["MatchOddID"])
        print(json_response["AreaMarkets"][entry]["publishedAt"])
        print("\n\n")

    for entry in range(0, len(json_response["AreaMarkets"])):
        sql = """INSERT INTO kbet (ItemIDtle, OddType, OddName, OddOutcome, MatchOddID,) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
        cur.execute(sql, (json_response["AreaMarkets"][entry]["ItemID"],
                          json_response["AreaMarkets"][entry]["OddType"],
                          json_response["AreaMarkets"][entry]["OddName"],
                          json_response["AreaMarkets"][entry]["OddOutcome"],
                          json_response["AreaMarkets"][entry]["MatchOddID"],
                          json_response["AreaMarkets"][entry]["publishedAt"],

                          )
                    )

    conn.commit()
    print("%s records inserted successfully" %
          len(json_response["AreaMarkets"]))
    conn.close()

except (Exception, psycopg2.DatabaseError) as error:
    print(error)

finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')
