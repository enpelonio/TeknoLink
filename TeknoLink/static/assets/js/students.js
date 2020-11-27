$(document).ready(function() {
    var table=$('#community-table').DataTable();
    $('#select-type-activities').on("change",function(){
        table
        .columns( 4 )
        .search( this.value );
        table.draw();
    });
    $('#select-status-activities').on("change",function(){
        table
        .columns( 5 )
        .search( this.value );
        table.draw();
    });
} );