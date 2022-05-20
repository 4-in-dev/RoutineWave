from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        # 기본 저장 필드: first_name, last_name, username, email

        user = super().save_user(request, user, form, False)
        # 추가 저장 필드: profile_image, nick_name

        nick_name = data.get("nick_name")
        if nick_name:
            user.nick_name = nick_name

        profile_image = data.get("profile_image")
        if profile_image:
            user.profile_image = profile_image

        user.save()
        return user