def finalizer_node(state):
    """
    結束流程的收尾節點，可做日誌、狀態保存等
    """
    state["system"]["current_node"] = "finalizer"
    state["system"]["workflow_status"] = "finished"
    return state