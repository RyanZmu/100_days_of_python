## Bootstrap Layout - 12 column layout system:
     
        <div class="container">
        <div class="row"></div>
            <div class="col">Hello</div>
        </div>
     

## Auto Fit:
Bootstrap will try to give all columns equal spacing

## Containers:
.container is used to make a nice fitting container with space around it
.container-fluid is used when edge to edge display is desired

In general:
sm = mobile
med = Ipad
lrg = laptop 
xlrg = desktop
xxlrg = TV/Ultra wide

Screen size breakpoints are between one size and then the next. IE small >576 and med >768 so between that is the sm size's breakpoint


## Sized Columns:
col-2 : div will take up 2 of the 12 columns in the row
Will help bootstrap divide sizes amongst the columns

for dealing with different size screens you can specify the col spacing with a -(num)
col-sm-2 = will give columns 2 of the 12 spaces on mobile devices
col-sm-4 = will give this column 4 spaces on a mobile device

## Setting multiple breakpoints for screen sizes:
        <div class="col-sm-12 col-md-8 col-lg-4"></div>

The above code would make it so on large devices and above will get 4/12 of the width each
on a medium take 8/12 of the width
on a mobile device 12/12 so a small screen gets full screen size

## Spacing
Can adjust padding and margin using different class names to specify what you want changed
m - margin
y - yaxis
my-3 = set the y-axis margin to 3
https://getbootstrap.com/docs/5.3/utilities/spacing/#margin-and-padding

## Dark Mode Bootstrap
<html lang="us" data-bs-theme="dark"></html>