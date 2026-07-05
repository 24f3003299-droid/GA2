# ==========================================
# MASTER CONFIGURATION
# ==========================================

# Q1
EMAIL = "24f3003299@ds.study.iitm.ac.in"
Q1_ALLOWED_ORIGIN = "https://dash-hzecuz.example.com"

# Q2 (baad me fill karna)
ISSUER = "https://idp.exam.local"

AUDIENCE = "tds-0helx7a7.apps.exam.local"

PUBLIC_KEY_PEM = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2okOHspNjgA+2rTLbeuY
cxiP/hG8C6Sb9iwg3yiLAA4HCnpITcbWCSelbvbYGuc3EbNy4xFyf5Cbj5DHJMID
EkryOgyd2giIIIBOUBj8S63uGcnRpOBh9NFatfNwheKuzsPuVNldu6A9cNteNpXc
WyJjG2axVfmq7i6SuKr1JoWYG7xTTAvKPujSl4OtsQfO3h5NepzdfXpr28oNnzfW
ed+zclR6BcmNNo/WVfJ4xyCLSf0BCOgdTgW6PdaChd1l9VDetJZVEgC5tkyvXsfI
SI6iyrYbKR0NEBSqq4XkadEjsCs4F1RncsS4LlgniT7GlkL9Mce3b0wGLs9/7ZIX
dQIDAQAB
-----END PUBLIC KEY-----"""
# 4. Q3: 12-Factor Config (Manually merge the variables)
# 4. Q3: 12-Factor Config
Q3_PORT = 8032
Q3_WORKERS = 9
Q3_DEBUG = True
Q3_LOG_LEVEL = "debug"

# 5. Q5: Analytics (Find the API key in the Q5 instruction tab)
Q5_API_KEY = "ak_nesopcw6to8dyh4ym87r09ae"

# 6. Q9: Idempotency & Rate Limit (Find total orders and rate limit)
Q9_TOTAL_ORDERS = 50
Q9_RATE_LIMIT = 15

# 7. Q10: Middleware Rate Limit (Find allowed origin and rate limit)
Q10_ALLOWED_ORIGIN = "https://app-xxxxxx.example.com"
Q10_RATE_LIMIT = 8

# ==========================================
# FIXED VARIABLES (Do not change these)
# ==========================================
EXAM_PORTAL_ORIGIN = "https://exam.sanand.workers.dev"
