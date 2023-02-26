const form = document.querySelector('form');
const result = document.querySelector('.result');

form.addEventListener('submit', (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        result.innerHTML = 'rating: ${data.rating}, prefer: ${data.prefer}';
    })
    .catch(error => console.error(error));
});
