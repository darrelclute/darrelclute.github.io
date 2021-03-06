PGP Transition Statement
########################

:slug: pgp-transition-statement
:date: 2015-07-27 13:00

I have created a new OpenPGP key `0x54816ED6261FCA30`_ and am transitioning
away from my old key.  If you have signed my old key. I would appreciate
signatures on my new key as well.  I have created a transition statement which
is included inline below, and can be downloaded for verification from
`https://www.darrelclute.net/pgp-transition-statement.txt
<https://www.darrelclute.net/pgp-transition-statement.txt>`_.

.. PELICAN_END_SUMMARY

.. code-block:: text

    -----BEGIN PGP SIGNED MESSAGE-----
    Hash: SHA512
    
    OpenPGP Key Transition Statement for Darrel Ray Clute, III
    
    I have created a new OpenPGP key and will be transitioning away from
    my old key.  The old key has not been compromised and will continue to
    be valid for some time, but I prefer all future correspondence to be
    encrypted to the new key, and will be making signatures with the new
    key going forward.
    
    I would like this new key to be re-integrated into the web of trust.
    This message is signed by both keys to certify the transition.  My new
    and old keys are signed by each other.  If you have signed my old key,
    I would appreciate signatures on my new key as well, provided that
    your signing policy permits that without re-authenticating me.
    
    The old key, which I am transitioning away from, is:
    
    pub   rsa4096/0x778346C225CA8B71 2014-02-24
          Key fingerprint = B6D4 6D64 F0C2 2513 B5EA  5E5C 7783 46C2 25CA 8B71
    
    The new key, to which I am transitioning, is:
    
    pub   rsa4096/0x54816ED6261FCA30 2015-07-06 [expires: 2016-01-04]
          Key fingerprint = 58A5 4A51 58F1 C5DA C51E  A537 5481 6ED6 261F CA30
    
    The entire key may be downloaded from:https://www.darrelclute.net/pgp-public-key.txt
    
    To fetch the full new key from a public key server using GnuPG, run:
    
      gpg --recv-key 0x54816ED6261FCA30
    
    If you already know my old key, you can now verify that the new key is
    signed by the old one:
    
      gpg --check-sigs 0x54816ED6261FCA30
    
    If you are satisfied that you've got the right key, and the User IDs
    match what you expect, I would appreciate it if you would sign my key:
    
      gpg --sign-key 0x54816ED6261FCA30
    
    You can upload your signatures to a public keyserver directly:
    
      gpg --send-key 0x54816ED6261FCA30
    
    Or email darrel@darrelclute.net (possibly encrypted) the output from:
    
      gpg --armor --export 0x54816ED6261FCA30
    
    If you'd like any further verification or have any questions about the
    transition please contact me directly.
    
    To verify the integrity of this statement:
    
      wget -q -O- https://www.darrelclute.net/pgp-transition-statement.txt --verify
    
    Darrel Clute
    -----BEGIN PGP SIGNATURE-----
    Version: GnuPG v2
    
    iQIcBAEBCgAGBQJVnZqIAAoJEHeDRsIlyotx8ikP/iLReo8BQQ24J5aMeO+6uaxw
    vMWIX20Au07RuiySaYf3pMOqiWGATGo2Oa/kum7dnHBhAlEo1WUhpkAR7bZm7A9P
    LmE1xVLM0gpQyo+AVN1kdvlDFjPu0tGcCnysiaySJA+Ilh0xrW2otKvt3NKFDSAh
    K/e6ptfKCo9yZiWhLwOUj2UcWKvji4n1z+Q81YlBz+QJNEglVjIw1C2nn+Luv/Bd
    udlLPXzbf/It1qrPyrom+dRc/0tvraZzDjesoNzFqzArZjSoROR65/qMGE90oGED
    pObidQCx50qUX8GQEIO/GooGxT9oPPFpxICuyBpgvWMpNykwXXzRz4hlV6RG5Qp+
    9d5kEdI+VmPIj5R2pj69qHKklSxrnudBoEFEFapnvsomC1KNDGPEITlqiREXylMd
    SX8r1dGjZ/7zRgyo0cUX/JViG8JNHaWB2VE6GECGD93tLqFcBm/ivCRb8QiitrZv
    2BTnv8+FFmJGzab2k8hkzsHMhj95Giji0m/3tawBiLooDlpXtB+K+KQBbU+SiQT4
    GbZ+8rKJ0cjgeSDb+DhPflfrbWB+ViskGTHN7C1Rxr5gcvplbILG1p7y7idz4BwO
    uihSmgRpSUlhYo8qqvEkVb7RWuvRZvtCi3OATS2TJBbCRxECfJESInbV9sQe1GBn
    HYfCvpf0HcoglMympmO8iQEcBAEBCgAGBQJVnZqIAAoJEEz2/mdWW5KY8ikIALvb
    ljFOT8PNSsOn1qheCoQES1XcMTwU/zAJB4bv159/Zglyx7NIS7LwmsD6P/fVM3gk
    ctb7/cc7ERTyCQLaxkYAUrlrx382aLXJUCLy7bK/xNRhojyHlUB5fqQm64E4d0k/
    mewznSGmKiN2TdsQsf9PMGwaQx+vkgpADC69wWyLNxHV5626mFosOOcv+Efpp9DM
    uQYkSaz/Ul+iwj13ZVcorS6q4Hn5nZpy6bAdF1M6LId6QIRKB++TnFGf4LSmsgia
    crR+5Rqmz1BA2pm5OAIh4XLI0IPfKcfbHUe20+Kw2FMPP2LgwXqWRJqJx23Qesyo
    xb7DWWH0JbWQbnxWWxM=
    =/ShQ
    -----END PGP SIGNATURE-----

.. _0x54816ED6261FCA30: https://www.darrelclute.net/pgp-key.txt

