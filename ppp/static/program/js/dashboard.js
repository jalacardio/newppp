// chart colors
var colors = ['#277647','#ffc600','#dedede','#c3e6cb','#dc3545','#6c757d'];

/* 3 donut charts */
//var donutOptions = {
////    cutoutPercentage: 85,
////    legend: {position:'bottom', padding:5, labels: {pointStyle:'circle', usePointStyle:true}},
////    rotation: 1 * Math.PI,
////    circumference: 1 * Math.PI,
////    responsive:true,
////    maintainAspectRatio: false
//};

//function loadPieChart(id, chart_labels, chart_data) {
//    var chDonutData2 = {
//    labels: chart_labels,
//    datasets: [
//      {
//        backgroundColor: colors.slice(0,3),
//        borderWidth: 0,
//        data: chart_data
//      }
//    ]
//    };
//    var chDonut2 = document.getElementById(id);
//    if (chDonut2) {
//      new Chart(chDonut2, {
//          type: 'doughnut',
//          data: chDonutData2,
//          options: donutOptions
//      });
//    }
//}

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





