from celery import Celery
from src.notification.websocket_manager import manager
from asgiref.sync import async_to_sync
from celery.utils.log import get_task_logger

notifier = Celery("notifier", broker="amqp://guest:guest@127.0.0.1:5672//")

# Create logger-enable to display messages on task logger.
celery_log = get_task_logger(__name__)


@notifier.task
def notification(message: dict):
    message_status = async_to_sync(manager.send_personal_message)(message)
    return message_status