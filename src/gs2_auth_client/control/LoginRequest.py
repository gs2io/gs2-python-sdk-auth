# encoding: utf-8
#
# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

from gs2_core_client.Gs2BasicRequest import Gs2BasicRequest
from gs2_auth_client.Gs2Auth import Gs2Auth


class LoginRequest(Gs2BasicRequest):

    class Constant(Gs2Auth):
        FUNCTION = "Login"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(LoginRequest, self).__init__(params)
        if params is None:
            self.__service_id = None
        else:
            self.set_service_id(params['serviceId'] if 'serviceId' in params.keys() else None)
        if params is None:
            self.__user_id = None
        else:
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)

    def get_service_id(self):
        """
        ログインするサービスIDを取得
        :return: ログインするサービスID
        :rtype: unicode
        """
        return self.__service_id

    def set_service_id(self, service_id):
        """
        ログインするサービスIDを設定
        :param service_id: ログインするサービスID
        :type service_id: unicode
        """
        if service_id and not (isinstance(service_id, str) or isinstance(service_id, unicode)):
            raise TypeError(type(service_id))
        self.__service_id = service_id

    def with_service_id(self, service_id):
        """
        ログインするサービスIDを設定
        :param service_id: ログインするサービスID
        :type service_id: unicode
        :return: this
        :rtype: LoginRequest
        """
        self.set_service_id(service_id)
        return self

    def get_user_id(self):
        """
        ログインするユーザのIDを取得
        :return: ログインするユーザのID
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        ログインするユーザのIDを設定
        :param user_id: ログインするユーザのID
        :type user_id: unicode
        """
        if user_id and not (isinstance(user_id, str) or isinstance(user_id, unicode)):
            raise TypeError(type(user_id))
        self.__user_id = user_id

    def with_user_id(self, user_id):
        """
        ログインするユーザのIDを設定
        :param user_id: ログインするユーザのID
        :type user_id: unicode
        :return: this
        :rtype: LoginRequest
        """
        self.set_user_id(user_id)
        return self
