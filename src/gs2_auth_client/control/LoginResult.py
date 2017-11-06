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

from gs2_auth_client.model import *


class LoginResult(object):

    def __init__(self, response):
        """
        コンストラクタ
        :type response: レスポンスボディ
        :type response: dict
        """
        
        self.__token = unicode(response['token']) if 'token' in response.keys() and response['token'] is not None else None
        
        self.__service_id = unicode(response['serviceId']) if 'serviceId' in response.keys() and response['serviceId'] is not None else None
        
        self.__user_id = unicode(response['userId']) if 'userId' in response.keys() and response['userId'] is not None else None
        
        self.__expire = int(response['expire']) if 'expire' in response.keys() and response['expire'] is not None else None

    def get_token(self):
        """
        アクセストークンを取得
        :return: アクセストークン
        :rtype: unicode
        """
        return self.__token

    def get_service_id(self):
        """
        サービスIDを取得
        :return: サービスID
        :rtype: unicode
        """
        return self.__service_id

    def get_user_id(self):
        """
        ユーザIDを取得
        :return: ユーザID
        :rtype: unicode
        """
        return self.__user_id

    def get_expire(self):
        """
        アクセストークンの有効期限を取得
        :return: アクセストークンの有効期限
        :rtype: int
        """
        return self.__expire
