function getPrediction() {
    var form = document.getElementById('predict-form');
    var formData = new FormData(form);

    fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        body: JSON.stringify(Object.fromEntries(formData)),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = 'Prediction: ' + data.prediction;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
