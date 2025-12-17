document.addEventListener('DOMContentLoaded', () => {
    console.log('CulinaShare loaded successfully.');
    
    // Example: Add confirmation dialog to delete buttons
    const deleteBtns = document.querySelectorAll('.btn-danger');
    deleteBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            if (!confirm('Are you sure?')) {
                e.preventDefault();
            }
        });
    });
});