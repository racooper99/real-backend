import json
import boto3
import pymysql

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    bucket = 'capadventures-data-jan23-team1'
    conn = pymysql.connect(
        host='capadventures.chlmupi9m3gn.us-east-1.rds.amazonaws.com',
        user='admin', 
        passwd = 'poolparty',
        db='capadventures',
    )
    cur = conn.cursor()
    cur.execute('SELECT * FROM attraction')
    attraction_data = cur.fetchall()
    cur.execute('SELECT * from queue')
    queue_data = cur.fetchall()
    #cur.execute('SELECT * from attraction LEFT JOIN queue ON attraction.attraction_id = queue.queue.id')
    queue_attraction_data = []#cur.fetchall()
    conn.close()

    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "attraction_data": attraction_data,
            "queue_data": queue_data,
            "queue_attraction_data": queue_attraction_data,
        }), "headers": {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*'
          },
    }



    