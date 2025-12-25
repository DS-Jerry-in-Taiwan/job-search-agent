# Provider Interface 規範

## BaseProvider (抽象基類)
- 檔案：src/data_providers/base_provider.py
- 定義 fetch_jobs(self, **kwargs)
- 所有 Provider 必須繼承此類

## MockProvider (Mock 實現)
- 檔案：src/data_providers/mock_provider.py
- 繼承 BaseProvider
- 實作 fetch_jobs(self, **kwargs)
- 用於生成與讀取 Mock 職缺數據

## CrawlerProvider (預留擴展)
- 尚未實作，預留於未來 Phase
- 建議繼承 BaseProvider，並於 fetch_jobs raise NotImplementedError

## 類別結構
```
BaseProvider (ABC)
  ├── MockProvider
  └── CrawlerProvider (reserved)
```

## 命名規範
- 檔案命名：base_provider.py, mock_provider.py
- 類別命名：BaseProvider, MockProvider, CrawlerProvider

## 匹配度計算邏輯
- 由 MockProvider 依據 Schema 實作
- 可擴展至 CrawlerProvider
