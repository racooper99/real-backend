import json
import boto3
import pymysql

s3_client = boto3.client('s3')


def getUser(event, context):
    #attraction_id = event['attraction_id']
    bucket = 'capadventures-data-jan23-team1'
    conn = pymysql.connect(
    host='capadventures.chlmupi9m3gn.us-east-1.rds.amazonaws.com',
    user='admin', 
    passwd = 'poolparty',
    db='capadventures',
)
    cur = conn.cursor()
    cur.execute('SELECT * FROM queue')
    queue_var = cur.fetchall()
    conn.close()
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "queue": queue_var,
        }), "headers": {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
            },
    }