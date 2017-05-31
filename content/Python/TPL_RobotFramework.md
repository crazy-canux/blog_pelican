Title: TPL_RobotFramework
Date: 2017-03-27 21:18:33
Tags: RobotFramework



# RobotFramework

参考DevOps/robotframework进行安装配置．

    import robot.run
    # 调用该接口在程序里实现robot命令
    run(*tests, **options)
    # *tests是robot文件
    # **options包括所有robot命令的选项，另外还可以有stdout, stderr

    from robot.api import logger
    # robot的内置日志系统, 除了info可以同时选择输出到console,其它都是输出到logfile.
    logger.console(msg, newline=True, stream='stdout')
    logger.write(msg, level='INFO', html=False)
    logger.info(message, also_console=False) # 一般用来打印case的执行情况．
    logger.trace(message)
    logger.debug(message)
    logger.warn(message)
    logger.error(message)

    from robot.api.deco import keyword
    # 通过装饰器指定关键字名字和标签
    keyword(name=None, tags=())
    @keyword(name="the keyword name", tags=(tag1, tag2))
    def shortname():
        ...

    from robot.parsing.modle import TestData
    TestData(parent=None, source=None, include_suites=None, warn_on_skipped=False, extensions=None) # return model.TestCaseFile or model.TestDataDirectory
    testsuite = TestData(source="your.robot")

    from robot.errors import ExecutionFailed
