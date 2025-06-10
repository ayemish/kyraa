from langgraph.prebuilt import ToolNode
from tools.tool_definitions import (
    get_schedule_for_day,
    create_event_with_attendees,
    delete_event_by_title_and_date,
    update_event_by_id
)

tools = [
    get_schedule_for_day,
    create_event_with_attendees,
    delete_event_by_title_and_date,
    update_event_by_id
]

tool_node = ToolNode(tools)
