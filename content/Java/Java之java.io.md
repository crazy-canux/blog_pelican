---
layout: post
title: Java之java.io
comments: true
date: 2016-05-05 22:35:44
updated:
tags:
categories:
permalink:
---

# java.io

> Provides for system input and output through data streams, serialization and
the file system. Unless otherwise noted, passing a null argument to a
constructor or method in any class or interface in this package will cause a
NullPointerException to be thrown.

# java.io.Console

Field:

Constructor:

Method:

    void flush()
    Console format(String fmt, Object... args)
    Console printf(String format, Object... args)
    Reader reader()
    String readLine()
    String readLine(String fmt, Object... args)
    char[] readPassword()
    char[] readPassword(String fmt, Object... args)
    PrintWriter writer()

# java.io.InputStream

Field:

Constructor:

    InputStream()

Method:

    int available()
    void close()
    void mark(int readlimit)
    boolean markSupported()
    abstract int read()
    int read(byte[] b)
    int read(byte[] b, int off, int len)
    void reset()
    long skip(long n)

## java.io.FilterInputStream (java.io.InputStream)

Field:

    protected InputStream in

Constructor:

    protected FilterInputStream(InputStream in)

Method:

    The same with java.io.InputStream.

# java.io.OutputStream

Field:

Constructor:

    OutputStream()

Method:

    void close()
    void flush()
    void write(byte[] b)
    void write(byte[] b, int off, int len)
    void write(int b)

## java.io.FilterOutputStream (java.io.OutputStream)

Field:

    protected OutputStream out

Constructor:

    FilterOutputStream(OutputStream out)

Method:

    The same with java.io.OutputStream

### java.io.PrintStream (java.io.FilterOutputStream)

Field:

Constructor:

    PrintStream(File file)
    PrintStream(File file, String csn)
    PrintStream(OutputStream out)
    PrintStream(OutputStream out, boolean autoFlush)
    PrintStream(OutputStream out, boolean autoFlush, String encoding)
    PrintStream(String fileName)
    PrintStream(String fileName, String csn)

Method:

    <And all java.io.OutputStream class>
    PrintStream append(char c)
    PrintStream append(CharSequence csq)
    PrintStream append(CharSequence csq, int start, int end)
    boolean checkError()
    protected void clearError()
    PrintStream format(Locale l, String format, Object... args)
    PrintStream format(String format, Object... args)
    void print(...)
    void println(...)
    PrintStream printf(Local l, String format, Object... args)
    PrintStream printf(String format, Object... args)
    protected void setError()

# java.io.Writer

Field:

    protected Object lock

Constructor:

    protected Writer()
    protected Writer(Object lock)

Method:

    Writer append(char c)
    Writer append(CharSequence csq)
    Writer append(CharSequence csq, int start, int end)
    abstract void close()
    abstract void flush()
    void write(char[] cbuf)
    abstract void write(char[] cbuf, int off, int len)
    void write(int c)
    void write(String str)
    void write(String str, int off, int len)

## java.io.PrintWriter (java.io.Writer)

Field:

    protected Writer out

Constructor:

    PrintWriter(File file)
    PrintWriter(File file, String csn)
    PrintWriter(OutputStream out)
    PrintWriter(OutputStream out, boolean autoflush)
    PrintWriter(String fileName) /* 构建一个将数据写入文件的对象 */
    PrintWriter(String fileName, String csn)
    PrintWriter(Writer out)
    PrintWriter(Writer out, boolean autoFlush)

Method:

    <And all java.io.Writer class.>
    boolean checkError()
    protected void clearError()
    PrintWriter format(Locale l, String format, Object... args)
    PrintWriter format(String format, Object... args)
    void print(...)
    void println(...)
    PrintWriter printf(Locale l, String format, Object... args)
    PrintWriter printf(String format, Object... args)
    protected void setError()

