<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Random Word App</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
            font-family: Arial, sans-serif;
        }
        
        .container {
            text-align: center;
        }
        
        button {
            padding: 10px 20px;
            font-size: 18px;
            cursor: pointer;
            border-radius: 5px;
            margin-top: 20px;
        }
        
        h1 {
            color: #333;
            font-weight: bold;
        }
    </style>
</head>

<body>
<div class="container">
    <h1 id="output"></h1>
    <button onclick="showRandomWord()">Поехали!</button>
</div>

<script>
    const wordsList = [
        "Путешествие", "Радость", "Любовь", "Свобода", "Мир",
        "Счастье", "Красота", "Дружба", "Искусство", "Природа"
    ];

    function showRandomWord() {
        const outputElement = document.getElementById('output');
        const randomIndex = Math.floor(Math.random() * wordsList.length);
        outputElement.textContent = wordsList[randomIndex];
    }
</script>

</body>
</html>
