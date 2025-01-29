import psutil

def get_metrics() -> dict:
    return {
        "cpu_usage": psutil.cpu_percent(interval=1),
        "mem_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage("/").percent
    }