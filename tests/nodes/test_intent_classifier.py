import pytest
from src.nodes.conversation import intent_classifier

def test_rule_based_greet():
    result = intent_classifier("你好，請推薦職缺", enable_rule=True, enable_ml=False, enable_llm=False)
    assert result["intent"] == "greet"
    assert result["confidence"] == 1.0

def test_rule_based_goodbye():
    result = intent_classifier("謝謝，再見", enable_rule=True, enable_ml=False, enable_llm=False)
    assert result["intent"] == "goodbye"
    assert result["confidence"] == 1.0

def test_rule_based_recommend():
    result = intent_classifier("請推薦適合我的職缺", enable_rule=True, enable_ml=False, enable_llm=False)
    assert result["intent"] == "ask_recommendation"
    assert result["confidence"] == 1.0

def test_rule_based_skill():
    result = intent_classifier("請分析我的技能缺乏", enable_rule=True, enable_ml=False, enable_llm=False)
    assert result["intent"] == "ask_skill_advice"
    assert result["confidence"] == 1.0

def test_rule_based_resume():
    result = intent_classifier("我有5年工程師經驗", enable_rule=True, enable_ml=False, enable_llm=False)
    assert result["intent"] == "provide_resume"
    assert result["confidence"] == 1.0

def test_fallback_manual_review():
    result = intent_classifier("這是一個無法分類的訊息", enable_rule=True, enable_ml=False, enable_llm=False)
    assert result["intent"] == "manual_review"
    assert result["confidence"] == 0.0
