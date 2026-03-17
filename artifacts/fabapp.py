import certifi
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse, JSONResponse
import uvicorn

from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

from azure.identity import InteractiveBrowserCredential

# -----------------------------
# Global setup (preserve structure)
# -----------------------------
app_cred = InteractiveBrowserCredential()
scope = "https://analysis.windows.net/powerbi/api/.default"

def get_token(scope: str = scope):
    token = app_cred.get_token(scope)
    return token.token

def nl_to_graphql(nl_query: str):
    # IMPORTANT: escaping quotes for safe GraphQL string embedding
    safe = nl_query.replace("\\", "\\\\").replace('"', '\\"')
    # Return formatted GraphQL query string using f-string interpolation
    return 'query { executefind_products_chat_api(text: ' + f'"{safe}"' + ') { answer } }'

# -----------------------------
# FastAPI app
# -----------------------------
app = FastAPI()

# Update this if your endpoint changes
GRAPHQL_URL = (
    "https://99b3a51d60534ef3bbb1d178e84d73d4.z99.graphql.fabric.microsoft.com/v1/workspaces/99b3a51d-6053-4ef3-bbb1-d178e84d73d4/graphqlapis/87e92ce8-1f9b-49e6-9f4d-4164e1fb331b/GraphQL"
)

@app.get("/", response_class=HTMLResponse)
def root():
    # Return RAW HTML (not escaped) so browser renders it
    return HTMLResponse(
        """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>Zava Retail - GraphQL Chat</title>
  <style>
    :root{
      --bg-gradient: linear-gradient(135deg, #e9ddff 0%, #f7c8ff 55%, #d9e7ff 100%);
      --card-bg:#ffffff;
      --banner-gradient: linear-gradient(90deg, #8b5cf6 0%, #ec4899 100%);
      --primary:#2563eb;
      --text-dark:#1f2937;
      --muted:#6b7280;
      --border:#e5e7eb;
      --radius-lg:20px;
      --radius-md:12px;
    }
    *{box-sizing:border-box;}
    body{
      margin:0;
      min-height:100vh;
      font-family: "Segoe UI", Arial, sans-serif;
      background: var(--bg-gradient);
      display:flex;
      align-items:center;
      justify-content:center;
      padding:24px;
    }
    .container{
      width:100%;
      max-width:980px;
      background:var(--card-bg);
      border-radius:var(--radius-lg);
      box-shadow: 0 30px 60px rgba(0,0,0,0.15);
      overflow:hidden;
      border: 1px solid rgba(255,255,255,0.35);
    }
    .header{
      padding:18px 26px;
      display:flex;
      align-items:center;
      justify-content:space-between;
      background: linear-gradient(180deg, rgba(255,255,255,0.95), rgba(255,255,255,0.85));
    }
    .brand{
      display:flex;
      align-items:center;
      gap:10px;
    }
    .logo-badge{
      width:36px;
      height:36px;
      border-radius:50%;
      background:#2563eb;
      color:#fff;
      display:flex;
      align-items:center;
      justify-content:center;
      font-weight:800;
      letter-spacing:.5px;
    }
    .brand-text{
      display:flex;
      flex-direction:column;
      line-height:1.05;
    }
    .brand-text .name{
      font-size:20px;
      font-weight:800;
      color:#2563eb;
    }
    .brand-text .sub{
      font-size:11px;
      letter-spacing:1.2px;
      color:#6b7280;
      font-weight:700;
    }

    .banner{
      background: var(--banner-gradient);
      padding: 42px 32px;
      color:#fff;
      display:flex;
      align-items:center;
      justify-content:space-between;
      gap:24px;
    }
    .banner-text h1{
      margin:0 0 10px 0;
      font-size:30px;
      font-weight:800;
      letter-spacing:.2px;
    }
    .banner-text p{
      margin:0;
      font-size:15px;
      opacity:.92;
    }
    .banner-image{
      display:flex;
      align-items:flex-end;
      gap:16px;
      min-width:240px;
      justify-content:flex-end;
    }
    .clock{
      width:62px;
      height:62px;
      border-radius:50%;
      background: radial-gradient(circle at 30% 30%, #ffffff, #f3f4f6);
      border:4px solid rgba(17,24,39,0.25);
      position:relative;
      box-shadow: 0 10px 20px rgba(0,0,0,0.12);
    }
    .clock:before{
      content:"";
      width:4px;height:18px;
      background:#111827;
      position:absolute;
      left:50%;top:18px;
      transform:translateX(-50%);
      border-radius:2px;
      opacity:.9;
    }
    .clock:after{
      content:"";
      width:16px;height:4px;
      background:#111827;
      position:absolute;
      left:50%;top:31px;
      transform:translateX(-2px);
      border-radius:2px;
      opacity:.9;
    }
    .bag{
      width:72px;
      height:86px;
      border-radius:8px;
      position:relative;
      box-shadow: 0 10px 20px rgba(0,0,0,0.12);
    }
    .bag.yellow{ background:#f59e0b; }
    .bag.red{ background:#ef4444; }
    .bag:before{
      content:"";
      position:absolute;
      top:-18px;
      left:50%;
      width:34px;
      height:22px;
      border:4px solid rgba(255,255,255,0.7);
      border-bottom:none;
      border-radius: 16px 16px 0 0;
      transform:translateX(-50%);
      opacity:.85;
    }

    .assistant{
      padding: 26px 32px 32px;
      background: linear-gradient(180deg, #ffffff, #fbfbff);
    }
    .assistant label{
      display:block;
      font-weight:700;
      margin-bottom:10px;
      color:var(--text-dark);
      font-size:16px;
    }
    .input-row{
      display:flex;
      gap:12px;
      align-items:center;
      background:#fff;
      border:1px solid var(--border);
      border-radius:14px;
      padding:12px;
      box-shadow: 0 14px 30px rgba(31,41,55,0.08);
    }
    .input-row input{
      flex:1;
      border:none;
      outline:none;
      font-size:15px;
      padding:8px 10px;
      color:var(--text-dark);
      background:transparent;
    }
    .input-row button{
      padding:10px 22px;
      border:none;
      border-radius:10px;
      background: var(--primary);
      color:#fff;
      font-weight:800;
      cursor:pointer;
      box-shadow: 0 10px 18px rgba(37,99,235,0.25);
    }
    .input-row button:hover{ background:#1d4ed8; }

    .response-wrap{
      margin-top:18px;
      background:#fff;
      border:1px solid var(--border);
      border-radius:14px;
      padding:14px 14px 10px;
      box-shadow: 0 14px 30px rgba(31,41,55,0.06);
    }
    .response-title{
      font-size:12px;
      font-weight:800;
      letter-spacing:.8px;
      color:#6b7280;
      text-transform:uppercase;
      margin-bottom:8px;
    }
    pre#response{
      margin:0;
      white-space:pre-wrap;
      word-break:break-word;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
      font-size:13px;
      color:#111827;
      background:#f9fafb;
      border:1px solid #eef2f7;
      border-radius:12px;
      padding:12px;
      min-height:90px;
    }
    .hint{
      margin-top:10px;
      font-size:12px;
      color:#6b7280;
    }

    @media(max-width:768px){
      .banner{ flex-direction:column; text-align:center; }
      .banner-image{ display:none; }
      .assistant{ padding:20px; }
      .header{ padding:14px 18px; }
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div class="brand">
        <div class="logo-badge">Z</div>
        <div class="brand-text">
          <div class="name">zava</div>
          <div class="sub">RETAIL</div>
        </div>
      </div>
      <div style="color:#6b7280;font-weight:700;font-size:13px;">GraphQL Assistant</div>
    </div>

    <div class="banner">
      <div class="banner-text">
        <h1>Shop the latest deals and save!</h1>
        <p>Limited time offers on top products</p>
      </div>
      <div class="banner-image" aria-hidden="true">
        <div class="clock"></div>
        <div class="bag yellow"></div>
        <div class="bag red"></div>
      </div>
    </div>

    <div class="assistant">
      <form id="nlForm" action="/query" method="post">
        <label for="nl_query">What can I help you with?</label>
        <div class="input-row">
          <input type="text" id="nl_query" name="nl_query" placeholder="e.g., Find top discounted shoes" autocomplete="off"/>
          <button type="submit">Ask</button>
        </div>

        <div class="response-wrap">
          <div class="response-title">Response</div>
          <pre id="response">Response</pre>
          <div class="hint">Tip: Your output will show the GraphQL JSON response (answer field).</div>
        </div>
      </form>
    </div>
  </div>

  <script>
    const form = document.getElementById('nlForm');
    const responsePre = document.getElementById('response');

    form.addEventListener('submit', async function(e) {
      e.preventDefault();

      const formData = new FormData(form);
      const body = new URLSearchParams();
      for (const pair of formData) body.append(pair[0], pair[1]);

      responsePre.textContent = "Thinking...";
      try {
        const res = await fetch('/query', {
          method: 'POST',
          headers: { 'Accept': 'application/json' },
          body
        });

        const json = await res.json();
        responsePre.textContent = JSON.stringify(json, null, 2);
      } catch (err) {
        responsePre.textContent = String(err);
      }
    });
  </script>
</body>
</html>
"""
    )

@app.post("/query")
def query(nl_query: str = Form(...)):
    graphql_query = nl_to_graphql(nl_query)
    token = get_token()

    transport = RequestsHTTPTransport(
        url=GRAPHQL_URL,
        headers={"Authorization": f"Bearer {token}"},
        # ✅ Use certifi bundle to fix SSL verification issues
        verify=certifi.where(),
        retries=3,
    )

    client = Client(transport=transport, fetch_schema_from_transport=False)

    try:
        result = client.execute(gql(graphql_query))
        return JSONResponse(result)
        
    except Exception as e:
        # Return error details to the UI
        return JSONResponse({"error": str(e), "graphql_query": graphql_query})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.3", port=8000)