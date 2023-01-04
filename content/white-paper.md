<!-- uuid: 7a99d9cd -->
<!-- status: Draft -->
<!-- created: 2022-06-28 12:43:19.800584+00:00 -->
<!-- modified: 2022-07-08 21:49:18.746834+00:00 -->
<!-- categories: Pages -->
<!-- language: en -->
<!-- title: White paper -->
<!-- slug: /white-paper -->

# White paper

## Introduction

This article's primary goal is to gain a deeper understanding of how Ophuscado operates.

Ophuscado is a secure encrypted email service designed to provide higher security and privacy than standard email services.

To do this, Ophuscado uses a combination of end-to-end encryption with a zero-access encryption algorithm to ensure that no unencrypted data is sent to the server. If the server exclusively stores encrypted data, the chances of your email being intercepted and read by others are virtually zero.

## Security features

Ophuscado has implemented some features to protect the privacy of our users better:

- Our servers are located in Switzerland.

- We only use physical servers to protect your data (cloud servers are prone to legal and unauthorized access risks).

- Once you click "Delete", your data will be permanently deleted. [Singapore's PDPA](https://www.pdpc.gov.sg/Overview-of-PDPA/The-Legislation/Personal-Data-Protection-Act) does not specify a specific period for data retention.

- [HTTP Strict Transport Security (HSTS](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security) ensures that you can only access our website via HTTPS using an encrypted connection to prevent anyone from reading and tampering with your communication with our website Connection.

- [Subresource Integrity (SRI)](https://en.wikipedia.org/wiki/Subresource_Integrity) verifies that the JavaScript code used by our website has not been tampered with when the website is loaded.

- We do not require any personally identifiable information to create an account. You can complete registration anonymously.

- We do not log, monitor, store, log or share any of your submissions (such as IP address).

- We support anonymous payments using [Bitcoin (BTC) and Monero (XMR).](/help-centre/billing/can-i-make-a-payment-with-cryptocurrency)

- You can access Ophuscado over the [Tor network.](/tor-network)

## Account creation

When a user registers on Ophuscado, a PGP key pair is generated, using the account's password as the password for the private key.

We use the OpenPGP.js library for encryption.

Please refer the process:

![A process of generate a encryption key](__IMAGE__)

(Source: [OpenPGP.js](https://openpgpjs.org))

And we use [Elliptic Curve Cryptography (ECC)](https://en.wikipedia.org/wiki/Elliptic-curve_cryptography), [specifically Ed25519 IETF Recommended Algorithm](https://www.ietf.org/archive/id/draft-ietf-openpgp-crypto-refresh-05.html#name-ecc-curves-for-openpgp).

Implementations must implement Ed25519 for use with EdDSA and Curve25519 for use with [ECDH](https://en.wikipedia.org/wiki/Elliptic-curve_Diffie–Hellman).

In cryptography, [Curve25519](https://en.wikipedia.org/wiki/Curve25519) is an elliptic curve that provides 128-bit security (256-bit key size). It is designed for use with the Elliptic Curve Diffie-Hellman (ECDH) key agreement scheme. It is one of the fastest ECC curves and is not part of any known patent.

Compared to [RSA](<https://en.wikipedia.org/wiki/RSA_(cryptosystem)>), it provides faster encryption and decryption at a lower performance cost.

Account passwords are encrypted using a salted hash (explained further) before being sent to the server using Secure Remote Password version 6 [(SRPv6)](https://en.wikipedia.org/wiki/Secure_Remote_Password_protocol) protocol.

## Authentication

When you log in with your password, the password is hashed and sent to the backend for verification. This way, even if someone is spying on that network, they won't be able to access your credentials anytime.

For adding security, we also offer the option to enable [multi-factor authentication (MFA)](/help-centre/login-and-signup/multi-factor-authentication).

## Message encryption and decryption

### How to send encrypted messages to other Ophuscado recipients

1. The Ophuscado user composes a message.

1. The Ophuscado system will retrieve the public keys of the recipient from the servers and encrypt the message using the public keys.

1. The encrypted message is sent to the servers.

1. The Ophuscado recipient receives the encrypted message and decrypts the message using the private key.

1. The servers store an encrypted copy of the sent message in the sender's sent folder. At the same time, the servers store an encrypted copy of the received message in the recipient's inbox folder.

Note: Only the recipient can decrypt the message.

### How to send unencrypted (normal) messages to non-Ophuscado recipients

1. The Ophuscado user composes a message.
1. The message is sent to the servers in clear text.
1. The servers sends a plain text message to a non-Ophuscado recipient. At the same time, the servers encrypts the message for Ophuscado users (The server stores encrypted copies of sent messages under your sent folder).

### How to send an encrypted (password protected) message to non-Ophuscado recipients

If a Ophuscado user wants to send encrypted messages to non-Ophuscado users, a password-protected email can be used. This is a fully end-to-end encrypted communication with non-Ophuscado users.

1. The Ophuscado user will need to preset a password for the message. The message will be zero-knowledge symmetric encryption using the provided cypher.

1. The recipient will receive an email with a secure link.

1. When the recipient clicks on the link, the internet browser will open the Ophuscado web client, where they will be asked to enter the password (set in step 1) the sender used to encrypt the message.

1. After entering the correct password, the content of the email will be decrypted, allowing the recipient to read the email.

Note: The recipients does not need a Ophuscado account to reply to this encrypted message.
