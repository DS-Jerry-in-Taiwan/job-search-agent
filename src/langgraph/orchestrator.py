"""LangGraph Orchestrator
主編排器，負責編譯和執行 StateGraph。
"""

from .graph import create_workflow
from .state import AgentState

def get_orchestrator():
    """獲取編譯後的 LangGraph 應用

    Returns:
        編譯後的 LangGraph 應用，可直接調用 invoke()
    """
    workflow = create_workflow()
    app = workflow.compile()
    return app

# 測試用
if __name__ == "__main__":
    from .state import create_initial_state

    print("=" * 60)
    print("LangGraph Orchestrator 測試")
    print("=" * 60)

    # 創建 orchestrator
    app = get_orchestrator()

    # 測試執行
    initial_state = create_initial_state("找台北 Python 工作")
    print(f"\n查詢: {initial_state['query']}")

    result = app.invoke(initial_state)

    print(f"\n識別意圖: {result['intents']}")
    print(f"\n最終回應:\n{result['final_response']}")
    print("\n" + "=" * 60)
