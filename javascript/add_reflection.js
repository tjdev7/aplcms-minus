console.log('add_reflection');

(function($, jQuery) {
    $(document).ready(function() {
        var url_string = window.location.href;
        var url = new URL(url_string);
        var nid = url.searchParams.get('nid');

        function decodeHtmlEntities(text) {
            // Create a temporary DOM element to leverage the browser's decoder
            var textarea = document.createElement('textarea');
            textarea.innerHTML = text;
            return textarea.textContent;
        }

        if (nid) {
            $('#edit-field-reflection-type').val('Event').trigger('change').prop('disabled', true);

            $.ajax({
                url: '/get-event-details.json?nid=' + nid,
                type: 'GET',
                dataType: 'json',
                success: function(response) {
                    var data = response[0];
                    console.log(data);
                    var decodedTitle = decodeHtmlEntities(data.title);
                    $('#edit-title-0-value').val(decodedTitle).prop('readonly', true);
                    $('#edit-field-event-category-tags-').val(data.event_category).prop('disabled', true);
                    $('#edit-field-branch-location').val(data.field_event_loc).prop('disabled', true);

                    var startDate = new Date(parseInt(data.field_slr_time_start) * 1000);
                    var formattedDate = startDate.toISOString().substring(0, 10);
                    var formattedTime = startDate.toISOString().substring(11, 16);

                    $('#edit-field-reflection-date-and-time-0-value-date').val(formattedDate).prop('readonly', true);
                    $('#edit-field-reflection-date-and-time-0-value-time').val(formattedTime).prop('readonly', true);

                    // Check if CKEditor is defined and if the specific instance exists
                    if (typeof CKEDITOR !== 'undefined' && CKEDITOR.instances['edit-field-reflection-description-0-value']) {
                        // Set the value in CKEditor
                        CKEDITOR.instances['edit-field-reflection-description-0-value'].setData(data.body || data.field_event_summary);
                        
                        // Make the CKEditor instance readonly
                        CKEDITOR.instances['edit-field-reflection-description-0-value'].setReadOnly(true);
                    } else {
                        // Fallback if CKEditor is not initialized yet
                        $('#edit-field-reflection-description-0-value').val(data.body || data.field_event_summary).prop('readonly', true);
                    }
                },
                error: function(xhr, status, error) {
                    console.error("Error fetching event details:", error);
                }
            });
        }
    });
})(jQuery);
