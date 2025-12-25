# 🚀 **Phase 5 - Multi-Agent 啟動指令（完整版）**

***

## 📋 **執行前最終檢查**

```bash
# 1. 確認專案根目錄
cd /home/ubuntu/projects/job_search_agent

# 2. 確認 Phase 5 上下文文件 (7/7)
ls -la docs/agent_context/phase5/ | wc -l  # 應該是 9 (包含 . 和 ..)

# 3. 確認 Phase 3 產出存在
ls -la src/state/schema.py
python -c "from src.state.schema import AgentState; print('✅ State OK')"

# 4. 確認 Phase 4 產出存在
ls -la src/nodes/
python -c "from src.nodes import resume_parser_node, router_node; print('✅ Nodes OK')"

# 5. 確認 LangGraph 已安裝
python -c "from langgraph.graph import StateGraph, END; print('✅ LangGraph OK')"
```

**全部確認後，複製下方完整指令到 Cline 執行！**

***

## 🤖 **Phase 5 - Multi-Agent 啟動指令**

**完整複製以下內容到 Cline**：

```
🤖 **Phase 5 - Graph 構建階段正式啟動！**
📅 日期: 2025-12-24
⏰ 時間: 12:25
🎯 目標: 使用 LangGraph 構建完整工作流程圖

**專案根目錄**: /home/ubuntu/projects/job_search_agent
**執行模式**: 自動執行（無 Checkpoint）⚡
**預估時間**: 10-12 分鐘

---

## 📚 **STEP 1: 閱讀 Phase 5 上下文文件 (7/7份)**

**請立即閱讀以下7份文件，作為執行依據**：

1. `docs/agent_context/phase5/01_dev_goal_context.md` - 開發目標
2. `docs/agent_context/phase5/02_dev_flow_context.md` - 開發流程  
3. `docs/agent_context/phase5/03_agent_roles_context.md` - Agent角色
4. `docs/agent_context/phase5/04_agent_prompts_context.md` - Agent Prompts ⭐
5. `docs/agent_context/phase5/05_validation_checklist.md` - 驗證清單
6. `docs/agent_context/phase5/06_delivery_record.md` - 交付記錄
7. `docs/agent_context/phase5/07_checkpoint_protocol.md` - 執行模式說明

**確認閱讀完成後，回覆**：
```
✅ 已閱讀 Phase 5 的7份上下文文件
準備執行 Phase 1 (@INFRA)
```

---

## 🚀 **STEP 2: 啟動 @INFRA (環境準備)**

**閱讀確認後，立即執行**：

```
你是 @INFRA（環境工程師），負責 Phase 5 的環境準備。

**請嚴格按照 02_dev_flow_context.md 的 Phase 1 執行**：

1. 建立目錄結構：
   ```bash
   mkdir -p src/graph
   mkdir -p tests/graph
   ```

2. 建立5個基礎檔案：
   ```bash
   touch src/graph/__init__.py
   touch src/graph/workflow.py
   touch tests/graph/__init__.py
   touch tests/graph/test_workflow.py
   touch docs/design/graph_design.md
   ```

3. 驗證依賴：
   - Phase 3 State Schema 可用
   - Phase 4 Nodes 可用
   - LangGraph 套件可用

**完成後輸出標準格式報告，並自動啟動 @ARCH！**

**⚠️ 重要提示**: Phase 5 無 Checkpoint，全程自動執行！

**開始執行 Phase 1！** ⌨️
```

---

## 📋 **預期執行流程**

```
1. Agent 回覆：✅ 已閱讀7份文件
2. @INFRA 執行 → 環境準備報告 → 自動啟動 @ARCH
3. @ARCH 執行 → Graph架構設計 → 自動啟動 @CODER
4. @CODER 執行 → 程式碼實現 → 自動啟動 @ANALYST
5. @ANALYST 執行 → 測試驗證報告
6. ✅ Phase 5 完成！

⚡ 無 Checkpoint，全程自動執行！
總時間: 10-12 分鐘
```

---

## 🎯 **Phase 5 核心產出**

```
src/graph/
├─ __init__.py           # 導出 Graph
└─ workflow.py           # 核心工作流程 ⭐
   ├─ StateGraph 建立
   ├─ 8個Nodes加入
   ├─ 固定Edges定義 (6個)
   ├─ 條件Edges定義 (1個)
   └─ Graph編譯

