import smtplib

from celery import shared_task

from support.settings import EMAIL_HOST, EMAIL_LOGIN, EMAIL_PASSWORD


@shared_task
def send_mail_change_status(email: str, ticket_id: int):
    """
    Sending an email message that the ticket status has been changed
    """

    smtp_obj = smtplib.SMTP_SSL(EMAIL_HOST, smtplib.SMTP_PORT)

    smtp_obj.login(EMAIL_LOGIN, EMAIL_PASSWORD)
    message = f'Hello! Status ticket {ticket_id} was changed.'
    smtp_obj.sendmail(EMAIL_LOGIN, email, message)
    smtp_obj.quit()
