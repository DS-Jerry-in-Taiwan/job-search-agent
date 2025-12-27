#!/bin/bash
echo "🚀 部署智能職缺搜尋 Agent..."
docker-compose build
docker-compose up -d
echo "⏳ 等待服務啟動..."
sleep 5
curl http://localhost:8000/health
echo "✅ 部署完成！"
echo "🌐 前端: http://localhost:8501"
echo "📚 API 文檔: http://localhost:8000/docs"
