from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.response import APIResponse

from user import serializers
from user.models import User, Employee


class UserAPIView(APIView):

    # 注册逻辑
    def post(self, request, *args, **kwargs):
        request_data = request.data
        print(request_data)
        if isinstance(request_data, dict):
            stu_ser = serializers.UserModelSerializer(data=request_data)
            many = False
        elif isinstance(request_data, list):
            stu_ser = serializers.UserModelSerializer(data=request_data, many=True)
            many = True
        else:
            return Response({
                "status": 200,
                "message": "数据格式有误",
            })
        pwd = request_data.get("password")
        re_pwd = request_data.get("password2")
        if pwd == re_pwd:
            stu_ser = serializers.UserModelSerializer(data=request_data, many=many)
            stu_ser.is_valid(raise_exception=True)
            stu_obj = stu_ser.save()

            return APIResponse(200, True, results=serializers.UserModelSerializer(stu_obj).data)
        return APIResponse(400, False)

    # 登录
    def get(self, request, *args, **kwargs):
        username = request.query_params.get("username")
        password = request.query_params.get("password")

        user_obj = User.objects.filter(username=username, password=password).first()
        print(user_obj)
        user = serializers.UserModelSerializer(user_obj).data

        if user_obj:
            return Response({
                "status": status.HTTP_200_OK,
                "message": "成功",
                "results": user
            })


class Empview(ListModelMixin, CreateModelMixin, GenericAPIView, UpdateModelMixin, DestroyModelMixin):
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeModelSerializer
    lookup_field = 'pk'
    print(123, lookup_field)

    def get(self, request, *args, **kwargs):
        # 获取固定id的员工
        id = kwargs.get("pk")
        print(id)
        if id:
            user = Employee.objects.get(pk=id)
            user_obj = serializers.EmployeeModelSerializer(user).data
            return APIResponse(200, True, results=user_obj)
        user_list = self.list(request, *args, **kwargs)
        return APIResponse(200, True, results=user_list.data)

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        user_list = self.list(request, *args, **kwargs)
        return APIResponse(200, True, results=user_list.data)

    def post(self, request, *args, **kwargs):
        user_obj = self.create(request, *args, **kwargs)
        return APIResponse(200, True, results=user_obj.data)

    def put(self, request, *args, **kwargs):
        emp_obj = self.update(request, *args, **kwargs)
        return APIResponse(200, True, results=emp_obj.data)
