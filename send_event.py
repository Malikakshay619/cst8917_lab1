from azure.eventhub import EventHubProducerClient, EventData

connection_str = "<REDACTED>"
eventhub_name = "click-events"

producer = EventHubProducerClient.from_connection_string(conn_str=connection_str, eventhub_name=eventhub_name)
event_data_batch = producer.create_batch()

event_data_batch.add(EventData('{"userId": "test-user", "timestamp": "2025-06-01T03:00:00Z", "action": "click", "page": "homepage"}'))

producer.send_batch(event_data_batch)
print("✅ Event sent successfully.")
