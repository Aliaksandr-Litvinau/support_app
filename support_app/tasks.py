import smtplib

from celery import shared_task

from support.settings import EMAIL_HOST
from support.settings import EMAIL_PASSWORD
from support.settings import EMAIL_LOGIN


@shared_task
def send_mail_change_status(email: str, ticket_id: int):
    """
    Отправка сообщения на email о том, что статус тикета был изменён
    """

    smtp_obj = smtplib.SMTP_SSL(EMAIL_HOST, smtplib.SMTP_PORT)

    smtp_obj.login(EMAIL_LOGIN, EMAIL_PASSWORD)
    message = f'Hello! Status ticket {ticket_id} was changed.'
    smtp_obj.sendmail(EMAIL_LOGIN, email, message)
    smtp_obj.quit()
