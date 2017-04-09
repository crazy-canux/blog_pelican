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

    from robot.api import logger, deco
    # robot的log和decorator接口

    from robot.parsing.modle import TestData
    TestData(parent=None, source=None, include_suites=None, warn_on_skipped=False, extensions=None) # return model.TestCaseFile or model.TestDataDirectory
    testsuite = TestData(source="your.robot")

