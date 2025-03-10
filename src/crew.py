from crewai import Agent, Task, Crew, Process

    # Definujeme agenty
    context_master = Agent.from_yaml('config/agents.yaml', 'context_master')
    context_manager_1 = Agent.from_yaml('config/agents.yaml', 'context_manager_1')
    context_manager_2 = Agent.from_yaml('config/agents.yaml', 'context_manager_2')
    code_generator = Agent.from_yaml('config/agents.yaml', 'code_generator')
    code_reviewer = Agent.from_yaml('config/agents.yaml', 'code_reviewer')
    tester = Agent.from_yaml('config/agents.yaml', 'tester')
    user_communication = Agent.from_yaml('config/agents.yaml', 'user_communication')

    # Definujeme úkoly
    plan_next_task = Task.from_yaml('config/tasks.yaml', 'plan_next_task')
    assign_context = Task.from_yaml('config/tasks.yaml', 'assign_context')
    generate_code = Task.from_yaml('config/tasks.yaml', 'generate_code')
    review_code = Task.from_yaml('config/tasks.yaml', 'review_code')
    run_tests = Task.from_yaml('config/tasks.yaml', 'run_tests')
    handle_user_decision = Task.from_yaml('config/tasks.yaml', 'handle_user_decision')

    # CrewAI nastavení – agenti + úkoly
    crew = Crew(
        agents=[context_master, context_manager_1, context_manager_2, 
                code_generator, code_reviewer, tester, user_communication],
        tasks=[plan_next_task, assign_context, generate_code, 
               review_code, run_tests, handle_user_decision],
        process=Process.sequential  # Úkoly poběží postupně (může být i parallel)
    )
