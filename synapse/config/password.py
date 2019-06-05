# -*- coding: utf-8 -*-
# Copyright 2015, 2016 OpenMarket Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ._base import Config


class PasswordConfig(Config):
    """Password login configuration
    """

    def read_config(self, config):
        self.enable_password_resets = config.get("enable_password_resets", False)

        password_config = config.get("password_config", {})
        if password_config is None:
            password_config = {}

        self.password_enabled = password_config.get("enabled", True)
        self.password_pepper = password_config.get("pepper", "")

    def default_config(self, config_dir_path, server_name, **kwargs):
        return """\
        # Allow users to reset their password
        #
        # Resetting a user's password is done either by sending a token from
        # Synapse, or asking an identity server to do so. In Synapse v1.0,
        # sending a password reset token from an identity server was turned off
        # by default for security reasons.
        #
        # If enable_password_reset_from_is is False, you must fill out the
        # "email" section of the config before enabling password resets
        #
        #enable_password_resets: False

        password_config:
           # Uncomment to disable password login
           #
           #enabled: false

           # Uncomment and change to a secret random string for extra security.
           # DO NOT CHANGE THIS AFTER INITIAL SETUP!
           #
           #pepper: "EVEN_MORE_SECRET"
        """
