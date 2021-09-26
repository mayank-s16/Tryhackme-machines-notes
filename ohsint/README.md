<div align = "center">
Sep 26, 2021<br>
Notes by: Mayank Kumar Prajapati<br>
Machine Name: ohsint<br>
URL: https://tryhackme.com/room/ohsint
</div>

## Exif Information
```
└─# exiftool WindowsXP.jpg 
ExifTool Version Number         : 12.16
File Name                       : WindowsXP.jpg
Directory                       : .
File Size                       : 229 KiB
File Modification Date/Time     : 2021:09:26 04:06:29-04:00
File Access Date/Time           : 2021:09:26 04:08:45-04:00
File Inode Change Date/Time     : 2021:09:26 04:08:12-04:00
File Permissions                : rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
XMP Toolkit                     : Image::ExifTool 11.27
GPS Latitude                    : 54 deg 17' 41.27" N
GPS Longitude                   : 2 deg 15' 1.33" W
Copyright                       : OWoodflint
Image Width                     : 1920
Image Height                    : 1080
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 1920x1080
Megapixels                      : 2.1
GPS Latitude Ref                : North
GPS Longitude Ref               : West
GPS Position                    : 54 deg 17' 41.27" N, 2 deg 15' 1.33" W

```
## Task 1: Ohsint
1. What is this users avatar of?
```
cat
```
2. What city is this person in?
```
London
```

3. Whats the SSID of the WAP he connected to?
```
***
```
BSSID has been disclosed on twitter account. Copy that and visit [Wigle](https://wigle.net/). Apply filter by creating an account and go advance filter.

4. What is his personal email address?
```
OWoodflint@gmail.com
```
5. What site did you find his email address on?
```
Github
```
6. Where has he gone on holiday?
```
New York
```
7. What is this persons password?
```
***
```
Found it on his website it was in white color that is why not visible in site. Investigate source code for getting it.
White Color: ffffff

