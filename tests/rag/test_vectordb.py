import pytest
import numpy as np
from src.rag.vectordb import FaissVectorStore, InMemoryVectorStore

@pytest.fixture(params=["faiss", "memory"])
def store(request):
    dim = 8
    if request.param == "faiss":
        return FaissVectorStore(dim=dim)
    else:
        return InMemoryVectorStore(dim=dim)

def random_vec(dim):
    return np.random.rand(dim).astype("float32").tolist()

def random_meta(i):
    return {"job_id": f"job{i}", "location": "Taipei" if i % 2 == 0 else "Hsinchu"}

def test_vector_store_init(store):
    assert store.dim == 8

def test_add_single_vector(store):
    vec = random_vec(8)
    meta = random_meta(0)
    ids = store.add([vec], [meta])
    assert len(ids) == 1

def test_add_batch_vectors(store):
    vecs = [random_vec(8) for _ in range(10)]
    metas = [random_meta(i) for i in range(10)]
    ids = store.add(vecs, metas)
    assert len(ids) == 10

def test_search_similarity(store):
    vecs = [random_vec(8) for _ in range(5)]
    metas = [random_meta(i) for i in range(5)]
    store.add(vecs, metas)
    q = vecs[0]
    results = store.search(q, top_k=3)
    assert len(results) == 3
    assert results[0]["score"] <= results[1]["score"]

def test_search_top_k(store):
    vecs = [random_vec(8) for _ in range(20)]
    metas = [random_meta(i) for i in range(20)]
    store.add(vecs, metas)
    q = vecs[0]
    results = store.search(q, top_k=5)
    assert len(results) == 5

def test_search_with_filters(store):
    vecs = [random_vec(8) for _ in range(10)]
    metas = [random_meta(i) for i in range(10)]
    store.add(vecs, metas)
    q = random_vec(8)
    results = store.search(q, top_k=10, filters={"location": "Taipei"})
    for r in results:
        assert r["metadata"]["location"] == "Taipei"

def test_save_load_index(tmp_path, store):
    vecs = [random_vec(8) for _ in range(5)]
    metas = [random_meta(i) for i in range(5)]
    ids = store.add(vecs, metas)
    store.save(str(tmp_path / "testidx"))
    # 新建一個 store
    if isinstance(store, FaissVectorStore):
        new_store = FaissVectorStore(dim=8)
    else:
        new_store = InMemoryVectorStore(dim=8)
    new_store.load(str(tmp_path / "testidx"))
    results = new_store.search(vecs[0], top_k=2)
    assert len(results) == 2

def test_empty_search(store):
    q = random_vec(8)
    results = store.search(q, top_k=3)
    assert results == []

def test_dimension_mismatch(store):
    vec = random_vec(7)
    meta = random_meta(0)
    with pytest.raises(ValueError):
        store.add([vec], [meta])
    q = random_vec(7)
    with pytest.raises(ValueError):
        store.search(q, top_k=1)

def test_large_scale(store):
    vecs = [random_vec(8) for _ in range(1000)]
    metas = [random_meta(i) for i in range(1000)]
    store.add(vecs, metas)
    q = vecs[0]
    results = store.search(q, top_k=10)
    assert len(results) == 10
