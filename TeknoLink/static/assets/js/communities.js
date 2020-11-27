$(document).ready(function() {
    var table= $('#community-table').DataTable({
        dom: 'lBfrtip',
        buttons: true,
        buttons: [
            'pdf'
        ]
    });
    $("#searchTxb").keyup(function(){
        table.search($("#searchTxb").val().toString());
        table.draw();
    });
    $(".understand-checkbox").change(function(){
        if(this.checked){
            $(this).parent().parent().find("#btnDelete").removeAttr("disabled");
        }
        else{
            $(this).parent().parent().find("#btnDelete").attr('disabled','disabled');
        }
    });
    $("#exportBtn").on("click",function(){
        $(".buttons-pdf").trigger("click");
    });
    $.fn.dataTable.ext.search.push(
        function(settings, data, dataIndex) {
            var min = $('#fromDate').val() == "" ? null : new Date($('#fromDate').val());
            var max = $('#toDate').val() == "" ? null : new Date($('#toDate').val());
            var startDate = new Date(data[0]);
            if (min == null && max == null) { return true; }
            if (min == null && startDate <= max) { return true; }
            if (max == null && startDate >= min) { return true; }
            if (startDate <= max && startDate >= min) { return true; }
            return false;
        }
    );
    $('#fromDate, #toDate').change(function() {
        table.draw();
    });
} );
$(function () {

    $('.datepicker').datepicker({
        clearBtn: true,
        format: "mm-dd-yyyy"
    });

});