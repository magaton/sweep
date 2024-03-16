from sweepai.agents.assistant_planning import new_planning
from sweepai.core.entities import FileChangeRequest


def process_issue_text(issue_text: str) -> tuple[list[str], str]:
    zip_path = "/tmp/dummy_path.zip"
    additional_messages = []
    file_change_requests = new_planning(issue_text, zip_path, additional_messages)
    
    files_to_change = []
    execution_plan_parts = []
    for fcr in file_change_requests:
        files_to_change.append(fcr.filename)
        if fcr.change_type == "create":
            execution_plan_parts.append(f"Create file {fcr.filename}")
        elif fcr.change_type == "modify":
            execution_plan_parts.append(f"Modify file {fcr.filename}")
    
    execution_plan = "\n".join(execution_plan_parts)
    return files_to_change, execution_plan
