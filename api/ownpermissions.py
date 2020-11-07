
# このファイルではpermissonを設定することで、ログインしていない状態から他ユーザの
# 更新、削除ができないようにする
from rest_framework import permissions

class ProfilePermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # ただのPOSTやGETは許容し、delete,update等は拒否する
        if request.method in permissions.SAFE_METHODS:
            return True
        return False
