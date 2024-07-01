from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
from mcq_generator import generate_mcqs


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # Serve the HTML form
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"""
            <html>
            <head>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                        background-color: #f4f4f4;
                    }
                    .container {
                        width: 80%;
                        margin: auto;
                        background: #fff;
                        padding: 20px;
                        border-radius: 8px;
                        box-shadow: 0 0 10px rgba(0,0,0,0.1);
                        margin-top: 20px;
                    }
                    h1 {
                        color: #333;
                    }
                    textarea {
                        width: 100%;
                        height: 150px;
                        margin-bottom: 10px;
                        padding: 10px;
                        border-radius: 4px;
                        border: 1px solid #ddd;
                    }
                    input[type="number"] {
                        padding: 10px;
                        border-radius: 4px;
                        border: 1px solid #ddd;
                    }
                    input[type="submit"] {
                        background-color: #007BFF;
                        color: #fff;
                        border: none;
                        padding: 10px 20px;
                        border-radius: 4px;
                        cursor: pointer;
                        font-size: 16px;
                    }
                    input[type="submit"]:hover {
                        background-color: #0056b3;
                    }
                </style>
                <script>
                    function toggleAnswer(id) {
                        var answer = document.getElementById('answer-' + id);
                        if (answer.style.display === 'none') {
                            answer.style.display = 'block';
                        } else {
                            answer.style.display = 'none';
                        }
                    }
                </script>
            </head>
            <body>
                <div class="container">
                    <h1>MCQ Generator</h1>
                    <form action="/process" method="post">
                        <textarea name="text" placeholder="Enter your paragraph here..."></textarea><br>
                        <label for="num_questions">Number of Questions:</label>
                        <input type="number" name="num_questions" id="num_questions" value="5" min="1" required><br>
                        <input type="submit" value="Generate MCQs">
                    </form>
                </div>
            </body>
            </html>
            """)
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"404 Not Found")

    def do_POST(self):
        if self.path == '/process':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            post_data = urllib.parse.parse_qs(post_data)
            text = post_data.get('text', [''])[0]
            num_questions = int(post_data.get('num_questions', ['5'])[0])

            # Generate MCQs
            mcqs = generate_mcqs(text, num_questions=num_questions)

            # Serve the processed MCQs
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"""
            <html>
            <head>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                        background-color: #f4f4f4;
                    }
                    .container {
                        width: 80%;
                        margin: auto;
                        background: #fff;
                        padding: 20px;
                        border-radius: 8px;
                        box-shadow: 0 0 10px rgba(0,0,0,0.1);
                        margin-top: 20px;
                    }
                    h1 {
                        color: #333;
                    }
                    .mcq {
                        margin-bottom: 20px;
                        padding: 10px;
                        border: 1px solid #ddd;
                        border-radius: 4px;
                        background-color: #f9f9f9;
                    }
                    .question {
                        font-weight: bold;
                        color: #333;
                    }
                    .choices {
                        margin-top: 10px;
                    }
                    .choices ul {
                        list-style: none;
                        padding: 0;
                    }
                    .choices li {
                        padding: 5px;
                        border-bottom: 1px solid #ddd;
                    }
                    .choices li:last-child {
                        border-bottom: none;
                    }
                    .answer {
                        display: none;
                        margin-top: 10px;
                        color: green;
                        font-weight: bold;
                    }
                    .show-answer {
                        margin-top: 10px;
                        cursor: pointer;
                        color: #007BFF;
                    }
                    .show-answer:hover {
                        text-decoration: underline;
                    }
                </style>
                <script>
                    function toggleAnswer(id) {
                        var answer = document.getElementById('answer-' + id);
                        if (answer.style.display === 'none') {
                            answer.style.display = 'block';
                        } else {
                            answer.style.display = 'none';
                        }
                    }
                </script>
            </head>
            <body>
                <div class="container">
                    <h1>Generated MCQs</h1>
            """)
            # Generate HTML for MCQs
            for i, mcq in enumerate(mcqs):
                self.wfile.write(f"""
                    <div class="mcq">
                        <div class="question">{i + 1}. {mcq['question']}</div>
                        <div class="choices">
                            <ul>
                                {''.join(f'<li>{chr(65 + j)}. {choice}</li>' for j, choice in enumerate(mcq['choices']))}
                            </ul>
                        </div>
                        <div id="answer-{i}" class="answer">
                            Correct Answer: {mcq['answer']}
                        </div>
                        <div class="show-answer" onclick="toggleAnswer({i})">Show Answer</div>
                    </div>
                """.encode('utf-8'))
            self.wfile.write(b"""
                </div>
            </body>
            </html>
            """)


def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}...')
    httpd.serve_forever()


if __name__ == "__main__":
    run()
