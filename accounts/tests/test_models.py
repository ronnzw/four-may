import pytest
from allauth.socialaccount.models import SocialLogin
from allauth.socialaccount.signals import social_account_added


def test_customer_str(customer):
    assert str(customer) == f'{customer.first_name} {customer.last_name}'

@pytest.mark.django_db
def test_social_account_added_signal(user_with_email, sociallogin):
    # Unpack the user and email address from the fixture
    _, email_address = user_with_email

    social_account_added.send(sender=SocialLogin, request=None, sociallogin=sociallogin)
    # Refresh the email address from the database
    email_address.refresh_from_db()
    assert email_address.verified is True