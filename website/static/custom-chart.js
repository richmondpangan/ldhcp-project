// Bar Chart for transaction by payment processor
const dataForMedicineSalesPurchases = {
    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    datasets: [
        {
            label: 'Purchase',
            data:[173, 395, 90, 233, 376, 340, 135, 185, 111, 275, 227, 326],
            backgroundColor: [
                'rgb(37, 135, 232)'
            ]
        },
        {
            label: 'Sales',
            data:[26, 113, 246, 127, 10, 385, 95, 151, 105, 290, 184, 7],
            backgroundColor: [
                'rgb(23, 209, 132)'
            ]
        }
    ]           
};

const configForMedicineSalesPurchases = {
    type: 'bar',
    data: dataForMedicineSalesPurchases,
    options: {
        maintainAspectRatio: false,
        categoryPercentage: 0.6,
        barPercentage: 0.9,
        plugins: {
            legend: {
                display: true
            }
        },
        scales: {
            x: {
                grid: {
                    drawOnChartArea: false
                }
            },
            y: {
                grid: {
                    drawOnChartArea: false
                }
            }
        }
    }
};

const medicineSalesPurchases = new Chart(
    document.getElementById('medicines-chart'),
    config = configForMedicineSalesPurchases
);