#!/usr/bin/env python3
import os

import aws_cdk as cdk

# from aws_project_etl.aws_project_etl_stack import AwsProjectEtlStack
from mwaa_cdk.mwaa_cdk_backend import MwaaCdkStackBackend
from mwaa_cdk.mwaa_cdk_env import MwaaCdkStackEnv

env_US = cdk.Environment(region="us-east-2", account="402440403671")
mwaa_props = {'dagss3location': '094459-airflow-hybrid-demo',
              'mwaa_env': 'mwaa-hybrid-demo'}

app = cdk.App()

mwaa_hybrid_backend = MwaaCdkStackBackend(
    scope=app,
    id="mwaa-hybrid-backend",
    env=env_US,
    mwaa_props=mwaa_props
)

mwaa_hybrid_env = MwaaCdkStackEnv(
    scope=app,
    id="mwaa-hybrid-environment",
    vpc=mwaa_hybrid_backend.vpc,
    env=env_US,
    mwaa_props=mwaa_props
)

app.synth()
