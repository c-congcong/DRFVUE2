from rest_framework import serializers,exceptions

from user.models import User, Employee


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "real_name", "password", "gender","register_time")
        extra_kwargs = {
            "username": {
                "required": True,
                "min_length": 2,
                "error_messages": {
                    "required": "用户名是必填的",
                    "min_length": "用户名长度太短"
                }
            },
            "real_name": {
                "required": True,
                "min_length": 2,
                "error_messages": {
                    "required": "真实姓名是必填的",
                    "min_length": "真实姓名长度太短，不合法！"
                }
            },
            "register_time": {
                "required": True,
                "error_messages": {
                    "required": "注册时间是必填的",
                }
            },
        }

    # 全局校验钩子
    # def validate(self, attrs):
    #     pwd = attrs.get("password")
    #     re_pwd = attrs.pop("password2")
    #     print(attrs)
    #     if pwd != re_pwd:
    #         raise exceptions.ValidationError("两次密码不一致")
    #
    #     return attrs
    def validate(self, attrs):
        username = attrs.get("username")
        print(username)
        st_obj = User.objects.filter(username=username)
        if st_obj:
            raise serializers.ValidationError("用户名已存在，请换一个！")
        return attrs

    # def validate_username(self, value):
    #     print(value)
    #     st_obj = User.objects.filter(username=value)
    #     if st_obj:
    #         raise serializers.ValidationError("用户名已存在，请换一个！")
    #     return value

# class UserModelSerializer1(serializers.ModelSerializer):
#
#     class Meta:
#         model = User
#         fields = ("__all__")


class EmployeeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("__all__")
        extra_kwargs = {
            "emp_name": {
                "required": True,
                "min_length": 2,
                "error_messages": {
                    "required": "用户名是必填的",
                    "min_length": "用户名长度太短"
                }
            },
            "salary": {
                "required": True,
                "error_messages": {
                    "required": "工资不能为空",
                }
            },
            "age": {
                "required": True,
                "error_messages": {
                    "required": "年龄不能为空",
                }
            }
        }

