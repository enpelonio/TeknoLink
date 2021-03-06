function AddContactNumberViewStudent(element){
    var currentDiv=$(element).parent().parent();
    var newContactNumber='<div class="col-md-4 mt-2">'+
    '<div class="form-item d-flex inputWrapper">'+
    '<span class="d-flex align-items-center mr-1">+63</span>'+
    '<input class="form-input form-input-view-student" type="text" value="" name="contact_number" pattern="[0-9]{10}" placeholder="9334123456">'+
    '<button onclick="RemoveContactNumber(this)" class="icon-button ml-2" data-toggle="tooltip" title="Remove Contact Number" type="button"><i class="fa fa-times remove-icon fa-view-student" ></i></button>'+
'</div>'+
'</div>';
    $(currentDiv).append(newContactNumber);
}
$(document).ready(function() {
    $("#upload-profile-pic-view-student-btn").on("click",function() {
      $('#fileInput-view-student').click();
    });
    $("#fileInput-view-student").on("change",function(){readURL(this)});
    function readURL(input){
      if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function (e) {
            $("#profile-image-view-student")
            .attr('src', e.target.result);
              //$(input).parent().find(".changeFlag").val("T");
        };
        reader.readAsDataURL(input.files[0]);
      }
    }
    $('body').removeClass('modal-open');

    var skillsTable= $('#skill-table').DataTable({
        dom: 'lBfrtip',
        buttons: true,
        buttons: [
            'pdf'
        ]
    });
    var milestonesTable=$('#milestone-table').DataTable({
        dom: 'lBfrtip',
        buttons: true,
        buttons: [
            'pdf'
        ]
    });
    $("#searchTxb-skill").keyup(function(){
        skillsTable.search($("#searchTxb-skill").val().toString());
        skillsTable.draw();
    });
    $("#searchTxb-milestone").keyup(function(){
        milestonesTable.search($("#searchTxb-milestone").val().toString());
        milestonesTable.draw();
    });
    $(".understand-checkbox").change(function(){
        if(this.checked){
            $(this).parent().parent().find("#btnDelete").removeAttr("disabled");
        }
        else{
            $(this).parent().parent().find("#btnDelete").attr('disabled','disabled');
        }
    });
    $("#exportBtn-skill").on("click",function(){
        $("#skill-table_wrapper .buttons-pdf").trigger("click");
    });
    $("#exportBtn-milestone").on("click",function(){
        $("#milestone-table_wrapper .buttons-pdf").trigger("click");
    });
    $.fn.dataTable.ext.search.push(
        function(settings, data, dataIndex) {
            if(settings.nTable.id=='skill-table'){
                var min = $('#fromDate-skill').val() == "" ? null : new Date($('#fromDate-skill').val());
                var max = $('#toDate-skill').val() == "" ? null : new Date($('#toDate-skill').val());
                var startDate = new Date(data[0]);
                if (min == null && max == null) { return true; }
                if (min == null && startDate <= max) { return true; }
                if (max == null && startDate >= min) { return true; }
                if (startDate <= max && startDate >= min) { return true; }
                return false;
            }
            else{
                var min = $('#fromDate-milestone').val() == "" ? null : new Date($('#fromDate-milestone').val());
                var max = $('#toDate-milestone').val() == "" ? null : new Date($('#toDate-milestone').val());
                var startDate = new Date(data[0]);
                if (min == null && max == null) { return true; }
                if (min == null && startDate <= max) { return true; }
                if (max == null && startDate >= min) { return true; }
                if (startDate <= max && startDate >= min) { return true; }
                return false;
            }
        }
    );
    
    $('#fromDate-skill, #toDate-skill').change(function() {
        skillsTable.draw();
    });
    $('#fromDate-milestone, #toDate-milestone').change(function() {
        milestonesTable.draw();
    });

});

$(function () {

    $('.datepicker').datepicker({
        clearBtn: true,
        format: "mm-dd-yyyy"
    });

});