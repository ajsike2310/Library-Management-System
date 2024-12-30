<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Library Management System</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      margin: 0 auto;
      max-width: 900px;
      padding: 20px;
      background-color: #f7f7f7;
      color: #333;
    }
    h1, h2, h3 {
      color: #4CAF50;
    }
    a {
      color: #007BFF;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
    ul {
      list-style: none;
      padding: 0;
    }
    li {
      margin: 5px 0;
    }
    .code-block {
      background-color: #282c34;
      color: #f8f8f2;
      padding: 10px;
      border-radius: 5px;
      font-family: Consolas, Monaco, "Andale Mono", "Ubuntu Mono", monospace;
    }
    .github-stats img {
      margin: 10px 0;
      border-radius: 10px;
    }
  </style>
</head>
<body>

<h1>📚 Library Management System</h1>
<p>
  A Python-based library management system with a graphical interface using Tkinter. This project helps manage books, members, and transactions for efficient library operations.
</p>

<h2>🌟 Key Features</h2>
<ul>
  <li>📖 Add, update, and delete book records.</li>
  <li>🧑‍💼 Manage member registrations and details.</li>
  <li>🔄 Issue and return books with real-time transaction tracking.</li>
  <li>🔍 Search and browse books by title, author, or ISBN.</li>
  <li>📊 View transaction history and overdue reports.</li>
  <li>🕒 Tracks due dates and sends alerts for overdue books.</li>
</ul>

<h2>⚙️ Technology Stack</h2>
<ul>
  <li><strong>Programming Language:</strong> Python</li>
  <li><strong>Database:</strong> SQLite</li>
  <li><strong>Libraries/Frameworks:</strong> Tkinter, Pandas</li>
</ul>

<h2>🚀 Setup & Installation</h2>
<ol>
  <li>Install Python 3.x from the official <a href="https://www.python.org/downloads/">Python website</a>.</li>
  <li>Clone or download this repository to your local machine.</li>
  <li>Install the required Python libraries:
    <div class="code-block">pip install pandas</div>
  </li>
  <li>Run the main script to launch the application:
    <div class="code-block">python library_management.py</div>
  </li>
</ol>

<h2>📚 Functionalities</h2>
<ul>
  <li>🏷️ <strong>Add Books:</strong> Add new books to the library by specifying their title, author, and ISBN.</li>
  <li>🔄 <strong>Issue/Return Books:</strong> Manage book lending and returns with due date tracking.</li>
  <li>🗑️ <strong>Delete Records:</strong> Remove outdated or incorrect book/member records.</li>
  <li>🔍 <strong>Search:</strong> Find books using keywords or filters.</li>
  <li>📊 <strong>Reports:</strong> View transaction history and overdue records for better monitoring.</li>
</ul>

<h2>🧑‍💻 Predefined Admin Accounts</h2>
<p>Below are some predefined admin accounts for testing purposes:</p>
<table>
  <thead>
    <tr>
      <th>Admin ID</th>
      <th>Name</th>
      <th>Email</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>001</td>
      <td>Jane Doe</td>
      <td>jane.doe@library.com</td>
    </tr>
    <tr>
      <td>002</td>
      <td>John Smith</td>
      <td>john.smith@library.com</td>
    </tr>
  </tbody>
</table>

<h2>💡 Fun Fact</h2>
<p>
  This project was inspired by the need for a lightweight, intuitive tool to manage small community libraries efficiently.
</p>

<h2>✨ Quote</h2>
<blockquote>
  "A library is not a luxury but one of the necessities of life." - Henry Ward Beecher
</blockquote>

</body>
</html>
