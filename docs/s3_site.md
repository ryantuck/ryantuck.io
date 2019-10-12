# S3 Site

Some notes on setting up a static S3 site because I always forget one piece of this and bash my head against the wall figuring out nameserver stuff.



- parts
    - domain (iwantmyname or namecheap)
    - s3 bucket with public hosting on
    - route53 hosted zone
- details
    - dns changes sometimes take minutes/hours to propagate
    - if s3 hosting works via the aws-supplied url, it's a networking issue
    - need to point NS values of domain provider to your route53 hosted zone

