import pytest
from src.rag.query.rewriter import QueryRewriter
from src.rag.query.hyde import HyDEGenerator
from src.rag.query.decomposer import QueryDecomposer

@pytest.fixture
def rewriter():
    return QueryRewriter()

@pytest.fixture
def hyde():
    return HyDEGenerator()

@pytest.fixture
def decomposer():
    return QueryDecomposer()

def test_query_rewriter_basic(rewriter):
    assert rewriter.rewrite("我想找台北的Python後端工程師工作") == "Python backend engineer job Taipei"

def test_query_rewriter_multilingual(rewriter):
    assert "backend" in rewriter.rewrite("請幫我找新竹的Java後端工程師工作")

def test_query_multi_rewrite(rewriter):
    results = rewriter.multi_rewrite("台北Python後端工程師工作", top_k=2)
    assert len(results) == 2
    assert "backend" in results[0]

def test_query_rewriter_empty(rewriter):
    with pytest.raises(ValueError):
        rewriter.rewrite("")

def test_query_rewriter_strip_redundant(rewriter):
    assert "請幫我" not in rewriter.rewrite("請幫我找台北的Python後端工程師工作")

def test_query_rewriter_variation(rewriter):
    results = rewriter.multi_rewrite("台北Python後端工程師工作", top_k=3)
    assert any("developer" in r or "engineer" in r for r in results)

def test_query_rewriter_chinese_to_english(rewriter):
    out = rewriter.rewrite("新竹的Java後端工程師工作")
    assert "Java backend engineer job Hsinchu" in out

def test_query_rewriter_invalid_type(rewriter):
    with pytest.raises(ValueError):
        rewriter.rewrite(None)

def test_hyde_generation(hyde):
    doc = hyde.generate_hypothetical_doc("Python backend engineer job Taipei")
    assert "We are seeking a talented Python backend engineer job Taipei." in doc

def test_hyde_quality(hyde):
    doc = hyde.generate_hypothetical_doc("Python backend engineer job Taipei")
    score = hyde.evaluate_quality(doc)
    assert score >= 0.75

def test_hyde_multiple(hyde):
    docs = hyde.generate_multiple("Python backend engineer job Taipei", top_k=2)
    assert len(docs) == 2
    assert any("frontend" in d or "backend" in d for d in docs)

def test_decomposer_basic(decomposer):
    queries = decomposer.decompose("台北Python後端工程師工作 或 新竹Java後端工程師工作")
    assert "台北Python後端工程師工作" in queries
    assert "新竹Java後端工程師工作" in queries

def test_decomposer_and_or(decomposer):
    queries = decomposer.decompose("台北Python後端工程師工作 和 新竹Java後端工程師工作 或 台北Java前端工程師工作")
    assert len(queries) >= 3

def test_decomposer_empty(decomposer):
    with pytest.raises(ValueError):
        decomposer.decompose("")

def test_decomposer_merge_results(decomposer):
    results = [["A", "B"], ["B", "C"], "D"]
    merged = decomposer.merge_results(results)
    assert set(merged) == {"A", "B", "C", "D"}
