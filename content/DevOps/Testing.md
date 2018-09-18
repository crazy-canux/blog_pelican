Title: Testing
Date: 2017-03-01 09:41:39
Tags: DevOps, QA, Testing



# QA

Quality Assurance

QA主要就是进行软件测试相关的工作.

软件测试就是使用人工或自动的手段来运行或测量软件系统的过程，以检验软件系统是否满足规定的要求，并找出与预期结果之间的差异．

软件测试五个要素：

* 质量
* 人员
* 技术
* 流程
* 资源

软件测试两个目标：

* 测试覆盖率
* 测试效率

软件测试阶段：

* 单元测试(Unit Testing)
* 集成测试(Integration Testing)
* 系统测试(System Testing)
* 验收测试(Acceptance Testing)

软件测试的手段：

* 手动测试/自动化测试
* 静态测试/动态测试
* 黑盒测试/白盒测试

软件测试的类型：

* 性能测试
* 稳定性测试
* 安全测试
* 可用性测试
* 兼容性测试
* 文档测试
* 本地化测试
* 冒烟测试
* 功能测试Functional Testing
* 回归测试Regression Testing
* 用户界面测试UI Testing
* 端到端测试End-To-End Testing

软件测试的模型：

* 传统的瀑布模型
* V模型
* W模型
* X模型
* H模型
* 敏捷测试模型(金字塔模式)

软件测试的模式：

* 金字塔模式Ideal Test Automation Pyramid
* 蛋筒冰激凌模式Ice Cream Cone
* 双金字塔模式Dual Test Pyramid
* 纸杯蛋糕模式Cupcake

# Test Automation Pyramid

Mike Cohn的测试金字塔

<https://martinfowler.com/bliki/TestPyramid.html>

* Automated GUI Tests(10%)
* Automated Service Tests(Component/Integration/API)(20%)
* Automated Unit Tests(70%)

***

# Unit Test/单元测试

单元测试是开发者编写的测试一个单元（函数／类）的功能是否符合预期．

单元测试的覆盖率是指测试的单元调用了多少代码．

Unit Test的工具有：

* Java: Junit
* Python: unittest(pyunit), nose2, pytest

***

# Test Automation

敏捷测试的核心就是自动化测试．

自动化测试框架：

* Robot Framework

ATDD: Acceptance test-driven development

BDD: Behavior-driven development

***

# big-list-of-naughty-strings

<https://github.com/minimaxir/big-list-of-naughty-strings>

测试中谨慎使用的字符串．

