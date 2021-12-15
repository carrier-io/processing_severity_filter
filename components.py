from flask import render_template


def render_test_toggle(context, slot, payload):
    integrations = context.rpc_manager.call.integrations_get_project_integrations_by_name(
        payload['id'],
        'processing_severity_filter'
    )
    payload['project_integrations'] = integrations
    return render_template(
        'processing_severity_filter:processing_severity_filter_test_toggle.html',
        config=payload
    )
