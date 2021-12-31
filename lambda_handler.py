
def lambda_handler(event, context):
  import boto3
   
  bucket_name = "exercise-s3"
  ssm = boto3.client('ssm')
  s3 = boto3.resource("s3")
  s3_path =""
  try:
    parameter = ssm.get_parameter(Name='UserName', WithDecryption=True)
    print(parameter)
    ssm_parameter = parameter["Parameter"].get("Name") + " "+ parameter["Parameter"].get("Value")
    
    file_name = "parameter.txt"
    s3_path =  file_name
    s3.Bucket(bucket_name).put_object(Key=s3_path, Body=ssm_parameter)
    
  except Exception as ex:
    print("ERROR: ", ex)
      
  finally:
    message = 'File is created in:'+ s3_path
    return message