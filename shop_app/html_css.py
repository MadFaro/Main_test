class css:
          container_output = """
                              #pywebio-scope-ROOT {
                                color: black;
                                position: absolute;
                                top: 0;
                                left: 0;
                                width: 100%;
                                height: 100%;
                              }                              
                              
                              .modal-dialog {
                                max-width: 520px;
                              }

                              .btn-link, .btn-link:hover {
                                color: #ffffff;
                                font: menu;
                                font-size: max(0.5vw, 10px);
                                padding:0rem;
                                width: 100%;
                                height: 100%;
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

                              .btn-outline-dark {
                                height: 100%;
                                width: 100%;
                                border: 0px;
                                border-radius: 0px;
                                font-family: cursive;
                                font-size:max(0.8vw, 10px)
                              }

                              .btn-outline-primary{
                                height: 100%;
                                width: 100%;
                                border-color:black;
                                color:black;
                              }

                              .btn-outline-danger {
                                height: 100%;
                                width: 100%;
                              }

                              .btn-outline-dark:hover {
                                border-radius: 0px;
                                background-color: #343a4061;
                              }

                              .webio-tabs {
                                position: relative;
                                border-radius: 0px;
                                transition: transform 0.3s ease, box-shadow 0.3s ease;
                                transition: all 0.2s ease;
                              }

                              .webio-tabs > .webio-tabs-content {
                                padding: 0rem;
                              }
                              
                              .webio-tabs:hover {
                                border-radius: 0px;
                                transform: translateY(-5px);                              
                              }

                              .webio-tabs > input[type=radio]:checked + label:hover {
                                cursor: default;
				                        background:white;
                              }

                              .webio-tabs > input[type=radio]:checked + label {
                                border-bottom: 1px solid #000000;
                              }

                              .webio-datatable {
                                filter: drop-shadow(1px 1px 2px #181d1f);
                                font-size:0.8vw;
                              }              
                              """

          tpl = '''
          <tab>
              {{#contents}}
                  {{& pywebio_output_parse}}
              {{/contents}}
          </tab>
          '''

          footer = '''
          <footer class="footer">
          Powered by
          </forret>
          '''