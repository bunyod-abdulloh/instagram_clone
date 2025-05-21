from rest_framework import serializers

from users.models import User


class SignUpSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    def __init__(self, *args, **kwargs):
        super(SignUpSerializer, self).__init__(*args, **kwargs)
        self.fields['email_phone_number'] = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = (
            "id",
            "auth_type",
            "auth_status"
        )
        extra_kwargs = {
            "auth_type": {"read_only": False, "required": False},
            "auth_status": {"read_only": False, "required": False}
        }

    # def create(self, validated_data):
    #     user = super(SignUpSerializer, self).create(validated_data)
    #     if user.auth_type == VIA_EMAIL:
    #         print(validated_data)
    #         # code = user.create_verify_code(VIA_EMAIL)
    #         # send_email(user.email, code)
    #     elif user.auth_type == VIA_PHONE:
    #         pass
    #         # code = user.create_verify_code(VIA_PHONE)
    #         # send_email(user.phone_number, code)
    #         # send_phone_code(user.phone_number, code)
    #     user.save()
    #     return user

    @staticmethod
    def auth_validate(data):
        print("salom", data)
        # user_input = str(data.get('email_phone_number')).lower()
        # input_type = check_email_or_phone(user_input)  # email or phone
        # if input_type == "email":
        #     data = {
        #         "email": user_input,
        #         "auth_type": VIA_EMAIL
        #     }
        # elif input_type == "phone":
        #     data = {
        #         "phone_number": user_input,
        #         "auth_type": VIA_PHONE
        #     }
        # else:
        #     data = {
        #         'success': False,
        #         'message': "You must send email or phone number"
        #     }
        #     raise ValidationError(data)
        #
        # return data

    # def validate_email_phone_number(self, value):
    #     value = value.lower()
    #     if value and User.objects.filter(email=value).exists():
    #         data = {
    #             "success": False,
    #             "message": "Bu email allaqachon ma'lumotlar bazasida bor"
    #         }
    #         raise ValidationError(data)
    #     elif value and User.objects.filter(phone_number=value).exists():
    #         data = {
    #             "success": False,
    #             "message": "Bu telefon raqami allaqachon ma'lumotlar bazasida bor"
    #         }
    #         raise ValidationError(data)
    #
    #     return value
    #
    # def to_representation(self, instance):
    #     data = super(SignUpSerializer, self).to_representation(instance)
    #     data.update(instance.token())
    #
    #     return data
