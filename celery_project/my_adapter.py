from django.contrib.auth.models import User
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class MyAdapter(DefaultSocialAccountAdapter):
    """
    This adapter helps in case a user trying social login with email is already exists.
    We takes that user and connect with the social account.
    """

    def pre_social_login(self, request, sociallogin):
        if request.user.is_authenticated:
            return

        # Get the email address of the social account
        email = sociallogin.account.extra_data.get("email")

        # Check if a user with this email address already exists
        try:
            user = User.objects.get(email=email)

            # If the user exists, link the social account with this user
            sociallogin.connect(request, user)
            sociallogin.save(request, user)
        except User.DoesNotExist:
            pass  # User doesn't exist, so proceed with the default flow
