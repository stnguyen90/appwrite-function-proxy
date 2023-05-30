from fastapi import FastAPI, Request, Response
import httpx
import os

app = FastAPI()

appwrite_endpoint = os.environ['APPWRITE_ENDPOINT']
appwrite_projects = os.environ.get('APPWRITE_PROJECTS', '').split(',')

@app.post("/projects/{project_id}/functions/{function_id}/executions")
async def executions_post(request: Request, project_id: str, function_id: str, response: Response):
    if appwrite_projects and project_id not in appwrite_projects:
        response.status_code = 403
        return {"success": False, "error": "Project not allowed"}

    body = (await request.body()).decode("utf-8")
    authorization = request.headers["Authorization"]
    bearer_token = ""
    if " " in authorization:
        bearer_token = authorization.split(" ")[1]

    async with httpx.AsyncClient() as client:
        r = await client.post(
            f"{appwrite_endpoint}/functions/{function_id}/executions",
            headers={
                "X-Appwrite-Project": project_id,
                "X-Appwrite-Key": bearer_token,
            },
            data={
                "data": body,
            }
        )
        execution = r.json()
        return Response(
            content=execution['response'],
            status_code=execution['statusCode']
        )
