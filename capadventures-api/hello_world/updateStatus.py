import json
import boto3
import pymysql

s3_client = boto3.client('s3')


def changeStatus(event, context):
    print(event)
    body = json.loads(event['body'])
    #queue_id = body['queue_id']
    attraction_id = (body['attraction_id'])
    status = (body['status'])
    bucket = 'capadventures-data-jan23-team1'
    conn = pymysql.connect(
    host='capadventures.chlmupi9m3gn.us-east-1.rds.amazonaws.com',
    user='admin', 
    passwd = 'poolparty',
    db='capadventures',
)
    cur = conn.cursor()
    #cur.execute('SELECT * FROM queue WHERE attraction_id = (%s)', (attraction_id))
    cur.execute('UPDATE attraction SET status = (%s) WHERE attraction_id = (%s)', (status, attraction_id))
    conn.commit()
    conn.close()
    return {
        "statusCode": 200,
        "body": json.dumps({
            "attraction_id": attraction_id,
            "status": status,
        }), "headers": {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
            },
    }