import requests
def call_api(
        method: str,
        url: str,
        headers: dict = None,
        params: dict = None,
        data: dict = None,
        token: str = None
):
    """
    method: "GET", "POST", "PUT", "DELETE"
    url: API endpoint
    headers: request headers
    params: query parameters (for GET)
    data: request body (for POST/PUT)
    token: optional Bearer token
    """
    headers = headers or {}
    if token:
        headers.setdefault("Authorization", f"Bearer {token}")
    try:
        resp = requests.request(
            method=method.upper(),
            url=url,
            headers=headers,
            params=params,
            json=data
        )
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        return {"error": str(e), "status_code": getattr(e.response, "status_code", None)}
print(call_api(method='get',url="https://catfact.ninja/fact"))
print(call_api("GET","https://dog.ceo/api/breeds/image/random",headers={"Accept": "application/json"}))
print(call_api("GET","https://reqres.in/api/users/2",headers={"Accept": "application/json", "Custom-Header": "Ritwik123"}))
