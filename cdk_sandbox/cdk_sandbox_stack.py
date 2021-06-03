from typing_extensions import runtime
from aws_cdk import core as cdk
from aws_cdk import aws_dynamodb, aws_kinesis, aws_s3, aws_lambda, aws_apigateway
# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core


class CdkSandboxStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_table = aws_dynamodb.Table(self, id='dynamo_table', table_name='my_table', partition_key=aws_dynamodb.Attribute(name='lastname',type=aws_dynamodb.AttributeType.STRING))

        my_stream = aws_kinesis.Stream(self, 'kinesis_string', stream_name='my_kinesis_stream')

        my_bucket = aws_s3.Bucket(self, 's3_bucket', bucket_name='my-bucket')

        my_lambda = aws_lambda.Function(self, id='lambda_function', runtime=aws_lambda.Runtime.PYTHON_3_8, handler='hello.handler', code=aws_lambda.Code.asset('lambda'))

        my_api = aws_apigateway.LambdaRestApi(self, 'lambda_api', rest_api_name='cdkapi', handler=my_lambda)
