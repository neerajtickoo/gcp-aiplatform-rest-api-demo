- create a .env file in root directory
- set below in the .env file. For me the service account had owner permissions.
```properties
GOOGLE_APPLICATION_CREDENTIALS=______PATH_TO_KEY_FILE______
```
- Run the demo application

```shell
virtualenv venv --python=3.11

source venv/bin/activate

pip install -r requirements.txt

cd src

python with_aiplatform_client.py

python with_discovery_client.py 
```