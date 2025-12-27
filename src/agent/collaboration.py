from typing import List, Any, Dict
from dataclasses import dataclass, field
import asyncio

@dataclass
class Task:
    task_id: str
    intent: str
    agent_name: str
    input_data: Dict

@dataclass
class Result:
    task_id: str
    agent_name: str
    output: Any
    metadata: Dict = field(default_factory=dict)

class AgentCollaboration:
    async def execute_parallel(self, tasks: List[Task], agent_map: Dict[str, Any]) -> List[Result]:
        async def run_task(task: Task):
            agent = agent_map[task.agent_name]
            output = await self._maybe_async(agent.run)(task.input_data.get("task", ""), task.input_data)
            return Result(task_id=task.task_id, agent_name=task.agent_name, output=output)
        return await asyncio.gather(*(run_task(t) for t in tasks))

    async def execute_sequential(self, tasks: List[Task], agent_map: Dict[str, Any]) -> List[Result]:
        results = []
        for task in tasks:
            agent = agent_map[task.agent_name]
            output = await self._maybe_async(agent.run)(task.input_data.get("task", ""), task.input_data)
            results.append(Result(task_id=task.task_id, agent_name=task.agent_name, output=output))
        return results

    @staticmethod
    def _maybe_async(func):
        if asyncio.iscoroutinefunction(func):
            return func
        async def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
