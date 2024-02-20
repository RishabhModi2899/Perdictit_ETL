#!/usr/bin/env python3
from mwaa_cdk.mwaa_cdk_env import MwaaCdkStackEnv
from mwaa_cdk.mwaa_cdk_backend import MwaaCdkStackBackend
import os
from dotenv import load_dotenv

import aws_cdk as cdk

load_dotenv()

# from aws_project_etl.aws_project_etl_stack import AwsProjectEtlStack

env_US = cdk.Environment(region=os.getenv(
    "region"), account=os.getenv("account"))
mwaa_props = {'dagss3location': os.getenv("dagss3location"),
              'mwaa_env': os.getenv("mwaa_env")}

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
