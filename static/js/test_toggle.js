window['processing_processing_severity_filter'] = {
    get_data: () => {
        if ($('#integration_checkbox_processing_severity_filter').prop('checked')) {
            return $('#processing_severity_filter .selectpicker').val()
        }
    },
    set_data: data => {
        $('#processing_severity_filter .selectpicker').val(data || 'Info').selectpicker('refresh')
        $('#integration_checkbox_processing_severity_filter').prop('checked', true)
        $('#selector_processing_severity_filter').collapse('show')
    },
    clear_data: () => {
        $('#processing_severity_filter .selectpicker').val('Info').selectpicker('refresh')
        $('#integration_checkbox_processing_severity_filter').prop('checked', false)
        $('#selector_processing_severity_filter').collapse('hide')
    }
}
