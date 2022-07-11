from django.db import models


class TicketStatus(models.TextChoices):
    """
    Model of the current status of the application
    """

    TO_DO = 'To Do'
    IN_PROGRESS = 'In progress'
    DONE = 'Done'


class TicketMessage(models.Model):
    """
    The message model for the application
    """

    ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE,
                               related_name='messages',
                               verbose_name='Messages')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Time of message creation')
    text = models.TextField(max_length=200, blank=False, null=False,
                            verbose_name='Message content')
    sender = models.ForeignKey('user.User', on_delete=models.CASCADE,
                               verbose_name='Sender')

    def __str__(self):
        return self.text


class Ticket(models.Model):
    """
    The model of the user's request to technical support
    """

    title = models.CharField(max_length=50, verbose_name='Message name')
    applicant = models.ForeignKey('user.User', on_delete=models.CASCADE,
                                  verbose_name='Sender')
    status = models.CharField(max_length=25, choices=TicketStatus.choices,
                              default=TicketStatus.TO_DO,
                              verbose_name='Message status')
    description = models.TextField(max_length=500, blank=False,
                                   verbose_name='Description of the problem')
    created_at = models.DateTimeField(auto_now_add=True, editable=False,
                                      verbose_name='Creation time')
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='The time of the last updates')

    def __str__(self):
        return self.title
