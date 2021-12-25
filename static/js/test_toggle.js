window['processing_processing_severity_filter'] = {
    get_data: () => {
        if ($('#integration_checkbox_processing_severity_filter').prop('checked')) {
            return $('#processing_severity_filter .selectpicker').val()
        }
    },
    set_data: data => {
        $('#processing_severity_filter .selectpicker').val(data || 'Info').selectpicker('refresh')
    },
    clear_data: () => {
        $('#processing_severity_filter .selectpicker').val('Info').selectpicker('refresh')
    }
}
