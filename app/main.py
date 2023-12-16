from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import py_eureka_client.eureka_client as eureka_client
from contextlib import asynccontextmanager

import constant
from schemas import Content, Hashtags
from utils import cleanhtml, create_tag

# 서버 시작 시 유레카 서버 등록
@asynccontextmanager
async def lifespan(app: FastAPI):
    await eureka_client.init_async(eureka_server=constant.EUREKA_SERVER,
                       app_name=constant.SERVICE_NAME,
                       instance_host=constant.SERVICE_IP,
                       instance_port=constant.SERVICE_PORT
                       )
    yield

app = FastAPI(lifespan=lifespan)

# 해시태그 추천
@app.post("/hashtag/createTags", response_model=Hashtags)
async def recommand_tag(content:Content):
    text = cleanhtml(content.content)
    tags = create_tag(text)
    return Hashtags(hashtag=tags)