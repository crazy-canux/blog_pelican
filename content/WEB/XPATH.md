Title: XPATH
Date: 2017-04-07 16:43:15
Tags: XML, XPath



# XPath

XPath是一门在XML文档中查找信息的语言．

xpath定位有绝对定位和相对定位，推荐使用相对定位．

绝对的XPath定位包含了从HTML根节点起的所有元素，并且一些轻微的改变就会失效。

相对的XPath用id或者name属性来找到一个靠近的元素(比较理想的是父元素)，这样你就可以依靠他们的相对关系来确定目标元素的位置。

# firefox

firebug + firepath

firefox通过两者结合来获取xpath

# chrome

chrome的开发者工具(F12)可以直接copy xpath.
