html = """
<!DOCTYPE html>
<html>
    <head>
        <title>FastAPI WebSocket Test</title>
    </head>
    <body>
        <h1>WebSocket Test Client</h1>
        <div id="messages"></div>
        <input type="text" id="messageText" placeholder="Type a message...">
        <button onclick="sendMessage()">Send</button>
        <script>
            var clientId = Date.now();  // unique id per client
            var ws = new WebSocket(`ws://localhost:8000/ws/${clientId}`);
        
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages');
                var message = document.createElement('div');
                message.textContent = event.data;
                messages.appendChild(message);
            };
        
            function sendMessage() {
                var input = document.getElementById('messageText');
                ws.send(input.value);
                input.value = '';
            }
        </script>
    </body>
</html>
"""