from aws_cdk import (
    aws_iam as iam,
    aws_ec2 as ec2,
    Stack,
    CfnOutput
)
from constructs import Construct

class MwaaCdkStackBackend(Stack):
    
    def __init__(self, scope: Construct, id: str, mwaa_props, **kwargs) -> 
    