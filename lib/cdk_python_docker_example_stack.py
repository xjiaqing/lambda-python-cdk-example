from os import path

from aws_cdk import Duration, Stack, aws_lambda
from constructs import Construct


class CdkPythonDockerExampleStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        aws_lambda.Function(
            self, "cdk-python-docker-example-stack",
            function_name="cdk-python-docker-example",
            description="this is a example.",
            code=aws_lambda.Code.from_asset_image(path.join(path.dirname(__file__), "../src")),
            runtime=aws_lambda.Runtime.FROM_IMAGE,
            handler=aws_lambda.Handler.FROM_IMAGE,
            architecture=aws_lambda.Architecture.ARM_64,
            memory_size=1024,
            timeout=Duration.seconds(30),
            environment={
                "KEY": "value",
            }
        )