Title: GSL_math
Date: 2018-01-01 10:49:21
Tags: Go, GSL, math, sort



# math

## constants

## variables


## functions

***

# math/big

***

# math/cmplx

***

# math/rand

***

# sort

## functions

    func Ints(a []int)
    func IntAreSorted(a []int) bool
    func SearchInts(a []int, x int) int

    func Float64s(a []float64)
    func Float64sArerSorted(a []float64) bool
    func SearchFloat64s(a []float64, x float64) int

    func Strings(a []string)
    func StringsAreSorted(a []string) bool
    func SearchStrings(a []string, x string) int

    func Sort(data Interface)
    func Stable(data Interface)
    func IsSorted(data Interface) bool
    func Reverse(data Interface) Interface
    // 二分查找
    func Search(n int, f func(int) bool) int

## Interface

    type Interface interface {
        Len() int
        Less(i, j int) bool
        Swap(i, j int)
    }

## InitSlice

    type InitSlice []int

## Float64Slice

    type Float64Slice []float64

## StringSlice

    type StringSlice []string

***


