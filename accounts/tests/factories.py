import factory

from django.contrib.auth.models import User
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
from accounts.models import Customer
from faker import Faker

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    #skip_postgeneration_save = True
    username = factory.Faker('user_name')
    password = factory.PostGenerationMethodCall('set_password', 'password')
    email = factory.Faker('email')

class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer
    user = factory.SubFactory(UserFactory)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

class EmailAddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EmailAddress

    user = factory.SubFactory(UserFactory)
    email = factory.LazyAttribute(lambda obj: obj.user.email)
    verified = False
    primary = True    

    