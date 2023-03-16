# Chroma Key with OpenCV

## Table of contents
* [General Information](#general-information)
* [Examples](#examples)
* [Setup](#setup)

## General Information
Chroma Key is a technique by which a block of a particular color (often blue or green) in a video image can be replaced either by another color or image, enabling, for example, a weather forecaster to appear against a background of a computer-generated weather map.

## Examples
We will have two image, one with the image that have block of particular color that you want to replace into another image.

We have the orginal that had a background you want to change

![images](https://user-images.githubusercontent.com/75088003/225689897-460f991e-6020-4251-bcf0-e6e31bf5ccfb.jpg) 

An alternative background

![hurricane](https://user-images.githubusercontent.com/75088003/225690252-07634b00-2d32-402a-a9bd-4f64c570df5d.jpg) 

And then voilà,

![Chromakey](https://user-images.githubusercontent.com/75088003/225690513-e11b936c-0688-46a0-9415-66eb87e3dd53.jpg)

This is Chroma Key!

## Setup

After having the coding file, you run it. And here is the description to get the result you desired:
* After changing paths to your images, the original image (the one that have the backgound you want to replace) show up. Crop the block of color by clicking your mouse and release it. The image you've just cropped will appear.
  * If it have the color of the background you want to replace, then type "c" to continue.
  * Or else, type "r" to repeat this process.
* Then, your final image will come into view. Good luck!!

**_NOTE:_**  The image that you cropped here is the representative block of color you want to replace, so make sure you crop it nice and well!
