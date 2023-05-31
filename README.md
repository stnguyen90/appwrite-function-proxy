# Appwrite Function Proxy

Proxy to execute an [Appwrite](https://appwrite.io/) Function.

<p align="left">
  <a href="https://railway.app/template/Ud6HvY?referralCode=g33k" _target="blank"><img src="https://railway.app/button.svg" alt="Deploy on Railway" height="40"></a>
  <a href="https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fstnguyen90%appwrite-function-proxy%2Ftree%2Fmain&demo-title=Appwrite%20Function%20Proxy&demo-description=Proxy%20to%20execute%20an%20Appwrite%20Function." _target="blank"><img src="https://vercel.com/button" alt="Deploy with Vercel" height="40"></a>
</p>

## ✨ Features

- Transforms generic requests to [create an Appwrite Function Execution](https://appwrite.io/docs/client/functions?sdk=web-default#functionsCreateExecution).
- One proxy can be used to execute any project's function for the configured Appwrite instance

## 💁‍♀️ How to use

### Setup

- Deploy using the button 👆
- Configure the following environment variables:
  - `APPWRITE_ENDPOINT`: Appwrite endpoint
  - `APPWRITE_PROJECTS`: comma separated project IDs to allow using this proxy

### Executing

To proxy your request to Appwrite, send a `POST` request to `https://[DOMAIN]/api/projects/{project_id}/functions/{function_id}/executions` with:

1. your Appwrite API Key as the Authorization Bearer token for authentication
2. your data as the request body

#### Example

```bash
curl -X POST https://$DOMAIN/projects/$PROJECT_ID/functions/$FUNCTION_ID/executions \
    -H "Authorization: Bearer $APPWRITE_API_KEY" \
    -d '{"x": 1}'
```
