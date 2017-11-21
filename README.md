# Crypto Toys

Hey, I'm just playing around.

Reading up a bit on classic ciphers, decided to start building a few toys to
help me understand them.

## Caesar Cipher

Current implementation skips characters outside of the 26 character alphabet.
Positive count shifts right, negative shifts left.  Flip the sign to decrypt.

```shell
./caesar.py --count 7 "render unto caesar that which is caesar's"
```

## Vigenere Cipher

Similar to a Caesar cipher, but shifts the alphabet according the the letters of
the key provided. Current implementation skips characters outside of the
alphabet but still advances the key rotation, which I'm not sure I like.

```shell
./vigenere.py --key lemon "attack at dawn"
```
