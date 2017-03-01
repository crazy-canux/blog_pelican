---
layout: post
title: Java之java.util
comments: true
date: 2016-04-28 22:36:47
updated:
tags:
- java
- util
categories:
- Java
permalink:
---

# java.util

> Contains the collections framework, legacy collection classes, event model,
date and time facilities, internationalization, and miscellaneous utility
classes (a string tokenizer, a random-number generator, and a bit array

# java.util.Scanner

Constructor:

    Scanner(File source) /* 构造一个从给定文件读取数据的对象 */
    Scanner(File source, String charsetName)
    Scanner(InputStream source) /* 用给定的输入流创建一个对象 */
    Scanner(InputStream source, String charsetName)
    Scanner(Path source) /* 构造一个从给定路径读取数据的对象 */
    Scanner(Path source, String charsetName)
    Scanner(Readable source)
    Scanner(ReadableByteChannel source)
    Scanner(ReadableByteChannel source, String charsetName)
    Scanner(String source) /* 构建一个从给定字符串读取数据的对象 */

Method:

    void close()
    Pattern delimiter()
    String findInLine(Pattern pattern)
    String findInLine(String pattern)
    String findWithinHorizon(Pattern pattern, int horizon)
    String findWithinHorizon(String pattern, int horizon)
    boolean hasNext()
    boolean hasNext(Pattern pattern)
    boolean hasNext(String pattern)
    boolean hasNextBigDecimal()
    boolean hasNextBigInteger()
    boolean hasNextBigInteger(int radix)
    boolean hasNextBoolean()
    boolean hasNextByte()
    boolean hasNextByte(int radix)
    boolean hasNextDouble()
    boolean hasNextFloat()
    boolean hasNextInt()
    boolean hasNextInt(int radix)
    boolean hasNextLine()
    boolean hasNextLong()
    boolean hasNextLong(int radix)
    boolean hasNextShort()
    boolean hasNextShort(int radix)
    IOException ioException()
    Locale locale()
    MatchResult match()
    String next()
    String next(Pattern pattern)
    String next(String pattern)
    BigDecimal nextBigDecimal()
    BigDecimal nextBigInteger()
    BigDecimal nextBigInteger(int radix)
    boolean nextBoolean()
    byte nextByte()
    byte nextByte(int radix)
    double nextDouble()
    float nextFloat()
    int nextInt()
    int nextInt(int radix)
    String nextLine()
    long nextLong()
    long nextLong(int radix)
    short nextShort()
    short nextShort(int radix)
    int radix()
    void remove()
    Scanner reset()
    Scanner skip(Pattern pattern)
    Scanner skip(String pattern)
    String toString()
    Scanner useDelimiter(Pattern pattern)
    Scanner useDelimiter(String pattern)
    Scanner useLocale(Locale locale)
    Scanner useRadix(int radix)

# java.util.Arrays

Field：

Constructor:

Method:

    static <T> List<T> asList(T... a)
    static int binarySearch(...)
    static <T>int binarySearch(...)
    static type[] copyOf(type[] a, int newLength) / 返回和a类型相同的数组, 长度为length /
    static type[] copyOfRange(type[] a, int start, int end) / 返回和a类型相同数组，从start开始，从end结束 /
    static boolean deepEquals(Object[] a1, Object[] a2)
    static int deepHashCode(object[] a)
    static String deepToString(Object[] a)
    static boolean equals(...)
    static boolean equals(type[] a, type[] a2) / 如果两个数组大小相同，对应元素相等，返回true /
    static void fill(type[] a, type val) / 将数组所有元素值设置为val /
    static void fill(type[] a, int fromIndex, int toIndex, type val)
    static int hashCode(...)
    static ... parallelPrefix(...)
    static ... parallelSetAll(...)
    static ... parallelSort(...)
    static ... setAll(...)
    static void sort(type[] a, ...) / 使用优化的快速排序算法对数组排序 /
    static ... spliterator(...)
    static ... stream(...)
    static String toString(type[] a) / 返回包含a中数据元素的字符串 /

# java.util.Date

Field:

Constructor:

    Date()
    Date(long date)

Method:

    boolean after(Date when)
    boolean before(Date when)
    Object clone()
    int compareTo(Date anotherDate)
    boolean equals(Object obj)
    static Date from(Instant instant)
    long getTime()
    int hashCode()
    void setTime(long time)
    Instant toInstant()
    String toString()

# java.util.Calender

Field:

Constructor:

Method:

# java.util.GregorianCalender

Field:

Constructor:

Method:

# java.util.Random

Field:

Constructor:

    Random()
    Random(long seed)

Method:

    DoubleStream doubles(...)
    IntStream ints(...)
    LongStream longs(...)
    protected int next(int bits)
    boolean nextBoolean()
    void nextBytes(byte[] bytes)
    double nextDouble()
    float nextFloat()
    double nextGaussian()
    int nextInt()
    int nextInt(int bound)
    long nextLong()
    void setSeed(long seed)

# java.util.Objects

Field:

Constructor:

Method:

    static <T> int compare(T a, T b, Comparator<? super T> c)
    static boolean deepEquals(Object a, Object b)
    static boolean equals(Object a, Object b)
    static int hash(Object... values)
    static int hashcode(Object o)
    static boolean isNull(Object obj)
    static boolean nonNull(Object obj)
    static <T> t requireNonNull(...)
    static String toString(...)

# java.util.AbstractCollection<E>

Field:

Constructor:

    protected AbstractCollection()

Method:

    boolean add(E a)
    ...

# java.util.AbstractList<E> (java.util.AbstractColletion<E>)

Field:

    protected int modCount

Constructor:

    protected AbstractList()

Method:

    boolean add(E e)
    ...

# java.util.ArrayList<E> (java.util.AbstractList<E>)

Field:

Constructor:

    ArrayList() / 构造一个空数组列表 /
    ArrayList(Collection<? extends E> c)
    ArrayList(int initialCapacity) / 用指定容量构造一个空数组列表 /

    eg:
    ArrayList<ClassName> var = new ArrayList<>();

Method:

    boolean add(E e) / 在数组列表尾端添加一个元素，永远返回true /
    void add(int index, E element) / 在中间插入一个元素 /
    boolean addAll(Collection<? extends E> c)
    boolean addAll(int index, Collection<? extends E> c)
    void clear()
    Object clone()
    boolean contains(object o)
    void ensureCapacity(int minCapacity) /确保数组列表在不重新分配存储空间的情况下就能保存给定数量元素 /
    void forEach(Consumer<? super E> action)
    E get(int index) / 获取数组列表中的元素的值 /
    int indexOf(Object o)
    boolean isEmpty()
    Iterator<E> iterator()
    int lastIndexOf(object o)
    ListIterator<E> listIterator()
    ListIterator<E> listIterator(int index)
    E remove(int index) / 从数组列表中删除一个元素 /
    boolean remove(Object o)
    boolean removeAll(Collection<?> c)
    boolean removeIf(Predicate<? super E> filter)
    boolean removeRange(int romIndex, int toIndex)
    void replaceAll(UnaryOperator<E> operator)
    boolean retainAll(collection<?> c)
    E set(int index, E element) / 更改数组列表中元素的值 /
    int size() / 返回存储在数组列表中的当前元素数量 /
    void sort(Comparator<? super E> c)
    Spliterator<E> spliterator()
    List<E> subList(int fromIndex, int toIndex)
    Object[] toArray()
    <T> T[] toArray(T[] a) / 将数组元素拷贝到一个数组中 /
    void trimToSize() / 将数组列表的存储容量削减到当前尺寸 /
