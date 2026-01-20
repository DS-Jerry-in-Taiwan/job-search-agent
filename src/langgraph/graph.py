# StateGraph workflow registry for多 workflow支援

from src.graph.workflow import create_workflow

# 統一註冊完整 workflow
workflow_registry = {
    "default": create_workflow(),
}

def get_state_graph_by_id(workflow_id: str):
    return workflow_registry.get(workflow_id, workflow_registry["default"])
