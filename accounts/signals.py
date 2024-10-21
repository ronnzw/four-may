from allauth.socialaccount.signals import social_account_added
from django.dispatch import receiver


@receiver(social_account_added)
def social_account_added_(request, sociallogin, **kwargs):
    # Automatically verify the email address for social logins
    email_address = sociallogin.user.emailaddress_set.get(email=sociallogin.user.email)
    email_address.verified = True
    email_address.save()