# from pylon.core.tools import log  # pylint: disable=E0611,E0401
from pylon.core.tools import web

from tools import rpc_tools


class RPC:
    integration_name = 'processing_severity_filter'

    @web.rpc(f'dusty_config_{integration_name}')
    @rpc_tools.wrap_exceptions(RuntimeError)
    def make_dusty_config(self, context, test_params, scanner_params):
        """ Prepare dusty config for this scanner """
        #
        # log.info("Test params: %s", test_params)
        # log.info("Scanner params: %s", scanner_params)
        #
        # integration = context.rpc_manager.call.integrations_get_by_id(scanner_params['id'])
        # result = integration.settings
        #
        result = {"severity": scanner_params.capitalize()}
        #
        # log.info("Result: %s", result)
        #
        return 'min_severity_filter', result



# def security_test_create_integration_validate(data: str, **kwargs) -> str:
#     if data.lower() in {'info', 'critical', 'high', 'medium', 'low'}:
#         return data
#     raise ValueError(f'{data.lower()} if not in the available range')
