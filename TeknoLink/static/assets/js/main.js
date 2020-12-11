(function($) {
    "use strict";
    var fullHeight = function() {
        $('.js-fullheight').css('height', $(window).height());
        $(window).resize(function() {
            $('.js-fullheight').css('height', $(window).height());
        });
    };
    fullHeight();
    $('#sidebarCollapse').on('click', function() {
        $('#sidebar').toggleClass('active');
    });

})(jQuery);
var activity = [];
var activityCount = 0;
var code;

function onStepCreation() {
    console.log("im here after creation");
    $('#add-event-step').modal('hide');
    activity[activityCount] = document.getElementById("event_name").value;
    console.log(activityCount);
    code = '<div class="input-field mb-1 col-xl-11 col-md-11 col-sm-12"><input type="text" class="stepping-stone mt-2" value="' + activity[activityCount] + '"><button type="button" class="icon-button-v2" href="#" id=' + count + ' onclick="remove_step(this.id)"><i class="fa fa-times fa-remove-icon" aria-hidden="true "></i></button> </div>'
    document.getElementById("stepsContainer").innerHTML += code;
    activityCount += 1;
    console.log('onstepCreation-event' + activity[activityCount]);
}

function onStepCreation2() {
    console.log("im here after creation 2");
    $('#add-announ-step').modal('hide');
    activity[activityCount] = document.getElementById("announ_name").value;
    console.log(activityCount);
    code = '<div class="input-field mb-1 col-xl-11 col-md-11 col-sm-12"><input type="text" class="stepping-stone mt-2" value="' + activity[activityCount] + '"><button type="button" class="icon-button-v2" href="#" id=' + count + ' onclick="remove_step(this.id)"><i class="fa fa-times fa-remove-icon" aria-hidden="true "></i></button> </div>'
    document.getElementById("stepsContainer").innerHTML += code;
    activityCount += 1;
    console.log('onstepCreation-announ' + activity[activityCount]);

}

var dict = {};
var list = [];
var count = 0;
var table = '<table><tr></tr>';

function add_community() {
    var currentCollege = document.getElementById("college").value;
    var currentDepartment = document.getElementById("department").value;
    if (currentCollege != "none" && currentDepartment != "none") {
        list[0] = currentCollege;
        list[1] = currentDepartment;
        dict[count] = list;
        table += '<tr><td>' + list[0] + '</td><td>' + list[1] + '</td><td><button type="button" class="icon-button-v2" href="#" id=' + count + ' onclick="remove_community(this.id)"><i class="fa fa-times fa-remove-icon" aria-hidden="true "></i></button></td></tr>';
        list = [];
        count += 1;
        document.getElementById("community_table").innerHTML = table + '</tabel>';
        document.getElementById('college').value = "none";
        document.getElementById('department').value = "none";
    }

}

function remove_community(id) {
    table = '<table><tr></tr>';
    console.log('in removing');
    delete dict[id];
    console.log("len of dict=" + Object.keys(dict).length);
    if (Object.keys(dict).length == 0) {
        document.getElementById("community_table").innerHTML = "";
    } else {
        for (var d in dict) {
            table += '<tr><td>' + dict[d][0] + '</td><td>' + dict[d][1] + '</td><td><button type="button" class="icon-button-v2" href="#" id=' + d + ' onclick="remove_community(this.id)"><i class="fa fa-times fa-remove-icon" aria-hidden="true "></i></button></td></tr>';
        }
        document.getElementById("community_table").innerHTML = table + '</tabel>';
    }

}

var dict_task = {};
var list_task = [];
var count_task = 0;
var table_task = '<table><tr></tr>';

function add_community_task() {
    var currentCollege = document.getElementById("college_task").value;
    var currentDepartment = document.getElementById("department_task").value;
    if (currentCollege != "none" && currentDepartment != "none") {
        list_task[0] = currentCollege;
        list_task[1] = currentDepartment;
        dict_task[count_task] = list_task;
        table_task += '<tr><td>' + list_task[0] + '</td><td>' + list_task[1] + '</td><td><button type="button" class="icon-button-v2" href="#" id=' + count_task + ' onclick="remove_community_task(this.id)"><i class="fa fa-times fa-remove-icon" aria-hidden="true "></i></button></td></tr>';
        list_task = [];
        count_task += 1;
        document.getElementById("community_table_task").innerHTML = table_task + '</table>';
        document.getElementById('college_task').value = "none";
        document.getElementById('department_task').value = "none";
    }

}

