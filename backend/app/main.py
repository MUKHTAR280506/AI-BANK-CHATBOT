from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import chat, admin, beneficiary, validation

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router)
app.include_router(admin.router)
app.include_router(beneficiary.router)
app.include_router(validation.router)
print(validation.router.routes)

