---
layout: post
title: Java之java.math
comments: true
date: 2016-07-10 17:50:10
updated:
- java
tags:
- Java
categories:
permalink:
---

# java.math

> Provides classes for performing arbitrary-precision integer arithmetic
(BigInteger) and arbitrary-precision decimal arithmetic (BigDecimal). BigInteger
is analogous to the primitive integer types except that it provides arbitrary
precision, hence operations on BigIntegers do not overflow or lose precision. In
addition to standard arithmetic operations, BigInteger provides modular
arithmetic, GCD calculation, primality testing, prime generation, bit
manipulation, and a few other miscellaneous operations. BigDecimal provides
arbitrary-precision signed decimal numbers suitable for currency calculations
and the like. BigDecimal gives the user complete control over rounding behavior,
allowing the user to choose from a comprehensive set of eight rounding modes.

# java.math.BigInteger (java.lang.Number)

Fields:

    static BigInteger ONE
    static BigInteger TEN
    static BigInteger ZERO

Constructor:

    BigInteger(byte[] val)

Method:

    BigInteger abs()
    BigInteger add(BigInteger val)
    BigInteger and(BigInteger val)
    BigInteger andNot(BigInteger val)
    int bitCount()
    int bitLength()
    byte byteValueExact()
    BigInteger clearBit(int n)
    int compareTo(BigInteger val)
    BigInteger divide(BigInteger val)
    BigInteger[] divideAndRemainder(BigInteger val)
    double doubleValue()
    boolean equals(object x)
    BigInteger flipBit(int n)
    float floatValue()
    BigInteger gcd(BigInteger val)
    int getLowestSetBit()
    int hashCode()
    int intValue()
    int intValueExact()
    boolean isProbablePrime(int certainty)
    long longValue()
    long longValueExact()
    BigInteger max(BigInteger val)
    BigInteger min(BigInteger val)
    BigInteger mod(BigInteger m)
    BigInteger modInverse(BigInteger m)
    BigInteger modPow(BigInteger exponent, BigInteger m)
    BigInteger multiply(BigInteger val)
    BigInteger negate()
    BigInteger nextProbablePrime()
    BigInteger not()
    BigInteger or(BigInteger val)
    BigInteger pow(int exponent)
    static BigInteger probablePrime(int bigLength, Random rnd)
    BigInteger remainder(BigInteger val)
    BigInteger setBit(int n)
    BigInteger shiftLeft(int n)
    BigInteger shiftRight(int n)
    BigInteger shortValueExact()
    int signum()
    BigInteger subtract(BigInteger val)
    boolean testBit(int n)
    byte[] toByteArray()
    String toString()
    String toString(int radix)
    static BigInteger valueOf(long val)
    BigInteger xor(BigInteger val)

# java.math.BigDecimal

Field:

Constructor:

Method:

# java.math.MathContext

Field:

Constructor:

Method:

