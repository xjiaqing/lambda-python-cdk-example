import aws_cdk as core
import aws_cdk.assertions as assertions

from lib.cdk_python_docker_example_stack import CdkPythonDockerExampleStack


# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_python_docker_example/cdk_python_docker_example_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkPythonDockerExampleStack(app, "cdk-python-docker-example")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
