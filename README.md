# Encoder

## Capabilities:
  - URL encoding
  - Hex encoding
  - Unicode encoding
  - HTML encoding using ascii in decimal form
  - HTML encoding using ascii in hexidecimal form
  - Base64 encoding (base on rfc 4648)

### How it works
Following example shows encoding of all characters and print the result:
```
$ python3 src/encoder.py http -a -A 
[+] String: http
[+] Hex: 68747470
[+] Bin: 01101000011101000111010001110000
[+] Url: %68%74%74%70
[+] Html dec: &#104;&#116;&#116;&#112;
[+] Html hex: &#x68;&#x74;&#x74;&#x70;
[+] Unicode: \u0068\u0074\u0074\u0070
[+] Base64: aHR0cA==
```
Or writing the result into the specified file:
```
$ python3 src/encoder.py http -a -A -w /tmp/encoder.json
$
$ cat /tmp/encoder.json 
{
    "http": {
        "hex": "68747470",
        "bin": "01101000011101000111010001110000",
        "url": "%68%74%74%70",
        "html_dec": "&#104;&#116;&#116;&#112;",
        "html_hex": "&#x68;&#x74;&#x74;&#x70;",
        "unicode": "\\u0068\\u0074\\u0074\\u0070",
        "base64": "aHR0cA=="
    }
}
```


### Containerization
navigate to Encoder directory and build docker image:
```
$ docker build -t encoder .
$ docker images | grep encoder
encoder      latest    607d53a03527   2 hours ago   889MB

```

In order to run encoder in docker, a directory would be shared:
```
$ cat /tmp/links 
example.com
google.com
$
$ docker run -v /tmp:/tmp --rm encoder -f /tmp/links -a -x 
[+] String: example.com                                                 
[+] Hex: 6578616d706c652e636f6d

[+] String: google.com
[+] Hex: 676f6f676c652e636f6d
$
$ docker run -v /tmp:/tmp --rm encoder -f /tmp/links -w /tmp/encoder.json -B
$ cat /tmp/encoder.json 
{
    "example.com": {
        "base64": "ZXhhbXBsZS5jb20="
    },
    "google.com": {
        "base64": "Z29vZ2xlLmNvbQ=="
    }
}
```