function remove_community_task(id) {
    table_task = '<table><tr></tr>';
    console.log('in removing');
    delete dict_task[id];
    console.log("len of dict=" + Object.keys(dict_task).length);
    if (Object.keys(dict_task).length == 0) {
        document.getElementById("community_table_task").innerHTML = "";
    } else {
        for (var d in dict_task) {
            table_task += '<tr><td>' + dict_task[d][0] + '</td><td>' + dict_task[d][1] + '</td><td><button type="button" class="icon-button-v2" href="#" id=' + d + ' onclick="remove_community_task(this.id)"><i class="fa fa-times fa-remove-icon" aria-hidden="true "></i></button></td></tr>';
        }
        document.getElementById("community_table_task").innerHTML = table_task + '</table>';
    }

}
var dict_announ = {};
var list_announ = [];
var count_announ = 0;
var table_announ = '<table><tr></tr>';

function add_community_announ() {
    var currentCollege = document.getElementById("college_announ").value;
    var currentDepartment = document.getElementById("department_announ").value;
    if (currentCollege != "none" && currentDepartment != "none") {
        list_announ[0] = currentCollege;
        list_announ[1] = currentDepartment;
        dict_announ[count_announ] = list_announ;
        table_announ += '<tr><td>' + list_announ[0] + '</td><td>' + list_announ[1] + '</td><td><button type="button" class="icon-button-v2" href="#" id=' + count_announ + ' onclick="remove_community_announ(this.id)"><i class="fa fa-times fa-remove-icon" aria-hidden="true "></i></button></td></tr>';
        list_announ = [];
        count_announ += 1;
        document.getElementById("community_table_announ").innerHTML = table_announ + '</table>';
        document.getElementById('college_announ').value = "none";
        document.getElementById('department_announ').value = "none";
    }

}

function remove_community_announ(id) {
    table_announ = '<table><tr></tr>';
    console.log('in removing');
    delete dict_announ[id];
    console.log("len of dict=" + Object.keys(dict_announ).length);
    if (Object.keys(dict_announ).length == 0) {
        document.getElementById("community_table_announ").innerHTML = "";
    } else {
        for (var d in dict_announ) {
            table_announ += '<tr><td>' + dict_announ[d][0] + '</td><td>' + dict_announ[d][1] + '</td><td><button type="button" class="icon-button-v2" href="#" id=' + d + ' onclick="remove_community_announ(this.id)"><i class="fa fa-times fa-remove-icon" aria-hidden="true "></i></button></td></tr>';
        }
        document.getElementById("community_table_announ").innerHTML = table_announ + '</table>';
    }

}

var dict2 = {};
var list2 = [];
var count2 = 0;
var table2 = '<table><tr></tr>';

function add_skill() {
    console.log('adding skill');
    var currentSkill = document.getElementById("skill").value;
    var currentPoint = document.getElementById("points").value;
    if (currentSkill != "none") {
        list2[0] = currentSkill;
        list2[1] = currentPoint;
        dict2[count2] = list2;
        table2 += '<tr><td>' + list2[0] + '</td><td>' + list2[1] + '</td><td><button type="button" class="icon-button-v2" href="#" id=' + count2 + ' onclick="remove_skill(this.id)"><i class="fa fa-times fa-remove-icon" aria-hidden="true "></i></button></td></tr>';
        list2 = [];
        count2 += 1;
        document.getElementById("skill_table").innerHTML = table2 + '</tabel>';
        document.getElementById('skill').value = "none";
        document.getElementById('points').value = 0;
    }

}

function remove_skill(id) {
    table2 = '<table><tr></tr>';
    console.log('in removing');
    delete dict2[id];
    console.log("len of dict=" + Object.keys(dict2).length);
    if (Object.keys(dict2).length == 0) {
        document.getElementById("skill_table").innerHTML = "";
    } else {
        for (var d in dict2) {
            table2 += '<tr><td>' + dict2[d][0] + '</td><td>' + dict2[d][1] + '</td><td><button type="button" class="icon-button-v2" href="#" id=' + d + ' onclick="remove_skill(this.id)"><i class="fa fa-times fa-remove-icon" aria-hidden="true "></i></button></td></tr>';
        }
        document.getElementById("skill_table").innerHTML = table2 + '</tabel>';
    }

}

var dict3 = {};
var list3 = [];
var count3 = 0;
var table3 = '<table><tr></tr>';

function add_day() {
    console.log('adding day');
    var currentDayTimeFrom = document.getElementById("day_time_from").value;
    var currentDayTimeTo = document.getElementById("day_time_to").value;
    var currentDay = document.getElementById("day").value;
    console.log(' day ' + currentDay + ' from ' + currentDayTimeFrom + ' to ' + currentDayTimeTo);
    if (currentDayTimeFrom != "" && currentDayTimeTo != "") {
        list3[0] = currentDay;
        list3[1] = currentDayTimeFrom;
        list3[2] = currentDayTimeTo;
        dict3[count3] = list3;
        table3 += '<tr><td>' + list3[0] + '</td><td>' + list3[1] + '</td><td>' + list3[2] + '</td><td><button type="button" class="icon-button-v2" href="#" id=' + count3 + ' onclick="remove_day(this.id)"><i class="fa fa-times fa-remove-icon" aria-hidden="true "></i></button></td></tr>';
        list3 = [];
        count3 += 1;
        document.getElementById("day_table").innerHTML = table3 + '</table>';
        document.getElementById('day_time_from').value = "";
        document.getElementById('day_time_to').value = "";
        document.getElementById('day').value = "Sunday";
    }
}

