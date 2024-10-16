import json
from googleapiclient.discovery import build
from dotenv import load_dotenv


# Set the GOOGLE_APPLICATION_CREDENTIALS in your environment variable with Service Account Key file path.
load_dotenv()


project = "cd-onboarding-graph-test-4"
location = "us-central1"


def list_ai_platform_runtime_templates():
    with build(
        "aiplatform", "v1"
    ) as ai_platform_client:
        par = f"projects/{project}/locations/{location}"
        obj = ai_platform_client.projects().locations().notebookRuntimeTemplates().list(parent=par)
        resp = obj.execute()
        print(json.dumps(resp, sort_keys=True, indent=4))


def list_ai_platform_runtimes():
    with build(
        "aiplatform", "v1"
    ) as ai_platform_client:
        par = f"projects/{project}/locations/{location}"
        obj = ai_platform_client.projects().locations().notebookRuntimes().list(parent=par)
        resp = obj.execute()
        print(json.dumps(resp, sort_keys=True, indent=4))


def list_ai_platform_endpoints():
    with build(
        "aiplatform", "v1"
    ) as ai_platform_client:
        par = f"projects/{project}/locations/{location}"
        obj = ai_platform_client.projects().locations().endpoints().list(parent=par)
        resp = obj.execute()
        print(json.dumps(resp, sort_keys=True, indent=4))


def main():
    api_methods_to_run = [
        list_ai_platform_runtime_templates,
        list_ai_platform_runtimes,
        list_ai_platform_endpoints,
    ]

    for method in api_methods_to_run:
        try:
            print("***** Running Method ****", method.__name__)
            method()
        except Exception as e:
            print("Exception while running method ", method.__name__, e)


if __name__ == '__main__':
    main()