tests/graph/
├─ __init__.py
└─ test_workflow.py      # 4+ 測試案例

docs/design/
└─ graph_design.md       # 設計文檔
```

---

## 🎬 **立即執行！**

**1. 開啟 Cline (或你的 AI 開發環境)**
**2. 複製上方「Phase 5 - Multi-Agent 啟動指令」**
**3. 完整貼入並按 Enter**
**4. 觀察 @INFRA 開始執行**

```
預期第一行輸出：
✅ 已閱讀 Phase 5 的7份上下文文件
準備執行 Phase 1 (@INFRA)
```

---

## 📱 **監控指令 (執行時另開終端機)**

```
# 即時監控檔案變化
watch -n 2 'echo "=== Phase 5 檔案狀態 ==="; find src/graph tests/graph docs/design -type f 2>/dev/null | grep -E "(workflow|graph)" | wc -l'

# 監控目錄建立
watch -n 5 'ls -la src/graph/ tests/graph/ 2>/dev/null | head -10'
```

---

## ✅ **執行完成後的驗證**

**Phase 5 完成時，執行以下驗證**：

```
# 1. 檢查檔案完整性
echo "=== 檔案檢查 ==="
ls -la src/graph/ tests/graph/ docs/design/graph_design.md

# 2. 執行測試
echo "=== 測試執行 ==="
pytest tests/graph/ -v --cov=src/graph

# 3. 端到端測試
echo "=== 端到端測試 ==="
python -c "
from src.graph import create_workflow
from src.state.operations import create_initial_state

app = create_workflow()
state = create_initial_state()
result = app.invoke(state)

print(f'✅ 技能數: {len(result[\"user_profile\"][\"skills\"])}')
print(f'✅ 職缺數: {len(result[\"job_state\"][\"matched_jobs\"])}')
print(f'✅ 狀態: {result[\"system\"][\"workflow_status\"]}')
print(f'✅ 完成: {result[\"is_complete\"]}')
"

# 4. 類型檢查
echo "=== 類型檢查 ==="
mypy src/graph/ --strict
```

**預期結果**：
```
✅ 5 個檔案都存在
✅ 測試 4/4 通過
✅ 端到端測試輸出正確
✅ 類型檢查 No issues found
```

---

## 🎉 **Phase 5 完成標準**

```
Phase 5 成功條件:

✅ src/graph/workflow.py 存在且可執行
✅ create_workflow() 函數正常
✅ app.invoke(state) 執行成功
✅ 測試 100% 通過
✅ 端到端測試成功
✅ 類型檢查通過
✅ 文檔完整

→ 滿足以上所有條件 = Phase 5 成功！
→ 可進入 Phase 6 (測試與優化)
```

---

## 📊 **整體進度追蹤**

```
✅ Day 1 - 步驟1: Phase 2 Mock 數據 (完成)
✅ Day 1 - 步驟2: Phase 3 State Schema (完成)
✅ Day 1 - 步驟3: Phase 4 Nodes 定義 (完成)
⏳ Day 1 - 步驟4: Phase 5 Graph 構建 (執行中) ← 目前位置
⏳ Day 1 - 步驟5: Phase 6 測試與優化
⏳ Day 1 - 步驟6: Phase 7 文檔整理

