Title: GSL_cryptographic
Date: 2018-01-01 10:49:21
Tags: Go, crypto, hash



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

method:

    func (h Hash) Avaliable() bool
    func (h Hash) Size() int
    func (h Hash) New() hash.Hash

***

# crypto/cipher

## function




## Block

代表一个使用特定密钥的底层　加／解密器．

    type Block interface {
        BlockSize() int
        Encrypt(dst, src []byte)
        Decrypt(dst, src []byte)
    }

## BlockMode

代表一个工作在块模式(CBC, ECB等)的加／解密器

    type BlockMode interface {
        BlockSize() int
        CryptBlocks(dst, src []byte)
    }

function:

    // 返回一个BlockMode接口，底层用b加密，初始向量长度等于b的块尺寸.
    func NewCBCEncrypter(b Block, iv []byte) BlockMode

    // 返回一个BlockMode接口，底层用b解密，初始向量长度等于b的块尺寸.
    func NewCBCDecrypter(b Block, iv []byte) BlockMode

## Stream

stream接口表示一个流模式的加／解密器．

    type Stream interface {
        XORKeyStream(dst, src []byte)
    }

function:

    func NewCFBEncrypter(block Block, iv []byte) Stream

    func NewCFBDecrypter(block Block, iv []byte) Stream

    func NewOFB(b Block, iv []byte) Stream

    func NewCTR(b Block, iv []byte) Stream

***

# crypto/rand

***

# crypto/aes

## constants

    const BlockSize = 16

## function

    // 创建一个cipher.Block接口, key为密钥，长度只能是16(aes-128),24(aes-192),32(aes-256)字节.
    func NewCipher(key []byte) (cipher.Block, error)

***

# crypto/des

***

# crypto/dsa

***

# crypto/rsa

***

# crypto/md5

## constants

    const BlockSize = 64
    const Size = 16

## function

    // 返回data的ms5检验和
    func Sum(data []byte) [Size]byte

    func New() hash.Hash

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
