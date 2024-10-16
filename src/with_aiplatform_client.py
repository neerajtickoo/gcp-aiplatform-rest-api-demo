from google.cloud import aiplatform_v1
from dotenv import load_dotenv
import traceback

# Set the GOOGLE_APPLICATION_CREDENTIALS in your environment variable with Service Account Key file path.
load_dotenv()


project = "cd-onboarding-graph-test-4"
location = "us-central1"


def list_runtime_templates():
    client = aiplatform_v1.NotebookServiceClient()

    request = aiplatform_v1.ListNotebookRuntimeTemplatesRequest({
            "parent": f"projects/{project}/locations/{location}"
        }
    )

    # Make the request
    page_result = client.list_notebook_runtime_templates(request=request)

    # Handle the response
    for response in page_result:
        print(response)


def list_runtimes():
    client = aiplatform_v1.NotebookServiceClient()

    request = aiplatform_v1.ListNotebookRuntimesRequest({
            "parent": f"projects/{project}/locations/{location}"
        }
    )

    # Make the request
    page_result = client.list_notebook_runtimes(request=request)

    # Handle the response
    for response in page_result:
        print(response)


def list_endpoints():
    client = aiplatform_v1.EndpointServiceClient()

    request = aiplatform_v1.ListEndpointsRequest({
            "parent": f"projects/{project}/locations/{location}"
        }
    )

    # Make the request
    page_result = client.list_endpoints(request=request)

    # Handle the response
    for response in page_result:
        print(response)


def main():
    api_methods_to_run = [
        list_runtime_templates,
        list_runtimes,
        list_endpoints,
    ]

    for method in api_methods_to_run:
        try:
            print("***** Running Method ****", method.__name__)
            method()
        except Exception as e:
            print("Exception while running method ", method.__name__, e)
            traceback.print_exc()


if __name__ == '__main__':
    main()
