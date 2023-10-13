document.addEventListener("DOMContentLoaded", function() {
    var form = document.querySelector('form');
    var entryList = document.querySelector('.row'); // Select the second row as the container

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        var entryValue = document.querySelector('input[name="entry"]').value;

        if (entryValue.trim()) {
            // Create a new entry element
            var entryItem = document.createElement('div');
            entryItem.classList.add('col-12', 'text-center');
            entryItem.innerHTML = `
                <span>${entryValue}</span>
                <button class="btn btn-danger">Delete</button>
            `;
            entryItem.classList.add("mb-3");
            entryList.appendChild(entryItem);

            // Submit the form to the server
            submitForm(form);

            // Clear the input field after successful submission
            document.querySelector('input[name="entry"]').value = '';
        }
    });

    function removeEntry(button) {
        // Remove the entry element when the delete button is clicked
        var entryItem = button.parentElement;
        entryList.removeChild(entryItem);
    }

    function submitForm(form) {
        // Serialize form data
        var formData = new FormData(form);

        // Create an AJAX request
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '', true);

        xhr.onload = function() {
            if (xhr.status === 200) {
                // Handle a successful response from the server
                console.log('Server response:', xhr.responseText);
            } else {
                // Handle errors or other status codes
                console.error('Server error:', xhr.status);
            }
        };

        xhr.send(formData);
    }
});