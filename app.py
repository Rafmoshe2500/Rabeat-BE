from fastapi import FastAPI
import uvicorn

from routers.torah import torah_router
from routers.mongo import mongo_router

app = FastAPI(title='Rabbeat')
app.include_router(mongo_router)
app.include_router(torah_router)
uvicorn.run(app)



