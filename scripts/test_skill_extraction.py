from src.nodes.resume_parser import extract_skills_from_text
if __name__ == "__main__":
    text = """個 男  31   
狀 在中
主⼿ 0988-783-059
E-mail workmk666@gmail.com
...
•技： Python, SQL, Linux ShellAI型開
•：⽤型預測
•技： PyTorch,  Scikit-learn,
ONNX, Langchain, Langgraph
#AI #習  # 習  #LLM理
...
•技： Docker , LXD, Kubernetes,
AWS
...
•技棧： Python 、 LangChain 、 LangGraph 、 Chroma DB 、
OpenAI GPT  API
"""
print(extract_skills_from_text(text))
