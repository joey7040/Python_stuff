// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable({
    // 'searching':true,  // things you can turn on and off based off a boolean
    // 'paging':true,
    // 'ordering':true,
    // 'info':true,
    // 'ajax':{
    //   'url':'api/endpoint',
    //   'dataSrc':''
    // } //Use this to get data with a ajax call then extract that data with columns below
    // 'columns':[
    //   { 'data': 'Name'},
    //   { 'data': 'Position'},
    //   { 'data': 'Office'},
    //   { 'data': 'Age'},
    //   { 'data': 'Start date'},
    //   { 'data': 'Salary'},
    // ]
    // 'order': [[4, desc]] // orders 3rd column in decresing order so in this case oldest to youngest in the age column
    // 'dom':'Bfrtip',
    // 'buttons': [
    //   'copy', 'csv', 'excel', 'pdf', 'print'
    ]
  });
});
