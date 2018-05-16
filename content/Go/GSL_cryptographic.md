Title: GSL_cryptographic
Date: 2018-01-01 10:49:21
Tags: Go, GSL, crypto, hash



# crypto

收集了常用的密码常量

## functions

    RegisterHash(h Hash, f func() hash.Hash)

## PublicKey

interface:

    type PublicKey interface{}

## PrivateKey

interface:

    type PrivateKey interface{}

## Hash

    type Hash uint

***

# crypto/dsa

***

# crypto/rsa

***

# crypto/md5

***

# crypto/sha1

## constants

    // SHA1块大小
    const BlockSize = 64

    // SHA1校验和的字节数
    const Size = 20

## functions

    // 返回数据data的SHA1校验和
    func Sum(data []byte) [Size]byte

    // 返回一个使用新的SHA1校验的hash.Hash接口
    func New() hash.Hash

***

# crypto/sha256

***

# crypto/sha512

***

# hash

## Hash

被所有hash函数实现的公共接口

interface:

    type Hash interface {
        io.Writer
        Sum(b []byte) []byte
        Reset()
        Size() int
        BlockSize() int
    }

## Hash32

被所有32位hash函数实现的公共接口

interface:

    type Hash32 interface {
        Hash
        Sum32() uint32
    }

## Hash64

被所有64位hash函数实现的公共接口

interface:

    type Hash64 interface {
        Hash
        Sum64() uint64
    }

***

# hash/adler32

***

# hash/crc32

***

# hash/crc64

***

# hash/fnv

***
