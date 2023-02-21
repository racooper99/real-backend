import json
import boto3
import pymysql

s3_client = boto3.client('s3')


def addUser(event, context):
    print(event)
    body = json.loads(event['body'])
    #queue_id = body['queue_id']
    attraction_id = (body['attraction_id'])
    operator_id = (body['operator_id'])
    alph_code = (body['alph_code'])
    bucket = 'capadventures-data-jan23-team1'
    conn = pymysql.connect(
    host='capadventures.chlmupi9m3gn.us-east-1.rds.amazonaws.com',
    user='admin', 
    passwd = 'poolparty',
    db='capadventures',
)
    cur = conn.cursor()
    iter =1
    cur.execute('SELECT * FROM queue WHERE attraction_id = (%s)', (attraction_id))
    queue_user_in = cur.fetchall()
    print(queue_user_in)
    
    #if queue_user_in == ():
    #
    cur.execute('INSERT INTO queue (attraction_id, operator_id, queue_length, alph_code) VALUES (%s, %s, %s, %s)', (attraction_id, operator_id, 1, alph_code))
    #else:
    #    i = queue_user_in[0][3]
    #    incrementer = i + 1
    #    cur.execute('UPDATE queue SET operator_id = (%s), queue_length = (%s), ticket_id = (%s) WHERE attraction_id = (%s)', (attraction_id, operator_id, incrementer, ticket_id))
    conn.commit()
    conn.close()
    return {
        "statusCode": 200,
        "body": json.dumps({
            "attraction_id": attraction_id,
            "operator_id": operator_id,
            "alph_code": alph_code,
        }), "headers": {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
            },
    }