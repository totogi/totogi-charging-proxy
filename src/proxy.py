from decimal import Decimal
import json
import httpx

from src.utils import headers, INIT_URL

client = httpx.Client(http2=True, verify=False)

# Decimal Bug Fix: https://stackoverflow.com/questions/63278737/object-of-type-decimal-is-not-json-serializable
class DecimalEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, Decimal):
      return str(obj)
    return json.JSONEncoder.default(self, obj)


def handler(event, context):
    print(event)
    body = json.loads(event['body'])
    requestData = body['requestData']
    idToken = body['token']
    url = body['url']
    if INIT_URL in url:
        response = client.post(
            url=url,
            json=requestData,
            headers=headers(idToken)
        )
        try:
            json_result = response.json()
        except:
            json_result = None
        return {
            'statusCode': 200,
            'body': json.dumps({
                'response': json_result,
                'headers': dict(response.headers)
            }, cls=DecimalEncoder)
        }
    return {
            'statusCode': 403,
            'body': json.dumps({
                'response': 'Please make sure you are proxying the Totogi Charging API'
            })
        }
