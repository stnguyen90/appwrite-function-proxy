const express = require("express");
const bodyParser = require("body-parser");
const morgan = require("morgan");

const app = express();

app.use(morgan("combined"));
app.use(bodyParser.text({ type: "*/*" }));

const APPWRITE_ENDPOINT =
  process.env.APPWRITE_ENDPOINT || "https://cloud.appwrite.io/v1";
const APPWRITE_PROJECTS = (process.env.APPWRITE_PROJECTS || "")
  .split(",")
  .filter((x) => x !== "");

app.post(
  "/projects/:projectId/functions/:functionId/executions",
  async (req, res) => {
    const { projectId, functionId } = req.params;

    if (
      APPWRITE_PROJECTS.length > 0 &&
      !APPWRITE_PROJECTS.includes(projectId)
    ) {
      res.status(403);
      res.end("Project not allowed");
      return;
    }

    const body = req.body;

    const authorization = req.headers["authorization"] || "";
    let bearerToken = "";
    if (authorization.includes(" ")) {
      bearerToken = authorization.split(" ")[1];
    }

    const response = await fetch(
      `${APPWRITE_ENDPOINT}/functions/${functionId}/executions`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-Appwrite-Project": projectId,
          "X-Appwrite-Key": bearerToken,
        },
        body: JSON.stringify({
          data: body,
        }),
      }
    );

    const execution = await response.json();
    res.end(execution.response);
  }
);

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => console.log(`Server is running in port ${PORT}`));
