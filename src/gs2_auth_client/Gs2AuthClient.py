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

import json

from gs2_core_client.Gs2Constant import Gs2Constant
from gs2_core_client.AbstractGs2Client import AbstractGs2Client


class Gs2AuthClient(AbstractGs2Client):

    ENDPOINT = "auth"

    def __init__(self, credential, region):
        """
        コンストラクタ
        :param credential: 認証情報
        :type credential: IGs2Credential
        :param region: GS2リージョン
        :type region: str
        """
        super(Gs2AuthClient, self).__init__(credential, region)


    def create_once_onetime_token(self, request):
        """
        実行回数制限付きワンタイムトークンを発行します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_auth_client.control.CreateOnceOnetimeTokenRequest.CreateOnceOnetimeTokenRequest
        :return: 結果
        :rtype: gs2_auth_client.control.CreateOnceOnetimeTokenResult.CreateOnceOnetimeTokenResult
        """
        body = { 
            "scriptName": request.get_script_name(),
        }

        if request.get_grant() is not None:
            body["grant"] = request.get_grant()
        if request.get_args() is not None:
            body["args"] = request.get_args()
        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_auth_client.control.CreateOnceOnetimeTokenRequest import CreateOnceOnetimeTokenRequest

        from gs2_auth_client.control.CreateOnceOnetimeTokenResult import CreateOnceOnetimeTokenResult
        return CreateOnceOnetimeTokenResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/onetime/once/token",
            service=self.ENDPOINT,
            module=CreateOnceOnetimeTokenRequest.Constant.MODULE,
            function=CreateOnceOnetimeTokenRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))




    def create_time_onetime_token(self, request):
        """
        1回のみ実行を許可するワンタイムトークンを発行します<br>
        このトークンはスタミナの回復処理など、有効期間内だからといって何度も実行されたくない処理を1度だけ許可したい場合に発行します。<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_auth_client.control.CreateTimeOnetimeTokenRequest.CreateTimeOnetimeTokenRequest
        :return: 結果
        :rtype: gs2_auth_client.control.CreateTimeOnetimeTokenResult.CreateTimeOnetimeTokenResult
        """
        body = { 
            "scriptName": request.get_script_name(),
        }

        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_auth_client.control.CreateTimeOnetimeTokenRequest import CreateTimeOnetimeTokenRequest

        from gs2_auth_client.control.CreateTimeOnetimeTokenResult import CreateTimeOnetimeTokenResult
        return CreateTimeOnetimeTokenResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/onetime/time/token",
            service=self.ENDPOINT,
            module=CreateTimeOnetimeTokenRequest.Constant.MODULE,
            function=CreateTimeOnetimeTokenRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))




    def login(self, request):
        """
        ログイン処理を実行します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_auth_client.control.LoginRequest.LoginRequest
        :return: 結果
        :rtype: gs2_auth_client.control.LoginResult.LoginResult
        """
        body = { 
            "serviceId": request.get_service_id(),
            "userId": request.get_user_id(),
        }

        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_auth_client.control.LoginRequest import LoginRequest

        from gs2_auth_client.control.LoginResult import LoginResult
        return LoginResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/login",
            service=self.ENDPOINT,
            module=LoginRequest.Constant.MODULE,
            function=LoginRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))




    def login_with_sign(self, request):
        """
        GS2-Accountの認証署名付きログイン処理を実行します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_auth_client.control.LoginWithSignRequest.LoginWithSignRequest
        :return: 結果
        :rtype: gs2_auth_client.control.LoginWithSignResult.LoginWithSignResult
        """
        body = { 
            "serviceId": request.get_service_id(),
            "userId": request.get_user_id(),
            "keyName": request.get_key_name(),
            "sign": request.get_sign(),
        }

        headers = { 
        }
        if request.get_request_id() is not None:
            headers["X-GS2-REQUEST-ID"] = request.get_request_id()
        from gs2_auth_client.control.LoginWithSignRequest import LoginWithSignRequest

        from gs2_auth_client.control.LoginWithSignResult import LoginWithSignResult
        return LoginWithSignResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/login/signed",
            service=self.ENDPOINT,
            module=LoginWithSignRequest.Constant.MODULE,
            function=LoginWithSignRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))


