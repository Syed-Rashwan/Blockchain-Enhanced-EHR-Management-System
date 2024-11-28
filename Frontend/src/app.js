document.getElementById('recordForm').addEventListener('submit', async function(event) {
  event.preventDefault();
  
  const patientName = document.getElementById('patientName').value;
  const dataHash = document.getElementById('dataHash').value;

  const response = await fetch('/add_record', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ patientName, dataHash })
  });

  if (response.ok) {
      alert('Record added successfully!');
      fetchRecords();
  } else {
      alert('Error adding record.');
  }
});

async function fetchRecords() {
  const response = await fetch('/get_records');
  const records = await response.json();
  const recordsDiv = document.getElementById('records');
  recordsDiv.innerHTML = '';

  records.forEach(record => {
      const recordElement = document.createElement('div');
      recordElement.textContent = `Patient: ${record[0]}, Data Hash: ${record[1]}, Timestamp: ${new Date(record[2] * 1000).toLocaleString()}`;
      recordsDiv.appendChild(recordElement);
  });
}

// Fetch records on page load
fetchRecords();
