import boto3

def get_ssm_parameter(param_name, with_decryption=True):
    ssm = boto3.client("ssm", region_name="us-east-1")  # Make sure this is your AWS region
    response = ssm.get_parameter(Name=param_name, WithDecryption=with_decryption)
    return response["Parameter"]["Value"]

try:
    secret_key = get_ssm_parameter("/JBI/SECRET_KEY")
    ses_username = get_ssm_parameter("/JBI/SES_USERNAME")
    ses_password = get_ssm_parameter("/JBI/SES_PASSWORD")
    ses_sender = get_ssm_parameter("/JBI/SES_EMAIL_SENDER")
    
    print(f"✅ SECRET_KEY: {secret_key}")
    print(f"✅ SES_USERNAME: {ses_username}")
    print(f"✅ SES_PASSWORD: {ses_password}")
    print(f"✅ SES_SENDER: {ses_sender}")

except Exception as e:
    print(f"❌ Failed to fetch SSM parameters: {e}")
