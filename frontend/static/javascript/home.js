function navigate(page) {
    alert(`Navigating to ${page} page...`);
}

function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    
    if (file) {
        alert(`File "${file.name}" selected!`);
        // You can further process the file here
    } else {
        alert("No file selected.");
    }
}