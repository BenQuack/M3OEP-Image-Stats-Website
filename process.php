<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="Ben Quackenbush" content="Ben Quackenbush">
        <title>Image Stats</title>
        <meta name="Takes an image and creates a few stats about the pixels that it contains" content="image stats using php html and python">
        <link href="style.css" rel="stylesheet" type="text/css" media="screen" />
    </head>
    <body>
    	<header>
    		<h1>CS 2300</h1>
    		<h2>Open Ended Project</h2>
    		<h3>Image Stats Project</h3>
    	</header>

        <form action="imageUpload.php" method="post" enctype="multipart/form-data">
          Select image to upload:
          <input type="file" name="fileToUpload" id="fileToUpload">
          <input type="submit" value="Upload Image" name="submit">
        </form>
    </body>
</html>
