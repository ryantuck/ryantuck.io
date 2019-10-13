# Running MTG Arena in AWS

I love Magic The Gathering and want to play the desktop version of the game, MTG Arena.

Some brilliant product people thought it would be best to create a PC-only game, trusting that people who are smart enough to choose macs over PCs are also smart enough to figure out how to get the damn thing working in an emulator or something.

**tl;dr - I tried WINE and VirtualBox to no avail, so used AWS to solve the problem!**

## AWS Setup

Spin up a Windows 2019 Server in AWS.

I chose a GPU-optimized machine (`g4dn.2xlarge`) to handle the graphics. TBH, it might need even more horsies than that - the graphics are a little laggy, but I can't tell if that's network-related or not.

Anyway, the key here is to not run up your AWS bill too high - shut off your machine when you're not playing!

Gave it all pretty vanilla defaults, public IP, etc. Could probably make it more secure via security groups or whatever.

### Connect via Microsoft Remote Desktop

I downloaded a remote desktop application, grabbed the public DNS entry for my instance, and found the password from Actions > Get Windows Password (decrypted using the `.pem` file you used when creating the instance).

### Enable downloads

AWS really locks down the download functionality by default (probably for good reason) so you gotta:

1. Open "Server Manager"
2. Click "Local Server" (left hand side)
3. Click the "On" link next to IE Enhanced Security Configuration
4. Turn it off for administrators
5. Now you can use IE to download MTG Arena (or Chrome, or whatever)

## Machine Maintenance

I imagine I'm gonna need to ensure this thing is not turned on at all times so I don't hemorrhage money, but that's pretty easy to do within the app.

It'd probably be cool to define a fixed public IP so I don't have to re-enter a new DNS entry into remote desktop every time I restart the machine, but hey. A route53 entry would be cool too.

Anyway, hope this helps!
