$(document).ready(function() {

    var milestonesTable=$("#milestone-table").DataTable();
    $('#select-type-activities').on("change",function(){
        milestonesTable
        .columns( 2 )
        .search( this.value );
        milestonesTable.draw();
    });
    $(".college-name-input").on("change",function(){
        var eventfirer=$(this);
        var college_initial_name=eventfirer.parent().find("#college_initial_name").val();
        $.ajax({
          url: '/Creator/validate-college-name/',
          data: {
            'college_name': this.value,
            'college_initial_name': college_initial_name
          },
          success: function (data) {
            var nearestResponse=eventfirer.parent().parent().parent().find('.name-response-create-community');
            var nearestUpdateBtn=eventfirer.parent().parent().parent().find('.update-button-create-community');
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
      $(".department-name-input").on("change",function(){
        var eventfirer=$(this);
        var department_initial_name=eventfirer.parent().find("#department_initial_name").val();
        $.ajax({
          url: '/Creator/validate-department-name/',
          data: {
            'department_name': this.value,
            'department_initial_name': department_initial_name
          },
          success: function (data) {
            var nearestResponse=eventfirer.parent().parent().parent().find('.name-response-create-community');
            var nearestUpdateBtn=eventfirer.parent().parent().parent().find('.update-button-create-community');
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
} );