from typing import Dict, Any, List
import numpy as np

class DecisionAgent:
    """
    決策 Agent，負責分數計算、正規化、分流與行動建議
    """
    def __init__(self):
        self.NORMALIZATION_MAP = {
            "min-max": self.min_max_normalize,
            "z-score": self.z_score_normalize,
            "softmax": self.softmax_normalize,
            "ratio": self.ratio_normalize,
        }

    def min_max_normalize(self, scores: Dict[str, float]) -> Dict[str, float]:
        min_v = min(scores.values())
        max_v = max(scores.values())
        if max_v == min_v:
            return {k: 1.0 for k in scores}
        return {k: (v - min_v) / (max_v - min_v) for k, v in scores.items()}

    def z_score_normalize(self, scores: Dict[str, float]) -> Dict[str, float]:
        vals = list(scores.values())
        mean = np.mean(vals)
        std = np.std(vals)
        if std == 0:
            return {k: 0.0 for k in scores}
        return {k: (v - mean) / std for k, v in scores.items()}

    def softmax_normalize(self, scores: Dict[str, float]) -> Dict[str, float]:
        vals = np.array(list(scores.values()))
        exp_vals = np.exp(vals - np.max(vals))
        softmax = exp_vals / exp_vals.sum()
        return {k: float(s) for k, s in zip(scores.keys(), softmax)}

    def ratio_normalize(self, scores: Dict[str, float]) -> Dict[str, float]:
        total = sum(scores.values())
        if total == 0:
            return {k: 0.0 for k in scores}
        return {k: v / total for k, v in scores.items()}

    def decide(
        self,
        case_id: str,
        raw_scores: Dict[str, float],
        weights: Dict[str, float],
        normalization_method: str = "min-max",
        action_plan_steps: List[Dict[str, str]] = None
    ) -> Dict[str, Any]:
        weight_sum = sum(weights.values())
        norm_weights = {k: v / weight_sum for k, v in weights.items()}

        norm_func = self.NORMALIZATION_MAP.get(normalization_method, self.min_max_normalize)
        normalized_raw = norm_func(raw_scores)
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
