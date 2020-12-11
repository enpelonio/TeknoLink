function AddContactNumber(element){
    var lastContactDiv=$(element).parent().parent().parent().find('.contact-number-wrapper-create-community');
    var lastContactDiv=$(lastContactDiv).filter(':last');
    
    console.log(lastContactDiv);
    var newContactNumber='<div class="col-sm-0 col-md-6"></div><div class="col-sm-12 col-md-6 mt-3 align-self-end contact-number-wrapper-create-community">'+
    '<div class="form-item d-flex align-content-center inputWrapper">' +
        '<i class="fa fa-phone fa-create-community fa-2x mr-3"></i> <span class="d-flex align-items-center mr-1">+63</span>'+
        '<input class="form-input" type="text" value="" name="community_contact_number" pattern="[0-9]{10}" placeholder="9334123456">'+
        '<button onclick="RemoveContactNumber(this)" class="icon-button ml-2" data-toggle="tooltip" title="Remove Contact Number" type="button" style="font-size: 16px;"><i class="fa fa-times remove-icon fa-create-community" ></i></button>'+
    '</div>'+
'</div>'
    $(newContactNumber).insertAfter(lastContactDiv);
}
function RemoveContactNumber(element){
  $(element).parent().parent().remove();
}
$(document).ready(function() {
      $(".uploadPhotoBtn").on("click",function() {
          console.log("Asdasdasdf");
        $(this).parent().find('.fileInput').click();
      });
      $(".image-background").on("click",function(){
        $(this).parent().parent().parent().find("#view-photo-modal").modal('show');
        console.log($(this).parent().parent().parent().find("#view-photo-modal"));
      });
      $(".fileInput").on("change",function(){readURL(this)});
      function readURL(input){
        if (input.files && input.files[0]) {
          var reader = new FileReader();
          reader.onload = function (e) {
              $(input).parent().find(".image-background")
              .attr('src', e.target.result);
              
              $(input).parent().parent().parent().find("#view-photo-modal").find("#image-content-modal").attr('src', e.target.result);
              $(input).parent().find(".changeFlag").val("T");
          };
          reader.readAsDataURL(input.files[0]);
        }
      }
      $(".community-name-create-community").on("change",function(){
        console.log("changed");
        var eventfirer=$(this);
        var com_initial_name=eventfirer.parent().find("#com_initial_name").val();
        $.ajax({
          url: '/Creator/validate-community-name/',
          data: {
            'community_name': this.value,
            'com_initial_name': com_initial_name
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
});
