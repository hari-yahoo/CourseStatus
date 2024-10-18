
def lambda_handler(event, context):
    response = "Received Message Body from API GW: " + event['Records'][0]['body']
    print(response)
    