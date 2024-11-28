const recordForm = document.getElementById('recordForm');
const recordsDiv = document.getElementById('records');
const searchInput = document.getElementById('search');

let records = JSON.parse(localStorage.getItem('records ')) || [];

recordForm.addEventListener('submit', function (event) {
    event.preventDefault();

    const patientName = document.getElementById('patientName').value;
    const dataHash = document.getElementById('dataHash').value;

    const record = {
        id: records.length + 1,
        name: patientName,
        hash: dataHash
    };

    records.push(record);
    localStorage.setItem('records', JSON.stringify(records));
    displayRecords();
    recordForm.reset();
});

searchInput.addEventListener('input', function () {
    const searchTerm = searchInput.value.toLowerCase();
    const filteredRecords = records.filter(record => 
        record.name.toLowerCase().includes(searchTerm) || 
        record.hash.toLowerCase().includes(searchTerm)
    );
    displayRecords(filteredRecords);
});

function displayRecords(filteredRecords = records) {
    recordsDiv.innerHTML = '';
    filteredRecords.forEach(record => {
        const recordDiv = document.createElement('div');
        recordDiv.className = 'record';
        recordDiv.innerHTML = `
            <strong>${record.name}</strong> - ${record.hash}
            <button class="btn btn-danger btn-sm float-end" onclick="deleteRecord(${record.id})">Delete</button>
        `;
        recordsDiv.appendChild(recordDiv);
    });
}

function deleteRecord(id) {
    records = records.filter(record => record.id !== id);
    localStorage.setItem('records', JSON.stringify(records));
    displayRecords();
}

// Initial load of records
displayRecords();