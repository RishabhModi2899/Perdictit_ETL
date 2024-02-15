#!/usr/bin/env python3
import os

import aws_cdk as cdk

from aws_project_etl.aws_project_etl_stack import AwsProjectEtlStack


app = cdk.App()
# AwsProjectEtlStack(app, "AwsProjectEtlStack",
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    #env=cdk.Environment(account='123456789012', region='us-east-1'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    # )

mwaa_hybrid_backend = MwaaCdkStackBackend(
    scope=app,
    id="mwaa-hybrid-backend",
    env=env_EU,
    mwaa_props=mwaa_props
)

mwaa_hybrid_env = MwaaCdkStackEnv(
    scope=app,
    id="mwaa-hybrid-environment",
    vpc=mwaa_hybrid_backend.vpc,
    env=env_EU,
    mwaa_props=mwaa_props
)

app.synth()