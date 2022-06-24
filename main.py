import os
import sms_lib
from fastapi import FastAPI, Depends
from fastapi_key_auth import AuthorizerDependency
from pydantic import BaseModel


os.environ['API_KEY'] = 'Test'
authorizer = AuthorizerDependency(key_pattern="API_KEY")

app = FastAPI(dependencies=[Depends(authorizer)])

class Sms(BaseModel):
    number: str
    message: str


@app.post("/send/")
async def send(sms: Sms):
    send_my_sms = sms_lib.send_sms(sms.number, sms.message)
    return send_my_sms
