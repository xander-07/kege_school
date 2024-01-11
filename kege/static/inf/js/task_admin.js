(function($) {
    'use strict';
    $(document).ready(function() {
        var taskType = $('#id_task_type');
        var linkedTask = $('#id_linked_task').closest('.form-row');
        if (taskType.val() !== '20' && taskType.val() !== '21') {
            linkedTask.hide();
        }
        taskType.change(function() {
            if (taskType.val() === '20' || taskType.val() === '21') {
                linkedTask.show();
            } else {
                linkedTask.hide();
            }
        });
    });
})(window.django && django.jQuery || jQuery);