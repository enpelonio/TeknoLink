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
    var table=$('#community-table').DataTable();
    $('#select-type-activities-student').on("change",function(){
        var selectedCollege=this.value;
        table
        .columns( 4 )
        .search( selectedCollege );
        table.draw();

        if(selectedCollege=='') selectedCollege=undefined;
        console.log(selectedCollege);
        $.ajax({
            url: '/Creator/get-departments-belonging-to-college/',
            data: {
              'college_name': selectedCollege
            },
            success: function (data) {
              $('#select-status-activities-student').empty();
              $('#select-status-activities-student').append('<option value="">All</option>');
              $.each(data.departments,function(key,val){
                var optionHtml='<option value="'+ val +'">'+val+'</option>';
                $('#select-status-activities-student').append(optionHtml);
              });
            },
            failure: function(data) { 
                alert('Got an error dude');
            }
          });
    });
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
    $('#select-status-activities-student').on("change",function(){
        table
        .columns( 5 )
        .search( this.value );
        table.draw();
    });
} );