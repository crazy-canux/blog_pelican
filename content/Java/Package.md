Title: Package
Date: 2016-04-03 10:49:07
Tags: Java, Jar, Package



# Package

***

# jar

用jar命令打包， 可以包含图像，声音，源代码等文件，并进行压缩。

    $ jar cvf JarFile.jar File1 File2 ... # 将指定文件压缩归档到JarFileName这个jar包。
    $ jar cvfm JareFile.jar manifest.mf File ... # 根据清单文件mainfest.mf压缩归档。
    $ jar uvfm JarFile.jar mainfest-additions.mf # 更新已有jar包。

运行jar包：

    $ java -jar JarFile.jar

***

# jws

JWS: Java Web Start

jws是一项通过internet发布应用程序的技术。

JWS程序需要打包一个或多个jar文件，然后创建一个JNLP格式的描述符文件，将这些文件放到web服务器。

JWS特性：
1. 通过浏览器发布，下载到本地就可以启动，不再需要浏览器。
2. 应用程序不在浏览器窗口内，显示在浏览器外的一个属于自己的框架中。
3. 应用程序不使用浏览器的java实现，浏览器只是在加载应用程序描述符时启动一个外部应用程序。
4. 数字签名用用程序可以被赋予访问本地机器的任意权限，未签名的应用程序只能在沙箱中运行。

***

# applet

applet是一种包含在html网页中的客户端的java应用程序。

***

# servlet

Java Servlet 是运行在 Web 服务器或应用服务器上的服务器端的java应用程序

# JSP

jsp是简化的servlet.
