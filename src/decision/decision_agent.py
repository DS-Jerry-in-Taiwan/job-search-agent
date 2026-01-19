"""
Decision Agent Phase 18 - 程式實現

- 支援多種正規化策略
- 加權公式可配置
- 結構化 action plan 輸出
"""

from typing import Dict, Any, List
import numpy as np

def min_max_normalize(scores: Dict[str, float]) -> Dict[str, float]:
    min_v = min(scores.values())
    max_v = max(scores.values())
    if max_v == min_v:
        return {k: 1.0 for k in scores}
    return {k: (v - min_v) / (max_v - min_v) for k, v in scores.items()}

def z_score_normalize(scores: Dict[str, float]) -> Dict[str, float]:
    vals = list(scores.values())
    mean = np.mean(vals)
    std = np.std(vals)
    if std == 0:
        return {k: 0.0 for k in scores}
    return {k: (v - mean) / std for k, v in scores.items()}

def softmax_normalize(scores: Dict[str, float]) -> Dict[str, float]:
    vals = np.array(list(scores.values()))
    exp_vals = np.exp(vals - np.max(vals))
    softmax = exp_vals / exp_vals.sum()
    return {k: float(s) for k, s in zip(scores.keys(), softmax)}

def ratio_normalize(scores: Dict[str, float]) -> Dict[str, float]:
    total = sum(scores.values())
    if total == 0:
        return {k: 0.0 for k in scores}
    return {k: v / total for k, v in scores.items()}

NORMALIZATION_MAP = {
    "min-max": min_max_normalize,
    "z-score": z_score_normalize,
    "softmax": softmax_normalize,
    "ratio": ratio_normalize,
}

def run_decision_agent(
    case_id: str,
    raw_scores: Dict[str, float],
    weights: Dict[str, float],
    normalization_method: str = "min-max",
    action_plan_steps: List[Dict[str, str]] = None
) -> Dict[str, Any]:
    """
    輸入案例資料，回傳決策結果（含分數、加權、正規化、行動建議）
    """
    # 權重正規化
    weight_sum = sum(weights.values())
    norm_weights = {k: v / weight_sum for k, v in weights.items()}

    # 分數正規化
    norm_func = NORMALIZATION_MAP.get(normalization_method, min_max_normalize)
    normalized_raw = norm_func(raw_scores)
    # 轉換 normalized_scores key 為 schema 格式
    key_map = {
        "skill_match": "skill",
        "experience_match": "experience",
        "preference_match": "preference"
    }
    normalized_scores = {key_map[k]: v for k, v in normalized_raw.items() if k in key_map}

    final_score = sum(
        normalized_scores[k] * norm_weights[k]
        for k in normalized_scores
        if k in norm_weights
    )

    # 結構化行動建議
    action_plan = action_plan_steps or [
        {"step": "Review Resume", "description": "確認履歷內容與職缺需求對齊"},
        {"step": "Skill Enhancement", "description": "針對弱項技能進行補強"},
        {"step": "Apply Job", "description": "投遞推薦職缺"}
    ]

    return {
        "case_id": case_id,
        "raw_scores": raw_scores,
        "weights": norm_weights,
        "normalized_scores": normalized_scores,
        "normalization_method": normalization_method,
        "final_score": final_score,
        "action_plan": action_plan
    }
