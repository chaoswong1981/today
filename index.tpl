<html>
  <head>
    <meta charset="utf-8" />
    <title>关注</title>
    <link type="text/css" rel="stylesheet" href="/static/index.css" />
  </head>
  <body>
    <div id="xueqiu" class="margin500">
      <p class="title">雪球头条<p/>
        %for i in xueqiu:
        <div>
          <a href="{{ i['href'] }}" target="_blank">{{ i['title'] }}</a>
          <br>
          {{ i['desc'] }}
          <br><br>
        </div> 
        %end
    </div>

    <div id="v2ex" class="margin500">
      <p class="title">v2ex今日热议</p>
      %for i in v2ex:
      <div>
        <a href="{{ i['href'] }}" target="_blank">{{ i['title'] }}</a>
        <br>
      </div>
      %end
    </div>
  </body>
</html>
