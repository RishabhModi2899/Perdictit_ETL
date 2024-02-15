from .venv/Lib/site-packages/aws_cdk import (
    aws_iam as iam,
    aws_ec2 as ec2,
    Stack,
    CfnOutput
)
from .venv/Lib/site-packages/co import Construct

class MwaaCdkStackBackend(Stack):