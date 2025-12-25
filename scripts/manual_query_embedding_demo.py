from src.rag.query import QueryRewriter, HyDEGenerator
from src.rag.embeddings import EmbeddingManager

def main():
    print("=== 查詢增強與向量化手動測試 ===")
    user_query = input("請輸入查詢（如：我想找台北的Python工程師工作）：\n> ")
    rewriter = QueryRewriter()
    hyde = HyDEGenerator()
    embedder = EmbeddingManager()

    # 查詢重寫
    enhanced = rewriter.rewrite(user_query)
    print(f"\n[查詢重寫結果]：{enhanced}")

    # HyDE 生成
    hyde_doc = hyde.generate_hypothetical_doc(enhanced)
    print(f"\n[HyDE 生成文檔]：\n{hyde_doc}")

    # 向量化
    vec_query = embedder.embed_text(enhanced)
    print(f"\n[查詢向量]（前10維）：{vec_query[:10]} ... (共{len(vec_query)}維)")

    vec_hyde = embedder.embed_text(hyde_doc)
    print(f"\n[HyDE 文檔向量]（前10維）：{vec_hyde[:10]} ... (共{len(vec_hyde)}維)")

if __name__ == "__main__":
    main()
