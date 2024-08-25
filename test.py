<div style="text-align: center; position: relative; display: inline-block;">
    <div class="bell">🔔
        {{#contents}}
            {{& pywebio_output_parse}}
        {{/contents}}
    </div>
    <div class="bell_cnt">1</div>
</div>

<style>
    .bell {
        font-size: 30px;
        width: 50px;
        display: inline-block;
        margin: auto;
        animation: ring 1s ease-in-out infinite;
        position: relative;
    }

    .bell_cnt {
        font-size: 12px;
        color: red;
        position: absolute;
        top: 0px;
        left: 30px;
        background-color: white;
        border-radius: 50%;
        width: 20px;
        height: 20px;
        text-align: center;
        line-height: 20px;
        font-weight: bold;
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
