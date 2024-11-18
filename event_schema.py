event_schema = {
    "type": "json_schema",
    "json_schema": {
        "name": "events",
        "schema": {
            "type": "object",
            "properties": {
                "events": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
    "name": {
    "description": "the name of the event",
      "type": "string"
    },
    "participants": {
    "description": "who will take part in this event",
     "type": "array",
                    "items": {
      "type": "string"}
    },
    "start_datetime": {
      "type": "string",
            "format": "date-time"
    },
    "end_datetime": {
      "type": "string",
            "format": "date-time"
    },
    "location": {
      "type": "string"
    },
    "description": {
      "type": "string"
    }
  },
  "required": [
    "name",
    "start_datetime",
    "end_datetime",
    "location",
    "description",
    "participants"
  ],
                    },
                    "minItems": 1,
                }
            },
            "required": ["events"]
        },
    }
}
