# -*- coding: utf-8 -*-
#
# Copyright 2013 IBM Corp
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.

import mock

from watcherclient.common import cliutils
from watcherclient.tests import utils
from watcherclient.v1 import strategy_shell


class StrategyShellTest(utils.BaseTestCase):

    def test_do_strategy_show(self):
        actual = {}
        fake_print_dict = lambda data, *args, **kwargs: actual.update(data)
        with mock.patch.object(cliutils, 'print_dict', fake_print_dict):
            strategy = object()
            strategy_shell._print_strategy_show(strategy)
        exp = ['uuid', 'name', 'display_name', 'goal_uuid']
        act = actual.keys()
        self.assertEqual(sorted(exp), sorted(act))
