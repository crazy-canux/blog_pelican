Title: Javascript
Date: 2017-03-13 09:36:32
Tags: Javascript



# JavaScript

Javascript包括三部分:

1. ECMAScript核心,提供核心语言功能．
2. DOM文档对象模型, 提供访问和操作网页内容的方法和接口．
3. BOM浏览器对象模型, 提供与浏览器交互的方法和接口．

# html中使用javascript

    <!DOCTYPE html>
    <html>
      <head>
        ...head content...
      </head>
    <body>
      ...body content...

      <!-- 页面内容先呈现，然后按顺序加载和解析脚本 -->
      <script type="text/javascript" src="example.js"></script>

      <!-- defer表示整个页面解析完后才加载和解析脚本 -->
      <script type="text/javascript" defer="defer" sr"example.js"></script>

      <!-- async表示在加载页面期间异步加载和解析脚本 -->
      <script type="text/javascript" async src="example.js"></script>

    </body>
    </html>
