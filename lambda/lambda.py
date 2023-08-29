import json

def lambda_handler(event, context):
   StatusCode = 200
   body = event['headers']['X-Forwarded-For']
   return {
       'StatusCode' : StatusCode,
       'body':json.dumps(body)
   }
