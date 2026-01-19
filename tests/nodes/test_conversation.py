import pytest
from src.nodes.conversation import conversation_node

def make_state(intent, context=None, job_state=None, user_profile=None):
    return {
        "conversation": {
            "current_intent": intent,
            "context": context or {},
            "messages": []
        },
        "job_state": job_state or {},
        "user_profile": user_profile or {},
        "system": {}
    }

def test_conversation_greet():
    state = make_state("greet")
    out = conversation_node(state)
    assert out["conversation"]["messages"][-1]["content"].startswith("您好")
    assert out["system"]["current_node"] == "conversation"

def test_conversation_ask_recommendation():
    jobs = [{"id": "job_1"}, {"id": "job_2"}]
    state = make_state("ask_recommendation", job_state={"recommendations": jobs})
    out = conversation_node(state)
    assert "job_1" in out["conversation"]["messages"][-1]["content"]
    assert out["system"]["current_node"] == "conversation"

def test_conversation_ask_skill_advice():
    state = make_state("ask_skill_advice", user_profile={"skill_analysis": "補強AI"})
    out = conversation_node(state)
    assert "補強AI" in out["conversation"]["messages"][-1]["content"]
    assert out["system"]["current_node"] == "conversation"

def test_conversation_goodbye():
    state = make_state("goodbye")
    out = conversation_node(state)
    assert "祝您求職順利" in out["conversation"]["messages"][-1]["content"]
    assert out["next_action"] == "end"
    assert out["system"]["current_node"] == "conversation"

def test_conversation_default():
    state = make_state("other", context={"user_message": "請推薦職缺"})
    out = conversation_node(state)
    assert "請推薦職缺" in out["conversation"]["messages"][-1]["content"]
    assert out["system"]["current_node"] == "conversation"
