// Retrieve all books
function getBooks() {
    $.ajax({
        url: '/api/books/',
        type: 'GET',
        success: function(response) {
            updateBookList(response);
        }
    });
}

// Retrieve a single book
function getBook(id) {
    $.ajax({
        url: '/api/books/' + id + '/',
        type: 'GET',
        success: function(response) {
            updateBookDetails(response);
        }
    });
}

// Create a new book
function createBook(title, author, description) {
    $.ajax({
        url: '/api/books/',
        type: 'POST',
        data: {
            title: title,
            author: author,
            description: description
        },
        success: function(response) {
            getBooks();
        }
    });
}

// Update a book
function updateBook(id, title, author, description) {
    $.ajax({
        url: '/api/books/' + id + '/',
        type: 'PUT',
        data: {
            title: title,
            author: author,
            description: description
        },
        success: function(response) {
            getBook(id);
            getBooks();
        }
    });
}

// Delete a book
function deleteBook(id) {
    $.ajax({
        url: '/api/books/' + id + '/',
        type: 'DELETE',
        success: function(response) {
            getBooks();
        }
    });
}

// Update the book list HTML
function updateBookList(books) {
    var bookList = $('#book-list');
    bookList.empty();
    for (var i = 0; i < books.length; i++) {
        var book = books[i];
        var bookItem = $('<li>').text(book.title);
        bookItem.click(function() {
            getBook(book.id);
        });
        bookList.append(bookItem);
    }
}

// Update the book details HTML
function updateBookDetails(book) {
    $('#book-title').text(book.title);
    $('#book-author').text(book.author);
    $('#book-description').text(book.description);
}

// Add event listeners to the HTML elements
$(document).ready(function() {
    $('#create-book').click(function() {
        var title = $('#title-input').val();
        var author = $('#author-input').val();
        var description = $('#description-input').val();
        createBook(title, author, description);
    });
});