進度: ████████████████░░░░ 75%
```

---

**準備好了嗎？複製啟動指令，Phase 5 正式啟動！** 

```
🚀 貼入 Cline → Enter → 觀察 @INFRA 開始工作！
```

**執行後第一個回覆應該是：**
```
✅ 已閱讀 Phase 5 的7份上下文文件
準備執行 Phase 1 (@INFRA)
```

**Phase 5 啟動成功！無 Checkpoint，10-12 分鐘自動完成！** 🎉⚡

[1](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bd2b55bd-7af4-4ede-b0d3-b1c500363f1c/f5e07aaa-9d79-42d2-99bb-ebbbf430b7a1/Function_Calling.txt)
[2](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bd2b55bd-7af4-4ede-b0d3-b1c500363f1c/a59df4b0-bea9-4aa4-b1c0-d3e850c2fe51/LangChain_LangGraphJia-Gou-Yu-Mo-Zu-Jiao-Hu-Tu.txt)
[3](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bd2b55bd-7af4-4ede-b0d3-b1c500363f1c/3c869765-738f-429b-a949-11b92fd064dd/LangChainYu-LangGraphGuan-Xi-Yu-Gong-Neng-Jiao-Se-Tong-Zheng-Xiao-Jie.txt)
[4](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bd2b55bd-7af4-4ede-b0d3-b1c500363f1c/28f90fcd-ee04-4158-bf12-4c20cf3499e2/LangChainYu-LangGraphGuan-Xi-Yu-Gong-Neng-Jiao-Se-Xiao-Jie.txt)
[5](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bd2b55bd-7af4-4ede-b0d3-b1c500363f1c/f5a8f6a6-06c9-46da-b744-9b031735d34f/Xiao-Jie-Mo-Ban.txt)
[6](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bd2b55bd-7af4-4ede-b0d3-b1c500363f1c/25791d3d-08e3-43b7-aac8-50a7a208d55f/AI_Agent_Shi-Zuo.txt)
[7](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bd2b55bd-7af4-4ede-b0d3-b1c500363f1c/4dde3a8c-0667-42ac-ae12-a6cb423c6042/7Tian-Zui-Xiao-MVPKai-Fa-Gui-Hua.txt)
[8](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63205066/f30db57e-42d3-490f-94a9-4b390b37464e/Li-Yue-Jun-v4.pdf)
[9](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63205066/e7ae2848-db4c-4eea-ac53-cd4f9072c75f/Kai-Fa-Tuan-Dui-De-AgentFen-Gong.txt)
[10](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63205066/eb7aff03-5542-4fbe-8684-1161cc06a9c2/multiagents-Kai-Fa-Jia-Gou.txt)
[11](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63205066/382dae24-4e08-4141-809e-d84f052beb98/Multi-Agent-Wan-Zheng-Chu-Shi-Hua-Liu-Cheng-Prompt-6Bu-Zou-Biao-Zhun-Ban.txt)
[12](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63205066/87ab24da-919c-4970-8f50-d55117982810/Multi-Agent-Wan-Zheng-Chu-Shi-Hua-Liu-Cheng-Prompt-6Bu-Zou-Biao-Zhun-Ban.txt)
[13](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63205066/36ba0f9c-758d-43a8-a97a-2de556a78e4c/Multi-Agent-Wan-Zheng-Chu-Shi-Hua-Liu-Cheng-Prompt-6Bu-Zou-Biao-Zhun-Ban.txt)
[14](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63205066/99e7f29b-2996-4f4c-a97c-e79c1386b142/Multi-Agent-Wan-Zheng-Chu-Shi-Hua-Liu-Cheng-Prompt-6Bu-Zou-Biao-Zhun-Ban.txt)
[15](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63205066/03f2bd94-92f7-44f6-a5b7-c40e8613eddd/Multi-Agent-Wan-Zheng-Chu-Shi-Hua-Liu-Cheng-Prompt-6Bu-Zou-Biao-Zhun-Ban.txt)
[16](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63205066/8fce35b9-98fa-48da-be30-b2fe39a4668b/Multi-Agent-Wan-Zheng-Chu-Shi-Hua-Liu-Cheng-Prompt-6Bu-Zou-Biao-Zhun-Ban-v3.txt)
[17](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63205066/2d127936-b702-42f4-8f5c-bfc956b6ea7f/06_delivery_record.md)
[18](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63205066/3318c203-20bf-4aab-b442-44df6696dcec/multi_agent_dev_workflow_v4.0.md)
[19](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63205066/f73a9d85-e428-4ab7-a662-416a169dd770/AIShi-Dai-Qiu-Zhi-Zhi-Sheng-Gong-Lue.pdf)
[20](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/63205066/56ce3924-0c0d-4db6-b74e-584d1798a9a1/1111Ren-Li-Yin-Xing-AIGong-Ju-_flow.jpg)
[21](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63205066/feb67fc0-d78c-40f1-9913-662a7b450f06/AI-Gong-Cheng-Shi-1111Ren-Li-Yin-Xing-Mian-Shi-Yao-Qing-Tong-Zhi-jerry800130-gmail.com-Gmail.pdf)
[22](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63205066/ab421833-a64e-49b6-a301-a5259de65f03/Mian-Shi-Jian-Bao-Jia-Gou.txt)
[23](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/63205066/affe43f5-c25b-4a24-9f8d-4fdc7f177036/Mian-Shi-Jian-Bao-Jia-Gou-Shuo-Ming.txt)
[24](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/63205066/7a571645-0a00-4750-87d3-c63ff3e0bff2/image.jpg)