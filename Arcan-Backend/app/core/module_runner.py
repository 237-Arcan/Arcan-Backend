from core.monitoring.module_status_manager import ModuleStatusManager
def run_module(module_name, module_func):
    start = time.time()
    try:
        result = module_func()
        duration = round(time.time() - start, 2)
        log_module_execution(module_name, str(result)[:150], "success", duration)
        return result
    except Exception as e:
        duration = round(time.time() - start, 2)
        log_module_execution(module_name, f"Error: {e}", "failure", duration)
        return None
