$(document).ready(function(){
    jQuery.fn.dataTable.render.ellipsis = function ( cutoff, wordbreak, escapeHtml ) {
        var esc = function ( t ) {
            return t
                .replace( /&/g, '&amp;' )
                .replace( /</g, '&lt;' )
                .replace( />/g, '&gt;' )
                .replace( /"/g, '&quot;' );
        };
     
        return function ( d, type, row ) {
            // Order, search and type get the original data
            if ( type !== 'display' ) {
                return d;
            }
     
            if ( typeof d !== 'number' && typeof d !== 'string' ) {
                return d;
            }
     
            d = d.toString(); // cast numbers
     
            if ( d.length <= cutoff ) {
                return d;
            }
     
            var shortened = d.substr(0, cutoff-1);
     
            // Find the last white space character in the string
            if ( wordbreak ) {
                shortened = shortened.replace(/\s([^\s]*)$/, '');
            }
     
            // Protect against uncontrolled HTML input
            if ( escapeHtml ) {
                shortened = esc( shortened );
            }
     
            return '<span class="ellipsis" title="'+esc(d)+'">'+shortened+'&#8230;</span>';
        };
    };
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
        ],
        columnDefs: [ {
            targets:2,
            render: $.fn.dataTable.render.ellipsis( 25, true )
        } ]
    });
    var milestonesTable=$('#milestone-table').DataTable({
        dom: 'lBfrtip',
        buttons: true,
        buttons: [
            'pdf'
        ],
        columnDefs: [ {
            targets:2,
            render: $.fn.dataTable.render.ellipsis( 25, true )
        } ]
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


    //autocomplete

    var availableSkills = [
        "ActionScript",
        "AppleScript",
        "Asp",
        "BASIC",
        "C",
        "C++",
        "Clojure",
        "COBOL",
        "ColdFusion",
        "Erlang",
        "Fortran",
        "Groovy",
        "Haskell",
        "Java",
        "JavaScript",
        "Lisp",
        "Perl",
        "PHP",
        "Python",
        "Ruby",
        "Scala",
        "Scheme"
      ];
      var availableJobs=[
          "Job1",
          "Job2",
          "Job3",
          "Job4",
          "Job5",
          "Job6"
      ]
      $(".add-skill-txb").autocomplete({
        source:availableSkills,
        appendTo: $(".add-skill-txb").parent().parent().parent()
      });
      $(".addSkillBtn").click(function(){
            var skill=$(this).parent().find(".add-skill-txb").val();
            if(availableSkills.findIndex(item => skill.toLowerCase() === item.toLowerCase())==-1){
                $("#skill-not-found-modal").modal('show');
            }
            else{
                var tagContainer=$(this).parent().parent().parent().find(".tag-container-job-companies-skill");
                console.log(tagContainer);
                var addedSkill='<div class="tag-item form-item inputWrapper ml-1 mr-1"><span class="mr-2 ml-2">'+
                    skill+'</span><button onclick="RemoveSkillTag(this)" data-toggle="tooltip"'+
                    'title="Remove Skill"><i class="fa fa-times"></i></button></div>';
                tagContainer.append(addedSkill);
                $(this).val("");
            }
      });
      $(".add-job-txb").autocomplete({
        source:availableJobs,
        appendTo: $(".add-job-txb").parent().parent().parent()
      });

      $(".addJobBtn").click(function(){
        var job=$(this).parent().find(".add-job-txb").val();
        if(availableJobs.findIndex(item => job.toLowerCase() === job.toLowerCase())==-1){
            $("#job-not-found-modal").modal('show');
        }
        else{
            var tagContainer=$(this).parent().parent().parent().find(".tag-container-job-companies-job");
            console.log(tagContainer);
            var addedSkill='<div class="tag-item form-item inputWrapper ml-1 mr-1"><span class="mr-2 ml-2">'+
                job+'</span><button onclick="RemoveSkillTag(this)" data-toggle="tooltip"'+
                'title="Remove Skill"><i class="fa fa-times"></i></button></div>';
            tagContainer.append(addedSkill);
            $(this).val("");
        }
  });
});

$(function () {

    $('.datepicker').datepicker({
        clearBtn: true,
        format: "mm-dd-yyyy"
    });

});
function RemoveSkillTag(element){
    $(element).parent().remove();
}
