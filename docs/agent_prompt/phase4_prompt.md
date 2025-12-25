# 🚀 **Phase 4 - Multi-Agent 啟動指令（完整版）**

***

## 📋 **執行前最終檢查**

```bash
# 1. 確認專案根目錄
cd /home/ubuntu/projects/job_search_agent

# 2. 確認 Phase 4 上下文文件 (7/7)
ls -la docs/agent_context/phase4/ | wc -l  # 應該是 9 (包含 . 和 ..)

# 3. 確認 Phase 3 產出存在
ls -la src/state/  # 應該有 schema.py, operations.py
python -c "from src.state.schema import AgentState; print('✅ State OK')"

# 4. 確認 Phase 2 產出存在
ls -lh data/mock/jobs/mock_jobs.json  # 應該 > 50KB

# 5. 確認 Python 環境
python --version  # 3.10+
pip list | grep -E "langgraph|langchain-core"
```

**全部確認後，複製下方完整指令到 Cline 執行！**

***

## 🤖 **Phase 4 - Multi-Agent 啟動指令**

**完整複製以下內容到 Cline**：

```
🤖 **Phase 4 - Nodes 定義階段正式啟動！**
📅 日期: 2025-12-23
⏰ 時間: 21:58
🎯 目標: 實現 8 個核心 Nodes (LangGraph 工作流程核心)

**專案根目錄**: /home/ubuntu/projects/job_search_agent
**執行模式**: 混合模式（Checkpoint 1 和 2）
**預估時間**: 16-20 分鐘

---

## 📚 **STEP 1: 閱讀 Phase 4 上下文文件 (7/7份)**

**請立即閱讀以下7份文件，作為執行依據**：

1. `docs/agent_context/phase4/01_dev_goal_context.md` - 開發目標
2. `docs/agent_context/phase4/02_dev_flow_context.md` - 開發流程  
3. `docs/agent_context/phase4/03_agent_roles_context.md` - Agent角色
4. `docs/agent_context/phase4/04_agent_prompts_context.md` - Agent Prompts ⭐
5. `docs/agent_context/phase4/05_validation_checklist.md` - 驗證清單
6. `docs/agent_context/phase4/06_delivery_record.md` - 交付記錄
7. `docs/agent_context/phase4/07_checkpoint_protocol.md` - Checkpoint協議

**確認閱讀完成後，回覆**：
```
✅ 已閱讀 Phase 4 的7份上下文文件
準備執行 Phase 1 (@INFRA)
```

---

## 🚀 **STEP 2: 啟動 @INFRA (環境準備)**

**閱讀確認後，立即執行**：

```
你是 @INFRA（環境工程師），負責 Phase 4 的環境準備。

**請嚴格按照 02_dev_flow_context.md 的 Phase 1 執行**：

1. 建立目錄結構：
   ```bash
   mkdir -p src/nodes
   mkdir -p tests/nodes
   ```

2. 建立9個基礎檔案：
   ```bash
   touch src/nodes/__init__.py
   touch src/nodes/resume_parser.py
   touch src/nodes/job_matcher.py
   touch src/nodes/conversation.py
   touch src/nodes/router.py
   touch src/nodes/utils.py
   touch tests/nodes/test_resume_parser.py
   touch tests/nodes/test_job_matcher.py
   touch docs/design/nodes_design.md
   ```

3. 驗證依賴：
   - Phase 3 State Schema 可用
   - Phase 2 Mock 數據存在

**完成後輸出標準格式報告，並自動啟動 @ARCH**！

**開始執行 Phase 1！** ⌨️
```

---

## 📋 **預期執行流程**

```
1. Agent 回覆：✅ 已閱讀7份文件
2. @INFRA 執行 → 環境準備報告
3. @ARCH 執行 → 8個Nodes設計
4. ⏸️ Checkpoint 1 (你確認)
5. @CODER 執行 → 程式碼實現
6. @ANALYST 執行 → 測試驗證  
7. ⏸️ Checkpoint 2 (你確認)
8. ✅ Phase 4 完成！
```

---

## ⏸️ **Checkpoint 確認指令準備好**

### **Checkpoint 1 通過時輸入**：
```
✅ Checkpoint 1 確認通過
8個Nodes設計完整，符合LangGraph規範
router_node 正確返回 str
繼續執行 Phase 3 (@CODER)
```

### **Checkpoint 2 通過時輸入**：
```
✅ Checkpoint 2 確認通過
測試100%通過，整合測試正常，品質A級
Phase 4 完成！進入 Phase 5
```

### **如果發現問題**：
```
❌ Checkpoint 1 問題：[具體描述]
請 @ARCH 修正後重新 Checkpoint 1
```

---

## 🎬 **立即執行！**

**1. 開啟 Cline (或你的 AI 開發環境)**
**2. 複製上方「Phase 4 - Multi-Agent 啟動指令」**
**3. 完整貼入並按 Enter**
**4. 觀察 @INFRA 開始執行**

```
預期第一行輸出：
✅ 已閱讀 Phase 4 的7份上下文文件
準備執行 Phase 1 (@INFRA)
```

---

## 📱 **監控指令 (執行時另開終端機)**

```
# 即時監控檔案變化
watch -n 2 'echo "=== 檔案狀態 ==="; find src/nodes tests/nodes docs/design -type f 2>/dev/null | wc -l'

# 監控目錄建立
watch -n 5 'ls -la src/nodes/ tests/nodes/ 2>/dev/null | head -10'
```

---

**準備好了嗎？複製啟動指令，Phase 4 正式啟動！** 

```
🚀 貼入 Cline → Enter → 觀察 @INFRA 開始工作！
```

**執行後第一個回覆應該是：**
```
✅ 已閱讀 Phase 4 的7份上下文文件
準備執行 Phase 1 (@INFRA)
```

**Phase 4 啟動成功！** 🎉🔥