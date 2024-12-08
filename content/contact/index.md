---
title: "Contact"
layout: "contact"
---

<p>If you have any questions, ideas or recommendations, feel free to reach out via the form below!</p>
<style>
form {
    max-width: 600px;
    margin: auto;
}
input, textarea {
    width: 100%;
    padding: 10px;
    margin: 5px 0;
    border: 1px solid #ddd;
    border-radius: 4px;
}
textarea {
    height: 150px; /* Adjust this value to your desired height */
}
button {
    background-color: #ababab;
    color: !#ababab;
    padding: 10px 15px;
    border: none;
    cursor: pointer;
    border-radius: 4px;
}
button:hover {
    background-color: #0056b3;
}
</style>
<form action="https://formspree.io/f/xvgoygpz" method="POST">
    <label for="name">Name</label>
    <input type="text" id="name" name="name" placeholder="Your Name" required>
    <label for="email">Email</label>
    <input type="email" id="email" name="email" placeholder="Your Email" required>
    <label for="message">Message</label>
    <textarea id="message" name="message" placeholder="Your Message" required></textarea>
    <button type="submit">Send</button>
</form>