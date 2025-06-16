// Espera o DOM carregar antes de executar
document.addEventListener("DOMContentLoaded", function () {
    const ctx = document.getElementById('cpuChart').getContext('2d');

    // Dados iniciais
    const labels = [];
    const data = {
        labels: labels,
        datasets: [{
            label: 'Uso da CPU (%)',
            data: [],
            borderColor: 'rgb(75, 192, 192)',
            tension: 0.1
        }]
    };

    // Configuração do gráfico
    const config = {
        type: 'line',
        data: data,
        options: {
            animation: false,
            responsive: true,
            scales: {
                y: {
                    min: 0,
                    max: 100,
                    title: {
                        display: true,
                        text: 'CPU (%)'
                    }
                }
            }
        }
    };

    const cpuChart = new Chart(ctx, config);

    // Função para buscar os dados da CPU da API
    function fetchCpuData() {
        fetch('/api/system-status-cpu/')
            .then(response => response.json())
            .then(cpu => {
                const now = new Date();
                const timeLabel = now.toLocaleTimeString();

                // Mantém só os últimos 20 pontos
                if (labels.length >= 20) {
                    labels.shift();
                    cpuChart.data.datasets[0].data.shift();
                }

                labels.push(timeLabel);
                cpuChart.data.datasets[0].data.push(cpu.cpu);  // Assumindo que a API retorna {"cpu": 38.0}
                cpuChart.update();
            })
            .catch(error => console.error('Erro ao buscar dados da CPU:', error));
    }

    // Chama a cada 2 segundos
    setInterval(fetchCpuData, 2000);
});
