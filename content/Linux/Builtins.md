Title: Shell Builtins
Date: 2016-03-31 21:51:03
Tags: Linux, Shell, Builtins, Bash, Zsh, Fish



# Linux内置命令

内置命令在bash/builtins目录中

shell命令分为内置命令和外部命令.

查看一个命令是内置命令还是外部命令：

    type -a [command]

    提示"[command] is a shell builtin"就表示是内置命令，否则就是外部命令。

查看所有内置命令：

    help
    enable -a

查看内置命令的帮助：

    help [command]

***

    type
    enable
    help

    alias
    bg
    bind
    break
    builtin
    caller
    cd
    command
    compgen
    complete
    compopt
    continue
    declare
    dirs
    disown
    echo
    eval
    exec
    exit
    export
    false
    fc
    fg
    getopts
    hash
    history
    jobs
    kill
    let
    local
    logout
    mapfile
    popd
    printf
    pushd
    pwd
    read
    readarray
    readonly
    return
    set
    shift
    shopt
    source
    suspend
    test
    times
    trap
    true
    typeset
    ulimit
    umask
    unalias
    unset
    wait

