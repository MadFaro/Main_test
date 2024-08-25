<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bell Animation</title>
    <style>
        .bell {
            font-size: 50px;
            display: inline-block;
            animation: ring 1s ease-in-out infinite;
        }

        @keyframes ring {
            0% { transform: rotate(0); }
            20% { transform: rotate(-15deg); }
            40% { transform: rotate(10deg); }
            60% { transform: rotate(-5deg); }
            80% { transform: rotate(5deg); }
            100% { transform: rotate(0); }
        }
    </style>
</head>
<body>
    <div class="bell">🔔</div>
</body>
</html>
