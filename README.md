# Voice

Playground for Rasa + Speech Recognition

## Run Server

```sh
$ rasa run
2019-08-17 19:05:23 INFO     root  - Starting Rasa server on http://localhost:5005
```

### Start Conversation

Send a message with the following:

POST:

```text
http://localhost:5005/webhooks/rest/webhook
```

Headers:

```text
Content-type: application/json
```

Body:

```json
{
    "sender": "Rasa",
    "message": "Hello there!"
}
```

```sh
curl -X POST \
  http://localhost:5005/webhooks/rest/webhook \
  -H 'Content-Type: application/json' \
  -d '{
	"sender": "Rasa",
	"message": "Hello world!"
}'
```
