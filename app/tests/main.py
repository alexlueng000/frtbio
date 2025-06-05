from app.tasks import test_task

if __name__ == "__main__":
    result = test_task.apply_async(args=["Hello Celery!"], countdown=10)
    print("任务已派发，ID:", result.id)