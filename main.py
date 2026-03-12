from fastapi import FastAPI
from fastapi.responses import Response
from twilio.rest import Client

app = FastAPI(title="Shreya Message Voice Call System")

# ----------------------
# Twilio Credentials
# ----------------------
ACCOUNT_SID = "YOUR_ACCOUNT_SID"       # Twilio Account SID
AUTH_TOKEN = "YOUR_AUTH_TOKEN"         # Twilio Auth Token
TWILIO_NUMBER = "+19522954216"         # Twilio Phone Number
MY_PHONE = "+918534866350"             # Your personal phone number (verified)
# ----------------------

client = Client(ACCOUNT_SID, AUTH_TOKEN)

# ---------------------------------------
# Voice Message Endpoint
# ---------------------------------------
@app.get("/voice")
def voice():
    """
    Twilio will hit this endpoint to get TwiML instructions for the call.
    The message will be spoken when the call is picked up.
    """
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


# ---------------------------------------
# Test Call Endpoint
# ---------------------------------------
@app.get("/test-call")
def test_call():
    """
    Triggers a test call to the phone number.
    When the call is answered, Twilio will fetch /voice endpoint
    and play the voice message.
    """
    call = client.calls.create(
        to=MY_PHONE,
        from_=TWILIO_NUMBER,
        url="https://YOUR_PUBLIC_DOMAIN/voice",  # Replace with your deployed server URL
        time_limit=20                             # Optional: max duration of the call in seconds
    )
    return {"status": "Call Triggered", "call_sid": call.sid}
