.btn-light:hover {
    color: #222;
    background-color: #dbdbdb00;
    border-color: #d5d5d500;
}

put_button("⬆", onclick=lambda:run_js('window.scrollTo({top: 0, behavior: "smooth"});'), color='light').style('position:fixed;right:1%;top:95%;z-index:2147483647')
