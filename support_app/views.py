from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from user.models import User

from .models import Ticket
from .serializers import (TicketMessageSerializer, TicketSerializer,
                          TicketUpdateSerializer)


class TicketCreate(generics.CreateAPIView):
    """
    Creating a new ticket. Every authorized user has access.
    """

    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        applicant = User.objects.get(id=self.request.user.id)
        serializer.save(applicant=applicant)


class TicketList(generics.ListAPIView):
    """
    Getting all tickets.
    All tickets are seen only by a support employee, and a regular user only sees his own.
    """

    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_support:
            return Ticket.objects.all()

        return Ticket.objects.filter(applicant=self.request.user)


class TicketRetrieve(generics.RetrieveDestroyAPIView):
    """
    Getting a specific ticket, as well as deleting it.
    The user has access only to his own, and the employee has access to everyone.
    """

    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_support:
            return Ticket.objects.all()

        return Ticket.objects.filter(applicant=self.request.user)


class TicketUpdate(generics.UpdateAPIView):
    """
    Updating only the ticket status.
    """

    serializer_class = TicketUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_support:
            return Ticket.objects.all()

        return Ticket.objects.filter(applicant=self.request.user)


class TicketMessageCreate(generics.CreateAPIView):
    """
    Creating a message in an existing ticket.
    The employee has the ability to write to any ticket, the user only to his own.
    """

    serializer_class = TicketMessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        try:
            ticket = Ticket.objects.get(id=self.kwargs['pk'])
        except Ticket.DoesNotExist:
            ticket = None

        if self.request.user.is_support or \
                ticket.applicant_id == self.request.user.id:
            return ticket

        return None

    def perform_create(self, serializer):
        ticket_object = self.get_queryset()

        if ticket_object:
            sender = User.objects.get(id=self.request.user.id)
            serializer.save(sender=sender, ticket=ticket_object)
            ticket_object.save()
        else:
            raise ValidationError({'Error': 'Not found or no permission'})
