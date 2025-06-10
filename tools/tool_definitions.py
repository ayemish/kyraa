from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode
import requests

# Transform the data into desired format
event_dict = {}



@tool
def delete_event_by_title_and_date(date_str: str, title_snippet: str):
    """
    Deletes a calendar event matching the given date and title by calling two n8n webhooks:
    one to fetch events and one to delete the matched event by its ID.

    Args:
        date_str (str): Date of the event in YYYY-MM-DD format.
        title_snippet (str): A keyword or phrase from the event title to match.

    Returns:
        str: Success or error message.
    """
    fetch_url = "https://raheemtariq4800.app.n8n.cloud/webhook/b94e5310-7adf-425a-820b-148dd36e64ea"
    delete_url = "https://raheemtariq4800.app.n8n.cloud/webhook/delete-event"

    try:
        # Step 1: Fetch all events for the given day
        fetch_response = requests.post(fetch_url, json={"date": date_str})
        fetch_response.raise_for_status()
        events = fetch_response.json()

        if not events or not isinstance(events, list):
            return "No events found for that date."

        # Step 2: Try to match an event by title snippet (case-insensitive)
        matched_event = next(
            (event for event in events if title_snippet.lower() in event.get("summary", "").lower()),
            None
        )

        if not matched_event:
            return f"No event found with title containing '{title_snippet}' on {date_str}."

        event_id = matched_event.get("id")
        if not event_id:
            return "Matched event does not contain an eventId."

        # Step 3: Call delete webhook with eventId
        delete_response = requests.post(delete_url, json={"id": event_id})
        delete_response.raise_for_status()

        return f"Event '{matched_event.get('title')}' on {date_str} was successfully deleted."

    except requests.RequestException as e:
        return f"Error during request: {e}"


@tool
def get_schedule_for_day(date_str: str):
    """
    Get schedule for a given day by calling the n8n webhook.

    Args:
        date_str (str): Date in YYYY-MM-DD format

    Returns:
        dict or str: The JSON response from webhook or error message
    """
    webhook_url = "https://raheemtariq4800.app.n8n.cloud/webhook/b94e5310-7adf-425a-820b-148dd36e64ea"
    
    payload = {"date": date_str}
    
    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()  # raise error for bad status
        for event in response.json():
            event_id = event['id']
            event_dict[event_id] = {
                'summary': event['summary'],
                'start_time': event['start']['dateTime'],
                'end_time': event['end']['dateTime'],
                'attendees': [attendee['email'] for attendee in event.get('attendees', [])]
            }
        print(response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"Error calling webhook: {e}"



@tool
def create_event_with_attendees(title: str, start: str, end: str, attendees: str):
    """
    Create a calendar event with attendees by calling the n8n webhook.
    Make sure you have all the information i.e the title, time, duration and attendee's email
    here is an example payload
    ```
        payload = {
    "title": "Team Meeting",
    "start": "2025-05-29T22:00:00+05:00",
    "end": "2025-05-29T23:00:00+05:00",
    "attendees": "person1@example.com,person2@example.com"
    }
    ```
    Args:
        title (str): Event title
        start (str): Event start time in ISO format (e.g., 2025-05-29T17:00:00+05:00)
        end (str): Event end time in ISO format (e.g., 2025-05-29T18:00:00+05:00)
        attendees (str): Comma-separated emails of attendees (e.g., "a@example.com,b@example.com")

    Returns:
        dict or str: JSON response from webhook or error message
    """
    webhook_url = "https://raheemtariq4800.app.n8n.cloud/webhook/create-event"

    payload = {
        "title": title,
        "start": start,
        "end": end,
        "attendees": attendees
    }
    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"Error calling webhook: {e}"

@tool
def update_event_by_id(event_id: str, title: str, start: str, end: str, attendees: str):
    """
    Update a calendar event by calling the n8n webhook.

    Args:
        event_id (str): The unique ID of the event to update.
        title (str): New title for the event.
        start (str): New start time in ISO format (e.g., 2025-06-01T10:00:00+05:00).
        end (str): New end time in ISO format (e.g., 2025-06-01T11:00:00+05:00).
        attendees (str): Comma-separated list of attendee emails.

    Returns:
        dict or str: JSON response from the webhook or an error message.
    """
    webhook_url = "https://raheemtariq4800.app.n8n.cloud/webhook/update-event"

    payload = {
        "eventId": event_id,
        "title": title,
        "start": start,
        "end": end,
        "attendees": attendees
    }

    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"Error updating event: {e}"

