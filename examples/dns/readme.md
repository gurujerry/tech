This exercise will create a simple web server and re-direct traffic from a legitimate website to it.

## Step 1 - Create a web server 
Build the web server docker image and run it on host port 80
```bash
docker build -t my-nginx-image .
docker run --name my-nginx-container -p 80:80 -d my-nginx-image
```

## Step 2 - Redirect DNS Traffic to the bogus web server
Login to your Fios Router and from the webpage `https://YOUR_FIOS_ROUTER_IP_HERE/#/advanced/dnsserver`, create an entry for `redskins.com` to point to the IP of the the host you are running the docker container in (From Step 1)

## Step 3 - Access the legitimate website
Now, from a machine on your LAN, go to http://redskins.com
