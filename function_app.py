import azure.functions as func
import logging
import json

app = func.FunctionApp()

@app.event_hub_message_trigger(arg_name="azeventhub", 
                               event_hub_name="click-events", 
                               connection="EventHubConnection")
def ClickEventFunction(azeventhub: func.EventHubEvent):
    message = azeventhub.get_body().decode('utf-8')
    logging.info(f"✅ Python EventHub trigger received: {message}")

