// chart colors
var colors = ['#277647','#ffc600','#dedede','#c3e6cb','#dc3545','#6c757d'];

function loadPieChart(id, chart_labels, chart_data) {
    var data = {
        labels: chart_labels,
        datasets: [
            {
                data: chart_data,
                backgroundColor: [
                    "#277647",
                    "#ffc600",
                    "#dedede"
                ],
                hoverBackgroundColor: [
                    "#277647",
                    "#ffc600",
                    "#dedede"
                ]
            }]
    };
    var ctx = document.getElementById(id);

    var myDoughnutChart = new Chart(ctx, {
        type: 'doughnut',
        data: data,
        options: {
            rotation: 1 * Math.PI,
            circumference: 1 * Math.PI,
            responsive:true,
            maintainAspectRatio: false
        }
    });
}





