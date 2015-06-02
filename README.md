# EncryptionAPI
Creates and returns public and private keys. Using Flask and SQLAlchemy in the server. Using [py-seccure](https://github.com/bwesterb/py-seccure) to generate public and private keys.

* [104.236.90.72/skylock/api/private/keys](http://104.236.90.72/skylock/api/private/keys) displays all available private keys (GET).
* [104.236.90.72/skylock/api/public/keys](http://104.236.90.72/skylock/api/public/keys) displays all available public keys (GET).
* [104.236.90.72/skylock/api/key](http://104.236.90.72/skylock/api/key) creates a new pair of public and private keys. It displays the public key (POST).

# Security
One of the ways to secure the APIs requests is by using **OAuth 2** and **SSL**. One of the advantages of OAuth 2 is its reduced complexity when compared to OAuth1.0a. Since it uses SSL, there is no signing procedure. If we were not using SSL, then refresh tokens are necessary over HTTP [1].

If SSL is not needed, then OAauth1.0a is the safest protocol since it never passes the token secret around. The advantages of this protocol are that is more widely used, tested, and there are more libraries supporting it [2].

Another way is by using public and private keys. Following Amazon's protocol shows that a user making a request can sign and pass a request (including the public key) to the server. The server then signs the request using the same algorithm and allows the request if the signature matches [3].

[1] http://stackoverflow.com/a/7562407/3641665

[2] https://stormpath.com/blog/secure-your-rest-api-right-way/

[3] http://docs.aws.amazon.com/AmazonS3/latest/dev/S3_Authentication2.html





