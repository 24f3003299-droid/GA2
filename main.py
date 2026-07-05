from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import time
import uuid
import config
import jwt
from fastapi import Request

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        config.Q1_ALLOWED_ORIGIN,
        config.EXAM_PORTAL_ORIGIN,
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


@app.middleware("http")
async def add_headers(request: Request, call_next):
    start = time.time()

    response = await call_next(request)

    response.headers["X-Request-ID"] = str(uuid.uuid4())
    response.headers["X-Process-Time"] = f"{time.time() - start:.6f}"

    return response


@app.get("/stats")
async def stats(values: str = ""):
    try:
        nums = [int(x.strip()) for x in values.split(",") if x.strip()]
    except ValueError:
        return JSONResponse(
            status_code=400,
            content={"error": "Invalid input"}
        )

    if not nums:
        return JSONResponse(
            status_code=400,
            content={"error": "no values"}
        )

    return {
        "email": config.EMAIL,
        "count": len(nums),
        "sum": sum(nums),
        "min": min(nums),
        "max": max(nums),
        "mean": round(sum(nums) / len(nums), 6),
    }
    @app.post("/verify")
async def verify_token(request: Request):
    try:
        body = await request.json()
        token = body.get("token")

        payload = jwt.decode(
            token,
            config.PUBLIC_KEY_PEM,
            algorithms=["RS256"],
            issuer=config.ISSUER,
            audience=config.AUDIENCE,
        )

        return {
            "valid": True,
            "email": payload.get("email", ""),
            "sub": payload.get("sub", ""),
            "aud": payload.get("aud", "")
        }

    except Exception:
        return JSONResponse(
            status_code=401,
            content={"valid": False}
        )
