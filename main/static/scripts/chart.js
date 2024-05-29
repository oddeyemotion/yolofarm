document.addEventListener("DOMContentLoaded", function () {
  const tempCtx = document.getElementById("tempChart").getContext("2d");
  const fluxCtx = document.getElementById("fluxChart").getContext("2d");
  const tempPredCtx = document.getElementById("tempPredChart").getContext("2d");
  const humidityCtx = document.getElementById("humidityChart").getContext("2d");
  const earthHumidityCtx = document
    .getElementById("earthHumidityChart")
    .getContext("2d");

  const tempChart = new Chart(tempCtx, {
    type: "line",
    data: {
      labels: [],
      datasets: [
        {
          label: "Nhiệt độ",
          data: [],
          borderColor: "rgb(255, 99, 132)",
          backgroundColor: "rgba(255, 99, 132, 0.5)",
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });

  const fluxChart = new Chart(fluxCtx, {
    type: "line",
    data: {
      labels: [],
      datasets: [
        {
          label: "Ánh sáng",
          data: [],
          borderColor: "rgb(54, 162, 235)",
          backgroundColor: "rgba(54, 162, 235, 0.5)",
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });

  const earthHumidityChart = new Chart(earthHumidityCtx, {
    type: "line",
    data: {
      labels: [],
      datasets: [
        {
          label: "Độ Ẩm Đất",
          data: [],
          borderColor: "rgb(255, 205, 86)",
          backgroundColor: "rgba(255, 205, 86, 0.2)",
          tension: 0.1,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });

  const humidityChart = new Chart(humidityCtx, {
    type: "line",
    data: {
      labels: [],
      datasets: [
        {
          label: "Độ Ẩm",
          data: [],
          borderColor: "rgb(75, 192, 192)",
          backgroundColor: "rgba(75, 192, 192, 0.2)",
          tension: 0.1,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });

  const tempPredChart = new Chart(tempPredCtx, {
    type: "line",
    data: {
      labels: [],
      datasets: [
        {
          label: "Predicted Temperature",
          data: [],
          borderColor: "rgb(255, 99, 132)",
          backgroundColor: "rgba(255, 99, 132, 0.5)",
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });

  function fetchDataAndUpdateCharts() {
    fetch("/record_data")
      .then((response) => response.json())
      .then((data) => {
        const { temp, flux, humidAtm, humidEarth, timestamp } = data.data;

        // Update temperature chart
        tempChart.data.labels.push(timestamp);
        tempChart.data.datasets[0].data.push(temp);
        tempChart.update();

        // Update flux chart
        fluxChart.data.labels.push(timestamp);
        fluxChart.data.datasets[0].data.push(flux);
        fluxChart.update();

        // Update humidity chart
        humidityChart.data.labels.push(timestamp);
        humidityChart.data.datasets[0].data.push(humidAtm);
        humidityChart.update();

        // Update earth humidity chart
        earthHumidityChart.data.labels.push(timestamp);
        earthHumidityChart.data.datasets[0].data.push(humidEarth);
        earthHumidityChart.update();
      })
      .catch((error) => console.error("Error fetching data:", error));
  }

  function fetchPredictionAndUpdateChart() {
    const inputData = {
      input: [[3], [5], [5]],
    };

    fetch("/predict_temperature", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(inputData),
    })
      .then((response) => response.json())
      .then((data) => {
        const { temperature, timestamp } = data;
        console.log("Prediction:", temperature);

        // Update predict temperature chart
        tempPredChart.data.labels.push(timestamp);
        tempPredChart.data.datasets[0].data.push(temperature);
        tempPredChart.update();
      })
      .catch((error) => console.error("Error fetching prediction:", error));
  }

  setInterval(fetchDataAndUpdateCharts, 500); // Fetch new data every 2 seconds
  setInterval(fetchPredictionAndUpdateChart, 500); // Fetch new prediction every 2 seconds
});
