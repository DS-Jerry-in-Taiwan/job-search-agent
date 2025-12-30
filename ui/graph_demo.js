// 前端 demo：串接 /graph/visualize 並渲染 mermaid 流程圖
// 假設使用 mermaid.js，請於 HTML 引入 mermaid.min.js

async function fetchGraph() {
  const resp = await fetch("http://localhost:8000/api/v1/graph/visualize");
  const data = await resp.json();
  const mermaidStr = data.graph_svg;
  console.log("mermaidStr:", mermaidStr);
  // 插入 mermaid 代碼，確保格式正確
  const graphDiv = document.getElementById("graph-mermaid");
  graphDiv.innerHTML = `<div class="mermaid">${mermaidStr}</div>`;
  
  // 等待 DOM 更新後再初始化
  setTimeout(() => {
    if (window.mermaid) {
      window.mermaid.init(undefined, document.querySelectorAll(".mermaid"));
    }
  }, 0);
}

// 頁面載入後自動執行
window.onload = fetchGraph;
