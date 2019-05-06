# Security+

## Access Control

Multifactor authentication involves more than one item to authenticate to a system, such as something you have (a card), something you know (a PIN), something you are (a fingerprint), or something you do (handwriting). Using a username and password combination (single-factor authentication), along with possessing a smartcard and entering a PIN to use the smartcard, results in a username/password/smartcard/PIN scan (or multifactor) authentication. Smartcard PINs that use the card's security certificate are said to comply with the Personal Identifiable Verification (PIV) standard.

Biometric authentication requires a unique physical characteristic (something you are) such as a fingerprint scan, retinal scan, iris scan, voice recognition, or facial recognition.

Location-based authentication uses your physical location or the device you are using as part of the authentication.

 Virtual private network (VPN) creates an encrypted tunnel between a remote access client and a private network over the Internet. This would allow access to corporate database servers.

Voice over Internet Protocol (VoIP) transmits digitized voice over a TCP/IP network such as the Internet. As such, the only cost to both parties is that of your Internet connection.

Network access control (NAC) technology can be a hardware or software solution that requires user or device authentication prior to gaining network access.

Packet-filtering firewalls analyze packet headers to allow or block traffic already on the network; they don't control who (or what) gains access to the network in the first place.

Unto itself, Public Key Infrastructure (PKI) does not control network access. PKI certificates can be used to authenticate and secure network traffic and can be used with NAC solutions.

Secure Sockets Layer (SSL) encrypts traffic that is already on the network.

RADIUS clients are network devices such as switches, wireless routers, or VPN concentrators that authenticate connecting devices or users to a RADIUS authentication server to grant network access.

Terminal Access Controller Access Control System (TACACS+) is a Cisco proprietary network access protocol that uses the reliable TCP transport mechanism. TACACS+ might be used instead of RADIUS because it encrypts the entire packet payload instead of only the password, as well as separates authentication, authorization, and accounting duties.

Kerberos is an authentication protocol used by many vendors, including Microsoft with Active Directory services. Clients and servers must securely prove their identity to each other by way of a central third party referred to as a key distribution center (KDC).

Advanced Encryption Standard (AES) is a symmetric key encryption algorithm; it encrypts data transmissions, but it does not authenticate users on a network.

A central database that can securely authenticate users or computers sounds like a Lightweight Directory Access Protocol (LDAP)–compliant database. LDAP transmissions can be clear text (TCP port 389) or encrypted (TCP port 636), and the LDAP database can also be replicated among servers. Encrypted LDAP transmissions are referred to as Secured LDAP. Microsoft Active Directory Services and Novell eDirectory are LDAP compliant.

Specifying a unique attribute of some kind (such as a logon name) is identification.

Authentication occurs as a result of correct identification. A logon name uniquely identifies one user from another; all users will be authenticated given they provide their unique credentials. Authentication means proving your identity (user or computer). This can be done via username/password, smartcard, and PIN, or in this case, the computer might have a PKI certificate installed that gets validated against a server with a related PKI certificate.

Retinal scanning is considered one of the most secure authentication methods. Retinal blood vessel patterns are unique to an individual and are extremely difficult to reproduce.

A key fob displays an authentication passcode that a user enters in addition to other data such as a username and password to gain access to a system or network resource.

The Diameter protocol adds capabilities to the RADIUS protocol such as using TCP instead of UDP (more reliability) and being more scalable and flexible.

Challenge Handshake Authentication Protocol (CHAP) involves a three-way handshake to establish a session, after which peers must periodically prove their identity by way of a changing value based on a shared secret. A shared secret (for example, a password) is known by both parties but is never sent over the network.

SSO enables users to use only a single username and password to access multiple network resources even if those network resources use different authentication sources

Security Assertion Markup Language (SAML) is an XML standard that defines how authentication and authorization data can be transmitted in a federated identity environment.

A common access card is used to gain access to more than one type of secured resource.

Time-based one-time passwords (TOTP) use the current system time and a shared secret known by both the client and the server as input to a hashing algorithm. The shared secret could be a user password. The OTP is useful for only a short period of time and is recalculated often, unlike HMAC-based one-time passwords (HOTP), which are longer-lived authentication passwords.

Transitive trusts are created where one party trusts a remote party through a middle party.

OpenID Connect, OAUTH, and Shibboleth are all authentication/authorization frameworks. Shibboleth is popular in UNIX and Linux environments. Microsoft's Active Directory Federation Services (AD FS) supports related protocols such as OAUTH. These frameworks are often used for identity federation so that a user signs on initially with a trusted identity store, which generates a unique security token for that session. The token is then used to authenticate users to other resources without prompting for credentials. These solutions are often used between organizations that need to share resources, including between cloud consumers and cloud providers.

False acceptance occurs when a biometric authentication system authenticates users even if they do not match the proper credentials


## Security Policies and Standards

- **Security policies** are an organized manner through which the corporate security strategy is realized in order to reduce the risk of security breaches.Security policies are composed of subdocuments such as an Internet use policy and remote access policy. Management approval is required for security policies to make an impact.

- **Procedural policies** provide step-by-step instructions for configuring servers.

- A **service level agreement** is a contract stipulating what level of service and availability can be expected.

## System Security Threats

IT security threats can apply to software or hardware. Software threats include the exploitation of vulnerabilities and the wide array of malware such as worms and spyware. Hardware threats apply when a malicious entity gains physical access, for example, to a handheld device or a server hard disk. Physical security threats could include employees being tricked to allow unauthorized persons into a secured area such as a server room. Identifying these threats is an important step in properly applying security policies.

# Cryptography

## Hash

Hashes are invloved with password storage and encryption; hashes are one way; exact same size 

Not being used anymore
- MD5
- SHA-1

Current used version
- SHA-2
- RIPEMD

HMAC - provides message integrity; each side of conversation shoudl have the same key; based on standard hashes (MD5, sha-1, etc)

## Steganogrphy

Hiding data within data (ex. images); Tool: Image Steganogrphy

## Certificates and Trust

Certificates inlcude a public key and at least one digital signature

publick key infrasture (PKI) uses a hierachical structure with root servers
## Tools

- https://www.freeformatter.com/


## Pracice Questions
https://www.examcompass.com/comptia/security-plus-certification/free-security-plus-practice-tests

- Proferssor Messer: https://www.youtube.com/watch?v=7NS3vvHRBg4&list=PLG49S3nxzAnkijp3VBQ5CPf19bK-5hmec