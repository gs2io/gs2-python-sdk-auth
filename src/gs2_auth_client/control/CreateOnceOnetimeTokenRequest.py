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


class CreateOnceOnetimeTokenRequest(Gs2BasicRequest):

    class Constant(Gs2Auth):
        FUNCTION = "CreateOnceOnetimeToken"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(CreateOnceOnetimeTokenRequest, self).__init__(params)
        if params is None:
            self.__script_name = None
        else:
            self.set_script_name(params['scriptName'] if 'scriptName' in params.keys() else None)
        if params is None:
            self.__grant = None
        else:
            self.set_grant(params['grant'] if 'grant' in params.keys() else None)
        if params is None:
            self.__args = None
        else:
            self.set_args(params['args'] if 'args' in params.keys() else None)

    def get_script_name(self):
        """
        認可処理に実行するスクリプトを取得
        :return: 認可処理に実行するスクリプト
        :rtype: unicode
        """
        return self.__script_name

    def set_script_name(self, script_name):
        """
        認可処理に実行するスクリプトを設定
        :param script_name: 認可処理に実行するスクリプト
        :type script_name: unicode
        """
        if not isinstance(script_name, unicode):
            raise TypeError(type(script_name))
        self.__script_name = script_name

    def with_script_name(self, script_name):
        """
        認可処理に実行するスクリプトを設定
        :param script_name: 認可処理に実行するスクリプト
        :type script_name: unicode
        :return: this
        :rtype: CreateOnceOnetimeTokenRequest
        """
        self.set_script_name(script_name)
        return self

    def get_grant(self):
        """
        認可するアクションを取得
        :return: 認可するアクション
        :rtype: unicode
        """
        return self.__grant

    def set_grant(self, grant):
        """
        認可するアクションを設定
        :param grant: 認可するアクション
        :type grant: unicode
        """
        if not isinstance(grant, unicode):
            raise TypeError(type(grant))
        self.__grant = grant

    def with_grant(self, grant):
        """
        認可するアクションを設定
        :param grant: 認可するアクション
        :type grant: unicode
        :return: this
        :rtype: CreateOnceOnetimeTokenRequest
        """
        self.set_grant(grant)
        return self

    def get_args(self):
        """
        grant で指定したアクションに引数として渡すことを許可する内容を取得
        :return: grant で指定したアクションに引数として渡すことを許可する内容
        :rtype: unicode
        """
        return self.__args

    def set_args(self, args):
        """
        grant で指定したアクションに引数として渡すことを許可する内容を設定
        :param args: grant で指定したアクションに引数として渡すことを許可する内容
        :type args: unicode
        """
        if not isinstance(args, unicode):
            raise TypeError(type(args))
        self.__args = args

    def with_args(self, args):
        """
        grant で指定したアクションに引数として渡すことを許可する内容を設定
        :param args: grant で指定したアクションに引数として渡すことを許可する内容
        :type args: unicode
        :return: this
        :rtype: CreateOnceOnetimeTokenRequest
        """
        self.set_args(args)
        return self
