from playwright.sync_api import Page
from tests.pages.auth import SignupPage, ConfirmationPage
from django.core import mail
import re
from app.models import UserProfile
from allauth.account.models import EmailAddress


def test_signup(page: Page):
    page.goto("/")
    signup_page = SignupPage(page)
    signup_page.email_field.fill("test@example.com")
    signup_page.password_field.fill("test_password123")
    signup_page.signup_button.click()

    confirmation_link = re.search(
        r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
        mail.outbox[0].body,
    ).group()

    page.goto(confirmation_link)

    confirmation_page = ConfirmationPage(page)
    confirmation_page.confirm_button.click()

    user = UserProfile.objects.get(email="test@example.com")
    email_address = EmailAddress.objects.get(user=user, email="test@example.com")
    assert email_address.verified
