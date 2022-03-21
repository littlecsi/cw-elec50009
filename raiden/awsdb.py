import boto3

def create_score_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    
    table = dynamodb.create_table(
        TableName='Scores',
        KeySchema=[
            {
                'AttributeName': 'user',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'score',
                'KeyType': 'RANGE'
            },
            {
                'AttributeName': 'date',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'user',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'score',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'date',
                'AttributeType': 'S'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table

def put_score(user, score, date, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('Scores')
    response = table.put_item(
        Item={
            'user': user,
            'score': score,
            'date': date
        }
    )
    return response

def get_highest_score(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('Scores')
    response = list(table.query_2(PRIMARYKEY__eq='score', reverse=True, limit=1))
    return response[0]['score']

if __name__ == '__main__':
    score_table = create_score_table()
    print("Table status:", score_table.table_status)