from flask import render_template


def render_integration_create_modal(context, slot, payload):
    return render_template(
        'severity_filter_integration.html',
        config=payload
    )


def render_integration_card(context, slot, payload):
    return render_template(
        'severity_filter_integration_card.html',
        config=payload
    )


def render_reporter_toggle(context, slot, payload):
    integrations = context.rpc_manager.call.integrations_get_project_integrations_by_name(
        payload['id'],
        'processing_severity_filter'
    )
    payload['project_integrations'] = integrations
    return render_template(
        'severity_filter_toggle.html',
        config=payload
    )
