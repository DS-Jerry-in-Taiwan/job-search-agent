import pytest
from src.rag.query.rewriter import QueryRewriter

def test_rewrite_basic():
    rewriter = QueryRewriter()
    assert rewriter.rewrite("我想找台北Python後端工程師") == "Python backend engineer Taipei"
    assert rewriter.rewrite("請幫我找新竹Java前端工程師") == "Java frontend engineer Hsinchu"
    assert rewriter.rewrite("台北Python工作") == "Python job Taipei"
    assert rewriter.rewrite("新竹Java工程師") == "Java engineer Hsinchu"

def test_rewrite_empty():
    rewriter = QueryRewriter()
    with pytest.raises(ValueError):
        rewriter.rewrite("")

def test_multi_rewrite():
    rewriter = QueryRewriter()
    results = rewriter.multi_rewrite("台北Python後端工程師", top_k=3)
    assert "Python backend engineer Taipei" in results
    assert any("developer" in r or "後端" in r for r in results)
