var doneButton;
function getCSRFToken() {
    var cookies = document.cookie.split(";");

    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.startsWith("csrftoken=")) {
            return cookie.substring("csrftoken=".length, cookie.length);
        }
    }

    return "";
}

function removeEntry(button) {
    console.log('removeEntry function called');
    // Remove the entry element when the delete button is clicked
    var entryList = document.querySelector('.list-unstyled');
    var listItem = button.parentElement;
    entryList.removeChild(listItem);

    // Add a function to send a DELETE request to the server
    var itemId = listItem.getAttribute('data-id'); // Get the item's ID from a data attribute
    deleteEntryOnServer(itemId);
}

function deleteEntryOnServer(itemId) {
    // Send a DELETE request to the server to delete the entry with the specified ID
    var xhr = new XMLHttpRequest();
    xhr.open('DELETE', 'api/ToDoModel/' + itemId, true);

    var csrftoken = getCSRFToken();
    xhr.setRequestHeader('X-CSRFToken', csrftoken);

    xhr.onload = function() {
        if (xhr.status === 204) {
            // Handle a successful response from the server
            console.log('Server response:', xhr.status);
        } else {
            // Handle errors or other status codes
            console.log('Sure');
            console.error('Server error:', xhr.status);
        }
    };

    xhr.send();
}

document.addEventListener("DOMContentLoaded", function() {
    var form = document.querySelector('form');
    entryList = document.querySelector('.list-unstyled');    

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        var entryValue = document.querySelector('input[name="entry"]').value;

        if (entryValue.trim()) {
            // Create a new entry element
            //var listItem = document.createElement('li');
            //listItem.classList.add('mb-3');
            //listItem.setAttribute('data-id', item.id);
            //listItem.innerHTML = `
               // ${entryValue}
                //<button class="btn btn-danger" onclick="removeEntry(this)">Done</button>
           // `;
            
            //entryList.insertBefore(listItem, entryList.firstChild);

            // Submit the form to the server
            submitForm(form);

            // Clear the input field after successful submission
            document.querySelector('input[name="entry"]').value = '';
        }
    });

    
    
    function submitForm(form) {
        // Serialize form data
        var formData = new FormData(form);

        // Create an AJAX request
        var xhr = new XMLHttpRequest();
        xhr.open('POST', 'api/ToDoModel', true);

        xhr.onload = function() {
            if (xhr.status === 201) {
                // Handle a successful response from the server
                console.log('Server response:', xhr.status);
                getUpdatedData();
            } else {
                // Handle errors or other status codes
                console.error('Server error:', xhr.status);
            }
        };

        xhr.send(formData);
    }   
    
    function getUpdatedData() {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', 'api/ToDoModel', true);
    
        xhr.onload = function() {
            if (xhr.status === 200) {
                // Parse the response JSON data
                var responseData = JSON.parse(xhr.responseText);
    
                // Update the HTML with the new data
                updateHTML(responseData);
            } else {
                console.error('GET request error:', xhr.status);
            }
        };
    
        xhr.send();
    }
    
    function updateHTML(entries) {
        var entryList = document.querySelector('.list-unstyled');
    
        // Clear the existing entries
        entryList.innerHTML = '';
    
        // Loop through the entries and create HTML elements
        entries.forEach(function(entry) {
            var listItem = document.createElement('li');
            listItem.classList.add('mb-3');
            listItem.setAttribute('data-id', entry.id);
            console.log(entry.id);
    
            // Display the entry text
            listItem.innerText = entry.entry;
    
            // Create a "Done" button and add an event listener to handle deletion
            var doneButton = document.createElement('button');
            doneButton.innerText = 'Done';
            doneButton.classList.add('btn', 'btn-danger');
            doneButton.onclick = function() {
                removeEntry(doneButton);
            };
    
            // Append the "Done" button to the list item
            listItem.appendChild(doneButton);
    
            // Append the list item to the entry list
            entryList.insertBefore(listItem, entryList.firstChild);
        });
    }
});