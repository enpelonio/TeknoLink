function AddContactNumber(element){
    var currentDiv=$(element).parent().parent();
    var newContactNumber='<div class="col-sm-0 col-md-6"></div><div class="col-sm-12 col-md-6 mt-3 align-self-end">'+
    '<p class="labels">Contacts</p>'+
    '<div class="form-item d-flex align-content-center inputWrapper">' +
        '<i class="fa fa-phone fa-2x mr-3"></i> <span class="d-flex align-items-center mr-1">+63</span>'+
        '<input class="form-input" type="text" value="" name="contact_number" pattern="[0-9]{10}" placeholder="9334123456">'+
        '<button onclick="AddContactNumber(this)" class="icon-button ml-2" data-toggle="tooltip" title="Add Contact Number" type="button"><i class="fa fa-plus fa-create-community" ></i></button>'+
        '<button onclick="RemoveContactNumber(this)" class="icon-button ml-2" data-toggle="tooltip" title="Remove Contact Number" type="button"><i class="fa fa-times remove-icon fa-create-community" ></i></button>'+
    '</div>'+
'</div>'
    $(newContactNumber).insertAfter(currentDiv);
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
        console.log("sdasdasadfg");
      });
      $(".fileInput").on("change",function(){readURL(this)});
      function readURL(input){
        if (input.files && input.files[0]) {
          var reader = new FileReader();
          reader.onload = function (e) {
              $(input).parent().find(".image-background")
              .attr('src', e.target.result);
              
              $(input).parent().parent().parent().find("#view-photo-modal").find("#image-content-modal").attr('src', e.target.result);
                //$(input).parent().find(".changeFlag").val("T");
          };
          reader.readAsDataURL(input.files[0]);
        }
      }
      $('body').removeClass('modal-open');
});
