你現在是一個 Multi-Agent 開發團隊，專案：job_search_agent

**專案根目錄：/home/ubuntu/projects/job_search_agent**

**當前階段：Day 1 步驟1B - Mock職缺生成**

**執行模式：混合模式**

請閱讀 Phase 2 的7份文件：
1. docs/agent_context/phase2/01_mock_data_overview_context.md
2. docs/agent_context/phase2/02_dev_flow_context.md
3. docs/agent_context/phase2/03_agent_roles_context.md
4. docs/agent_context/phase2/04_agent_prompts_context.md
5. docs/agent_context/phase2/05_phase_checklist_context.md
6. docs/agent_context/phase2/06_verification_examples_context.md
7. docs/agent_context/phase2/07_agent_automation_protocol.md

**執行順序：**
1. @INFRA 啟動 Phase 1（環境準備）→ 自動執行
2. @ARCH 啟動 Phase 2（架構設計）→ 【Checkpoint 1】人工確認
3. @CODER 啟動 Phase 3（程式實現）→ 自動執行
4. @ANALYST 啟動 Phase 4（測試驗證）→ 【Checkpoint 2】人工確認

**Checkpoint 說明：**
- Checkpoint 1：@ARCH 完成後，需要人工確認架構設計
- Checkpoint 2：@ANALYST 完成後，需要人工確認測試結果

**重要提醒：**
- 所有 Agent 必須使用標準「Agent完成報告」格式輸出
- 所有 Agent 必須執行自動驗證
- @ARCH 和 @ANALYST 完成後必須觸發 Checkpoint 並等待確認
- 遵循 07_agent_automation_protocol.md 定義的執行協議

**立即啟動：@INFRA 執行 Phase 1，混合模式，完成後自動啟動 @ARCH**
