class css:
          container_output = """
                              .pywebio{
                                background:white;
                                    font-family: cursive;}

                              .modal-dialog {
                                  max-width: 520px;
                                  font-family: cursive;}

                              .btn-link, .btn-link:hover {
                                  color: #ffffff;
                                  font: menu;
                                  padding:0rem;
                                  width: 100%;
                                  height: 100%;
                              }

                              #pywebio-scope-ROOT{
                                color: black;
                                position: absolute;
                                top: 0;
                                left: 0;
                                width: 100%;
                                height: 100%;}

                                .webio-datatable {
                                  filter: drop-shadow(1px 1px 2px #181d1f);
                                  font-size:0.8vw;
                                }
                              .btn {
                              vertical-align: baseline;
                              font-family: cursive;
                              }
                              .btn-info {
                                border-radius: 0px;
                                border: 0px;
                                padding: 0.6vw 1.7vw;
                                filter: drop-shadow(0px 0px 1px #181d1f);
                                background-color: #181d1f;
                                border-color: #181d1f;
                                line-height: 1.5;
                                }

                              .webio-tabs{
                                position: relative;
                                transition: transform 0.3s ease, box-shadow 0.3s ease;
                                transition: all 0.2s ease;}
                              .webio-tabs > .webio-tabs-content {
                                padding: 0rem;
                              }
                              .webio-tabs:hover{
                              transform: translateY(-5px);                              
                              }

                              .webio-tabs > input[type=radio]:checked + label:hover {
                                cursor: default;
				                        background:white;}  
                              .webio-tabs > input[type=radio]:checked + label {
                                  border-bottom: 1px solid #000000;
                                  font-family: cursive;
                              }                                                    
                              .btn-outline-dark{
                                height: 100%;
                                width: 100%;
                                border: 0px;
                                font-family: cursive;
                                }
                              .btn-outline-secondary{
                                height: 100%;
                                width: 100%;
                                border: 0px;
                                color: black;
                                }
                              .btn-outline-danger{
                                height: 100%;
                                width: 100%;
                                }
                              .markdown-body details summary {
                              font-size: 2vh;
                              display: grid;
                              position: relative;
                              left: 40%
                                width: 10%;
                                height: 20%;
                              }
                              details[open] {
                                margin: 0em 0em ;
                                padding: 0em;
                                width: 10%;
                                height: 20%;
                              }
                              details[open]>summary {
                                margin: 0em;
                                padding: 0em;
                              } 
                              .markdown-body details {
                                  display: grid;
                                  width: 10%;
                              }                
                              """

          tpl = '''
          <tab>
              {{#contents}}
                  {{& pywebio_output_parse}}
              {{/contents}}
          </tab>
          '''