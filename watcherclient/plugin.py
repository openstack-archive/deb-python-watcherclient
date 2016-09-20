#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.


import logging

from osc_lib import utils

LOG = logging.getLogger(__name__)

DEFAULT_API_VERSION = '1'
API_VERSION_OPTION = 'os_infra_optim_api_version'
API_NAME = 'infra-optim'
API_VERSIONS = {
    '1': 'watcherclient.v1.client.Client',
}


def make_client(instance):
    """Returns an infra-optim service client"""
    watcher_client = utils.get_client_class(
        API_NAME,
        instance._api_version[API_NAME],
        API_VERSIONS)
    LOG.debug('Instantiating infra-optim client: %s', watcher_client)

    endpoint = instance.get_endpoint_for_service_type(
        API_NAME,
        region_name=instance._region_name,
        interface=instance._interface,
    )

    auth_url = instance._auth_url \
        if hasattr(instance, '_auth_url') else instance.auth.auth_url
    username = instance._username \
        if hasattr(instance, '_username') else instance.auth._username
    password = instance._password \
        if hasattr(instance, '_password') else instance.auth._password

    client = watcher_client(
        endpoint=endpoint,
        session=instance.session,
        auth_url=auth_url,
        username=username,
        password=password,
        region_name=instance._region_name,
    )

    return client


def build_option_parser(parser):
    """Hook to add global options."""
    parser.add_argument('--os-infra-optim-api-version',
                        metavar='<infra-optim-api-version>',
                        default=utils.env(
                            'OS_INFRA_OPTIM_API_VERSION',
                            default=DEFAULT_API_VERSION),
                        help=('Watcher API version, default=' +
                              DEFAULT_API_VERSION +
                              ' (Env: OS_INFRA_OPTIM_API_VERSION)'))
    return parser
