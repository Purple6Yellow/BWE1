// import dayGridMonth from '\pakket\node_modules\@fullcalendar\daygrid'; 
// initialView: 'dayGridMonth',
document.addEventListener('DOMContentLoaded', function() {

    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
      
      headerToolbar: {
        right: 'prev, next today',
        center: 'title',
        right: 'dayGridMonth,timeGridWeek,timeGridDay'},
    
      views: {dayGridMonth: {
        titleFormat: {month: 'long', year:'numeric'},
      }},

    });
    calendar.render();
    calendar.setOption('height', 560);
  });


