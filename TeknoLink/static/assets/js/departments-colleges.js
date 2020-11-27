$(document).ready(function() {

    var milestonesTable=$("#milestone-table").DataTable();
    $('#select-type-activities').on("change",function(){
        milestonesTable
        .columns( 2 )
        .search( this.value );
        milestonesTable.draw();
    });
} );