function remove_day(id) {
    table3 = '<table><tr></tr>';
    console.log('in removing');
    delete dict3[id];
    console.log("len of dict=" + Object.keys(dict3).length);
    if (Object.keys(dict3).length == 0) {
        document.getElementById("day_table").innerHTML = "";
    } else {
        for (var d in dict3) {
            table3 += '<tr><td>' + dict3[d][0] + '</td><td>' + dict3[d][1] + '</td><td>' + dict3[d][2] + '</td><td><button type="button" class="icon-button-v2" href="#" id=' + d + ' onclick="remove_day(this.id)"><i class="fa fa-times fa-remove-icon" aria-hidden="true "></i></button></td></tr>';
        }
        document.getElementById("day_table").innerHTML = table3 + '</tabel>';
    }
}

function addEventStep() {
    console.log("Im here");
    $('#add-event-step').modal('show');
    $('#add-step-activity').modal('hide');
}

function addAnnounStep() {
    console.log("Im here");
    $('#add-announ-step').modal('show');
    $('#add-step-activity').modal('hide');
}

$(document).ready(function() {
    $('#anotherCom').click(function(event) {
        var element = document.getElementById("forCommunityAdd");
        if (this.checked) {
            element.classList.remove("notExtendCom");
        } else {
            element.classList.add("notExtendCom");
        }
    });
    $('#anotherCom-task').click(function(event) {
        var element = document.getElementById("forCommunityAdd-task");
        if (this.checked) {
            element.classList.remove("notExtendCom");
        } else {
            element.classList.add("notExtendCom");
        }
    });
    $('#anotherCom-announ').click(function(event) {
        var element = document.getElementById("forCommunityAdd-announ");
        if (this.checked) {
            element.classList.remove("notExtendCom");
        } else {
            element.classList.add("notExtendCom");
        }
    });
    $('#uploadPic').click(function(event) {
        document.getElementById("fileInput").click();
    });
    $("#fileInput").on("change", function() { readURL(this) });

    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function(e) {
                var result = e.target.result;
                document.getElementById("media-holder").style.backgroundImage = 'url(' + result + ')';
                $(input).parent().parent().parent().parent().parent().parent().find("#view-photo-modal").find("#image-content-modal").attr('src', e.target.result);
            };
            reader.readAsDataURL(input.files[0]);
        }
    }
    $('#uploadPic-announ').click(function(event) {
        document.getElementById("fileInput-announ").click();
    });
    $("#fileInput-announ").on("change", function() { readURLAnnoun(this) });

    function readURLAnnoun(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function(e) {
                var result = e.target.result;
                document.getElementById("media-holder-announ").style.backgroundImage = 'url(' + result + ')';
                $(input).parent().parent().parent().parent().parent().parent().find("#view-photo-modal-announ").find("#image-content-modal-announ").attr('src', e.target.result);
            };
            reader.readAsDataURL(input.files[0]);
        }
    }

    $('#uploadPic-task').click(function(event) {
        document.getElementById("fileInput-task").click();
    });
    $("#fileInput-task").on("change", function() { readURLTask(this) });

    function readURLTask(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function(e) {
                var result = e.target.result;
                document.getElementById("media-holder-task").style.backgroundImage = 'url(' + result + ')';
                $(input).parent().parent().parent().parent().parent().parent().find("#view-photo-modal-task").find("#image-content-modal-task").attr('src', e.target.result);
            };
            reader.readAsDataURL(input.files[0]);
        }
    }
    $('#eventType').click(function(event) {
        console.log(this.value);
        if (this.value == "Specific") {
            document.getElementById("specific-Event").style.display = "inline";
            document.getElementById("daily-Event").style.display = "none";
            document.getElementById("weekly-Event").style.display = "none";
        } else if (this.value == "Daily") {
            document.getElementById("daily-Event").style.display = "inline";
            document.getElementById("specific-Event").style.display = "none";
            document.getElementById("weekly-Event").style.display = "none";
        } else if (this.value == "Weekly") {
            document.getElementById("specific-Event").style.display = "none";
            document.getElementById("daily-Event").style.display = "none";
            document.getElementById("weekly-Event").style.display = "inline";
        }

    });
});