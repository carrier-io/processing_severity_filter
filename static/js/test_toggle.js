window['processing_processing_severity_filter'] = {
    $el: () => $('#selector_processing_severity_filter').closest('div.card').find('div.card-header input[type=checkbox]'),
    $select: () => $('#selector_processing_severity_filter .selectpicker'),
    get_data: () => {
        if (processing_processing_severity_filter.$el().prop('checked')) {
            return processing_processing_severity_filter.$select().val()
        }
    },
    set_data: data => {
        processing_processing_severity_filter.$select().val(data || 'info').selectpicker('refresh')
        processing_processing_severity_filter.$el().prop('checked', true)
        $('#selector_processing_severity_filter').collapse('show')
    },
    clear_data: () => {
        processing_processing_severity_filter.$select().val('info').selectpicker('refresh')
        processing_processing_severity_filter.$el().prop('checked', false)
        $('#selector_processing_severity_filter').collapse('hide')
    }
}
