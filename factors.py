#!/usr/bin/python
import sys

def factorize(n):
    p = 2
    while p * p <= n:
        if n % p == 0:
            q = n // p
            return f"{n}={p}*{q}"
        p += 1
    return f"{n}={n}*1"
