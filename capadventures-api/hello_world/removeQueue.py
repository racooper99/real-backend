import json
import boto3
import pymysql

s3_client = boto3.client('s3')


def dropUser(event, context):
    print(event)
    body = json.loads(event['body'])
    #queue_length = body['queue_length']
    attraction_id = (body['attraction_id'])
    alph_code = (body['alph_code'])
    bucket = 'capadventures-data-jan23-team1'
    conn = pymysql.connect(
    host='capadventures.chlmupi9m3gn.us-east-1.rds.amazonaws.com',
    user='admin', 
    passwd = 'poolparty',
    db='capadventures',
)
    cur = conn.cursor()
    cur.execute('SELECT * FROM queue WHERE attraction_id = (%s)', (attraction_id))
    queue_user_in = cur.fetchall()

    i = queue_user_in[0][3]
    cur.execute('DELETE from queue WHERE attraction_id = (%s) and alph_code = (%s)', (attraction_id, alph_code))
    #incrementer = i - 1
    #cur.execute('UPDATE queue SET queue_length = (%s) WHERE attraction_id = (%s)', (incrementer, attraction_id))
    conn.commit()
    conn.close()
    return {
        "statusCode": 200,
        "body": json.dumps({
            "attraction_id": attraction_id,
            "alph_code": alph_code,
        }), "headers": {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
            },
    }