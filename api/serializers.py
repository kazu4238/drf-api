 # シリアライザーとは、具体的には入力されたパスワードを暗号化してDBへ挿入するといったことを行う

from rest_framework import serializers
from .models import Task
# UserモデルはDjangoのデフォルトのものを利用する
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password')
        # passwordは読み取り専用で必須にする
        extra_kwargs = {'password':{'write_only':True,'required':True}}
    # 入力されたパスワードをハッシュ化してDBへ入れるために、validated_dataを用いる
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        # 同時にTokenを生成してDBに登録する
        Token.objects.create(user=user)
        return user


# Taskモデルに対するシリアライザー
class TaskSerializer(serializers.ModelSerializer):

    # DateTimeFieldを簡単な表記にする
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M",read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M", read_only=True)

    class Meta:
        model = Task
        fields = ('id','title','created_at','update_at')

