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


class AccountToken(object):

    def __init__(self, params=None):
        if params is None:
            self.__owner_id = None
            self.__game_name = None
            self.__user_id = None
            self.__timestamp = None
        else:
            self.set_owner_id(params['ownerId'] if 'ownerId' in params.keys() else None)
            self.set_game_name(params['gameName'] if 'gameName' in params.keys() else None)
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
            self.set_timestamp(params['timestamp'] if 'timestamp' in params.keys() else None)

    def get_owner_id(self):
        """
        オーナーIDを取得
        :return: オーナーID
        :rtype: unicode
        """
        return self.__owner_id

    def set_owner_id(self, owner_id):
        """
        オーナーIDを設定
        :param owner_id: オーナーID
        :type owner_id: unicode
        """
        self.__owner_id = owner_id

    def get_game_name(self):
        """
        GS2-Accountゲーム名を取得
        :return: GS2-Accountゲーム名
        :rtype: unicode
        """
        return self.__game_name

    def set_game_name(self, game_name):
        """
        GS2-Accountゲーム名を設定
        :param game_name: GS2-Accountゲーム名
        :type game_name: unicode
        """
        self.__game_name = game_name

    def get_user_id(self):
        """
        ユーザIDを取得
        :return: ユーザID
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        ユーザIDを設定
        :param user_id: ユーザID
        :type user_id: unicode
        """
        self.__user_id = user_id

    def get_timestamp(self):
        """
        認証日時(エポック秒)を取得
        :return: 認証日時(エポック秒)
        :rtype: int
        """
        return self.__timestamp

    def set_timestamp(self, timestamp):
        """
        認証日時(エポック秒)を設定
        :param timestamp: 認証日時(エポック秒)
        :type timestamp: int
        """
        self.__timestamp = timestamp

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(AccountToken, self).__getitem__(key)

    def to_dict(self):
        return {
            "ownerId": self.__owner_id,
            "gameName": self.__game_name,
            "userId": self.__user_id,
            "timestamp": self.__timestamp,
        }
