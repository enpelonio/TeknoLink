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
function AddContactNumberStudent(element){
    var currentDiv=$(element).parent().parent();
    var newContactNumber='<div class="col-md-6 mt-2">'+
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
            $(input).parent().find(".changeFlag").val("T");
        };
        reader.readAsDataURL(input.files[0]);
      }
    }

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
    $('#select-type-activities').on("change",function(){
        console.log("viewstudent");
        milestonesTable
        .columns( 2 )
        .search( this.value );
        milestonesTable.draw();
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

    $('#college_belong').on('change',function(){
        var selectedCollege=this.value;
        $.ajax({
            url: '/Creator/get-departments-belonging-to-college/',
            data: {
              'college_name': selectedCollege
            },
            success: function (data) {
              $('#department_belong').empty();
              $.each(data.departments,function(key,val){
                var optionHtml='<option value="'+ key +'">'+val+'</option>';
                $('#department_belong').append(optionHtml);
              });
            },
            failure: function(data) { 
                alert('Got an error dude');
            }
          });
    });
    $('#skill_category').on('change',function(){
        var selectedCategoryId=this.value;
        $.ajax({
            url: '/Creator/get-skills-of-a-category/',
            data: {
              'category_id': selectedCategoryId
            },
            success: function (data) {
              $('#skill_name').empty();
              $.each(data.skills,function(key,val){
                var optionHtml='<option value="'+ key +'">'+val+'</option>';
                $('#skill_name').append(optionHtml);
              });
            },
            failure: function(data) { 
                alert('Got an error dude');
            }
          });
    });
    $('#student_id').on('change',function(){
        var eventfirer=$(this);
        var initial_id=$('#student_initial_id').val()
        console.log(initial_id);
        $.ajax({
            url: '/Creator/validate-student-id/',
            data: {
              'student_id': this.value,
              'student_initial_id': initial_id
            },
            success: function (data) {
              var nearestResponse=eventfirer.parent().parent().find('.id-label');
              var nearestUpdateBtn=$('#update-button-container-view-student');
              console.log(nearestUpdateBtn)
              if(data.exists){
                console.log("exists");
                nearestResponse.find('.invalid-username').removeClass('d-none');
                nearestResponse.find('.valid-username').addClass('d-none');
                nearestUpdateBtn.addClass("update-button-create-community-disabled");
              }
              else{
                console.log("none");
                nearestResponse.find('.invalid-username').addClass('d-none');
                nearestResponse.find('.valid-username').removeClass('d-none');
                nearestUpdateBtn.removeClass("update-button-create-community-disabled");
              }
            },
            failure: function(data) { 
                alert('Got an error dude');
            }
          });
    });
});

$(function () {

    $('.datepicker').datepicker({
        clearBtn: true,
        format: "mm-dd-yyyy"
    });

});