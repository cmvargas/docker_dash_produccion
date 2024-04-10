$ docker build -t pepito_dash_plotly .
$ docker run -d -p 8050:8050 -v D:\pepitoprojects\folder_project\src:/app --rm pepito_dash_plotly