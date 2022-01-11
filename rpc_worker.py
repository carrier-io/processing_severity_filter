from pylon.core.tools import log  # pylint: disable=E0611,E0401


def make_dusty_config(context, test_params, scanner_params):
    """ Prepare dusty config for this scanner """
    #
    log.info("Test params: %s", test_params)
    log.info("Scanner params: %s", scanner_params)
    #
    integration = context.rpc_manager.call.integrations_get_by_id(scanner_params['id'])

    result = integration.settings
    #
    log.info("Result: %s", result)
    #
    return result


def security_test_create_integration_validate(data: str, **kwargs) -> str:
    if data.lower() in {'info', 'critical', 'high', 'medium', 'low'}:
        return data
    raise ValueError(f'{data.lower()} if not in the available range')
