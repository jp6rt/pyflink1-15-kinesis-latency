import boto3
import json
import random
from datetime import datetime, timedelta
import time
from botocore.config import Config
from uuid import uuid4

my_config = Config(
    signature_version='v4',
    retries={
        'max_attempts': 10,
        'mode': 'standard'
    },

)

stream_name = 'flink-source'


kinesis_client = boto3.client(
    'kinesis',
    config=my_config,
    region_name='ap-southeast-1')

device_id = str(uuid4())
user_id = str(uuid4())
session_id = str(uuid4())
game_id = str(uuid4())
mobile_id = str(uuid4())
partition_key = str(uuid4())

while True:
    message = {
        'event_time': (datetime.now() + timedelta(hours=-8)).isoformat(),
        'user_id': user_id,
        'session_id': session_id
    }

    print(message)

    response = kinesis_client.put_record(
        StreamName=stream_name,
        Data=json.dumps(message),
        PartitionKey=partition_key
    )

    print(response)
    time.sleep(0.25)
