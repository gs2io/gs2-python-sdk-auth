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


class LoginWithSignRequest(Gs2BasicRequest):

    class Constant(Gs2Auth):
        FUNCTION = "LoginWithSign"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(LoginWithSignRequest, self).__init__(params)
        if params is None:
            self.__service_id = None
            self.__user_id = None
            self.__key_name = None
            self.__sign = None
        else:
            self.set_service_id(params['serviceId'] if 'serviceId' in params.keys() else None)
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
            self.set_key_name(params['keyName'] if 'keyName' in params.keys() else None)
            self.set_sign(params['sign'] if 'sign' in params.keys() else None)

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
        self.__service_id = service_id

    def with_service_id(self, service_id):
        """
        ログインするサービスIDを設定
        :param service_id: ログインするサービスID
        :type service_id: unicode
        :return: this
        :rtype: LoginWithSignRequest
        """
        self.set_service_id(service_id)
        return self

    def get_user_id(self):
        """
        ログインするユーザのIDを指定してくださいを取得
        :return: ログインするユーザのIDを指定してください
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        ログインするユーザのIDを指定してくださいを設定
        :param user_id: ログインするユーザのIDを指定してください
        :type user_id: unicode
        """
        self.__user_id = user_id

    def with_user_id(self, user_id):
        """
        ログインするユーザのIDを指定してくださいを設定
        :param user_id: ログインするユーザのIDを指定してください
        :type user_id: unicode
        :return: this
        :rtype: LoginWithSignRequest
        """
        self.set_user_id(user_id)
        return self

    def get_key_name(self):
        """
        GS2-Accountの認証署名の作成に使用した GS2-Key の暗号鍵名を取得
        :return: GS2-Accountの認証署名の作成に使用した GS2-Key の暗号鍵名
        :rtype: unicode
        """
        return self.__key_name

    def set_key_name(self, key_name):
        """
        GS2-Accountの認証署名の作成に使用した GS2-Key の暗号鍵名を設定
        :param key_name: GS2-Accountの認証署名の作成に使用した GS2-Key の暗号鍵名
        :type key_name: unicode
        """
        self.__key_name = key_name

    def with_key_name(self, key_name):
        """
        GS2-Accountの認証署名の作成に使用した GS2-Key の暗号鍵名を設定
        :param key_name: GS2-Accountの認証署名の作成に使用した GS2-Key の暗号鍵名
        :type key_name: unicode
        :return: this
        :rtype: LoginWithSignRequest
        """
        self.set_key_name(key_name)
        return self

    def get_sign(self):
        """
        GS2-Accountの認証署名を取得
        :return: GS2-Accountの認証署名
        :rtype: unicode
        """
        return self.__sign

    def set_sign(self, sign):
        """
        GS2-Accountの認証署名を設定
        :param sign: GS2-Accountの認証署名
        :type sign: unicode
        """
        self.__sign = sign

    def with_sign(self, sign):
        """
        GS2-Accountの認証署名を設定
        :param sign: GS2-Accountの認証署名
        :type sign: unicode
        :return: this
        :rtype: LoginWithSignRequest
        """
        self.set_sign(sign)
        return self
