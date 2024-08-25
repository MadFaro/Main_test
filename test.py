from pywebio.output import put_widget, put_button, put_html

def bell_widget():
    template = '''
    <div style="text-align: center;">
        <div class="bell">🔔</div>
        <div>{{& pywebio_output_parse}}</div>
    </div>

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
    '''

    put_widget(template, data={"pywebio_output_parse": put_button("Click Me", onclick=lambda: print("Button clicked!"))})

bell_widget()
