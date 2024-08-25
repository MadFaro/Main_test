          tpl = '''
        <div style="text-align: center;">
        <div class="bell">🔔
              {{#contents}}
                  {{& pywebio_output_parse}}
              {{/contents}}
        </div>
        <div class="bell_cnt">1</div>
        <style>
        .bell {
            font-size: 30px;
            width:50px;
            display: inline-block;
            margin: auto;
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
