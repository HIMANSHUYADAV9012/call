import os
from fastapi import FastAPI
from fastapi.responses import Response
from twilio.rest import Client
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

app = FastAPI(title="Shreya Message Voice Call System")

# -------------------------
# Environment Variables
# -------------------------
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
MY_PHONE = os.getenv("MY_PHONE")
PUBLIC_URL = os.getenv("PUBLIC_URL")

client = Client(ACCOUNT_SID, AUTH_TOKEN)

# -------------------------
# Voice Endpoint
# -------------------------
@app.get("/voice")
def voice():

    twiml = """
    <Response>
        <Say voice="alice">
        Hello Himanshu
        </Say>
        <Pause length="1"/>
        <Say>
        Shreya sent a new message
        </Say>
        <Pause length="1"/>
        <Say>
        Please check your website
        </Say>
    </Response>
    """

    return Response(content=twiml, media_type="text/xml")


# -------------------------
# Test Call API
# -------------------------
@app.get("/test-call")
def test_call():

    call = client.calls.create(
        to=MY_PHONE,
        from_=TWILIO_NUMBER,
        url=f"{PUBLIC_URL}/voice",
        time_limit=20
    )

    return {
        "status": "Call Triggered",
        "call_sid": call.sid
    }
