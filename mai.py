import os 
from pprint import pprint
from src.state.operations import create_initial_state
from src.nodes import (
    resume_parser_node,
    job_matcher_node,
    recommendation_node,
    router_node,
    conversation_node,
    router_node,
    error_handler_node,
    finalizer_node,
)

NODE_MAP = {
    "resume_parser": resume_parser_node,
    "job_matcher": job_matcher_node,
    "recommendation": recommendation_node,
    "conversation": conversation_node,
    "router": router_node,
    "error_handler": error_handler_node,
    "finalizer": finalizer_node,
}

def print_state(state):
    print("\n================== Current State =================")
    pprint(state)
    print("=================================================\n")
    
def main():
    state = create_initial_state()
    # 先執行履歷解析，確保有技能
    state = resume_parser_node(state)
    print("🔹 Job Search Agent CLI Demo")
    print("每次按 Enter 執行下一個 Node，或輸入 'exit' 離開，'show' 顯示完整 state。\n")
    
    while True:
        next_node = router_node(state)
        print(f"➡️  下一個 Node: {next_node}")
        
        if next_node == "conversation":
            user_msg = input("請輸入對話內容（或 exit/show）：").strip()
            if user_msg == "exit":
                print("感謝您的使用，期待與您下次相遇。")
                break
            elif user_msg == "show":
                print_state(state)
                continue
            # 將 user_msg 寫入 state["conversation"]["messages"]
            state["conversation"]["messages"].append({"role": "user", "content": user_msg})
            state = conversation_node(state)
            
            # 只顯示最後一則 AI 回應
            ai_msgs = [m for m in state["conversation"]["messages"] if getattr(m, "role", None) == "ai" or (isinstance(m, dict) and m.get("role") == "ai")]
            if ai_msgs:
                last_msg = ai_msgs[-1]
                content = last_msg.content if hasattr(last_msg, "content") else last_msg.get("content")
                print(f"\n🤖 AI：{content}\n")
            else:
                print_state(state["conversation"]["messages"])
            continue
        
        cmd = input("按 Enter 執行，'show' 顯示 state，'exit' 離開：").strip().lower()
        if cmd == "exit":
            print("感謝您的使用，期待與您下次相遇。")
            break
        elif cmd == "show":
            print_state(state)
            continue
        
        if next_node== "__end__" or state.get("is_complete"):
            state = finalizer_node(state)
            print("✅ 流程已結束，謝您的使用，期待與您下次相遇。")
            print_state(state)
            break
        node_func = NODE_MAP.get(next_node)
        if node_func:
            state = node_func(state)
            # print_state(state)
        else:
            print(f"❌ 未知的 Node: {next_node}，請檢查配置。")
            break
        
if __name__ == "__main__":
    main()
