from django.core.management.base import BaseCommand
from django.db import DatabaseError, transaction
from ...utilities.utility import mass_insert_into_tables
from profiles.models import ProfileStatus, Avatar
from apiauthentication.models import TokenStatus, TokenType
from sessionmanagement.models import SessionStatus
from chat.models import ChatRequestStatus


class Command(BaseCommand):
    help = 'Import master table data like status, type tables.'
    mass_insert_data = [
        {
            'modal_name': TokenStatus,
            'entries': [
                {
                    'status_name': 'Active',
                },
                {
                    'status_name': 'Inactive',
                },
                {
                    'status_name': 'Pending Activation',
                },
                {
                    'status_name': 'Suspended',
                },
            ]
        },
        {
            'modal_name': TokenType,
            'entries': [
                {
                    'type_name': 'Website',
                },
                {
                    'type_name': 'Mobile App',
                },
            ]
        },
        {
            'modal_name': SessionStatus,
            'entries': [
                {
                    'status_name': 'Active',
                },
                {
                    'status_name': 'Inactive',
                },
                {
                    'status_name': 'Expired',
                },
            ]
        },
        {
            'modal_name': ProfileStatus,
            'entries': [
                {
                    'status_name': 'Active',
                },
                {
                    'status_name': 'Active',
                },
            ]
        },
        {
            'modal_name': Avatar,
            'entries': [
                {
                    'avatar_name': 'avatar-skull-old-school',
                },
                {
                    'avatar_name': 'avatar-wha-twat',
                },
                {
                    'avatar_name': 'avatar-stud-fudge-hair',
                },
                {
                    'avatar_name': 'avatar-emo-maeve',
                },
                {
                    'avatar_name': 'avatar-hombre-de-mehico',
                },
                {
                    'avatar_name': 'avatar-neco-robin-chan',
                },
                {
                    'avatar_name': 'avatar-soul-king-brook',
                },
                {
                    'avatar_name': 'avatar-naruko-anjou-chan',
                },
            ]
        },
        {
            'modal_name': ChatRequestStatus,
            'entries': [
                {
                    'status_name': 'Sent',
                },
                {
                    'status_name': 'Accepted',
                },
                {
                    'status_name': 'Rejected',
                },
                {
                    'status_name': 'Withdrawn',
                },
            ]
        },
    ]

    def handle(self, *srgs, **options):
        self.stdout.write(
            '_______ Began: adding to master tables _______ '
        )
        try:
            with transaction.atomic():
                mass_insert_into_tables(self.mass_insert_data)
                self.stdout.write(
                    '_______ END: master tables added to DB successfully _______ '
                )
        except DatabaseError as db_exc:
            self.stdout.write(
                '_______ Error: in DB, failed to add master tables to DB  _______ \n%s' % db_exc
            )
        except Exception as exc:
            self.stdout.write(
                '_______ Error: occured while added to master tables  _______ \n%s' % exc
            )
