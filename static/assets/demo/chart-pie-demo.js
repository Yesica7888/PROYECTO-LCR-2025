// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

console.log("Mi script de graficos se está ejecutando");

// Pie Chart Example
var ctx = document.getElementById("graficoDiagnosticos");
var diagnosticosGraph= JSON.parse(ctx.dataset.diagnosticos);
var totalGraph=JSON.parse(ctx.dataset.total);

var myPieChart = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: diagnosticosGraph,
    datasets: [{
      data: totalGraph,
      backgroundColor: ['#007bff', '#dc3545', '#ffc107', '#28a745'],
    }],
  },
});
