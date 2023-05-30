from fastapi import FastAPI, Request
import httpx
import os

app = FastAPI()

appwrite_endpoint = os.environ['APPWRITE_ENDPOINT']

@app.post("/projects/{project_id}/functions/{function_id}/executions")
async def executions_post(request: Request, project_id: str, function_id: str):
    body = (await request.body()).decode("utf-8")
    authorization = request.headers["Authorization"]
    bearer_token = ""
    if " " in authorization:
        bearer_token = authorization.split(" ")[1]

    async with httpx.AsyncClient() as client:
        await client.post(
            f"{appwrite_endpoint}/functions/{function_id}/executions",
            headers={
                "X-Appwrite-Project": project_id,
                "X-Appwrite-Key": bearer_token,
            },
            data={
                "data": body,
            }
        )

    return {"success": True}
