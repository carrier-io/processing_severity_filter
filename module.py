#!/usr/bin/python3
# coding=utf-8

#   Copyright 2021 getcarrier.io
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

""" Module """
from functools import partial
from pylon.core.tools import log  # pylint: disable=E0611,E0401
from pylon.core.tools import module  # pylint: disable=E0611,E0401

from .components import render_test_toggle
from .rpc_worker import make_dusty_config


class Module(module.ModuleModel):
    """ Task module """

    def __init__(self, context, descriptor):
        self.context = context
        self.descriptor = descriptor

    def init(self):
        """ Init module """
        log.info(f"Initializing module {self.descriptor.name}")
        SECTION_NAME = 'processing'

        self.descriptor.init_blueprint()

        # Register template slot callback
        # self.context.slot_manager.register_callback(f"integration_card_{NAME}", render_integration_card)
        self.context.slot_manager.register_callback(f"security_{SECTION_NAME}", render_test_toggle)

        self.context.rpc_manager.call.integrations_register_section(
            name=SECTION_NAME,
            integration_description='Manage processing',
            test_planner_description='Specify processing tools. You may also set processors in <a '
                                     'href="/?chapter=Configuration&module=Integrations&page=all">Integrations</a> '
        )

        self.context.rpc_manager.call.integrations_register(
            name=self.descriptor.name,
            section=SECTION_NAME,
        )

        self.context.rpc_manager.register_function(
            partial(make_dusty_config, self.context),
            name=f'dusty_config_{self.descriptor.name}',
        )


    def deinit(self):  # pylint: disable=R0201
        """ De-init module """
        log.info("De-initializing severity_filter")
