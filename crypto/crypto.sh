#!/bin/bash 

# https://www.gnupg.org/gph/en/manual.html#INTRO

# Generate keypair
gpg --gen-key

# Revoke Key
gpg --output revoke.asc --gen-revoke mykey


# View all keys on keychain 
gpg --list-keys


# Export Key 
gpg --output alice.gpg --export alice@cyb.org

# Import Key
gpg --import blake.gpg


# Edit Key
gpg --edit-key blake@cyb.org


# Encrypt a Document
gpg --output doc.gpg --encrypt --recipient blake@cyb.org doc

# Decrypt a Message
gpg --output doc --decrypt doc.gpg


# Symmetrically encrypt a document
gpg --output doc.gpg --symmetric doc


#-----------------------

# --Signing Documents--

#-----------------------

# A digital Signature certifies and timestamps a document

# Sign a document
gpg --output doc.sig --sign doc

# Signatures 
gpg --output doc.sig --sign doc


# Signs the document without compressing it
gpg --clearsign doc

