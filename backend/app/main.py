from fastapi import FastAPI
from app.schemas import TaskInput, PlanResponse
from app.agents.task_decomposer import run_task_decomposer
from app.agents.time_estimator import estimate_time
from app.agents.priority_agent import assign_priority
from app.planner.scheduler import build_day_wise_plan
from app.utils.markdown_exporter import generate_markdown
from concurrent.futures import ThreadPoolExecutor

app = FastAPI(title="AI Task Planning Agent")

executor = ThreadPoolExecutor(max_workers=2)

@app.post("/generate-plan", response_model=PlanResponse)
def generate_plan(data: TaskInput):
    tasks = run_task_decomposer(data.goal, data.days)
    
    time_future = executor.submit(estimate_time, tasks, data.days)
    priority_future = executor.submit(assign_priority, tasks)
    
    time_map = time_future.result()
    priority_map = priority_future.result()
    
    final_plan = []
    
    for task in tasks:
        final_plan.append({
            "task": task,
            "estimated_days": time_map.get(task, 1),
            "priority": priority_map.get(task, "Medium")
        })
        
    schedule = build_day_wise_plan(final_plan)
    markdown = generate_markdown(data.goal, schedule)
        
    return {
        "goal": data.goal,
        "days": data.days,
        "plan": final_plan,
        "markdown": markdown
    }