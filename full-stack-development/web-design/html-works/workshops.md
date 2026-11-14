
- [Cat Photo App](#cat-photo-app)
- [Bookstorage Page](#bookstorage-page)
- [HTML Music Player](#html-music-player)
- [HTML Video Player](#html-video-player)
- [iframe Video Display](#iframe-video-display)
---

## Cat Photo App

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">    
    <title>CatPhotoApp</title>
  </head>
  <body>
    <main>
      <h1>CatPhotoApp</h1>
      <section>
        <h2>Cat Photos</h2>
        <p>Everyone loves <a href="https://cdn.freecodecamp.org/curriculum/cat-photo-app/running-cats.jpg">cute cats</a> online!</p>
        <p>See more <a target="_blank" href="https://freecatphotoapp.com">cat photos</a> in our gallery.</p>
        <a href="https://freecatphotoapp.com"><img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/relaxing-cat.jpg" alt="A cute orange cat lying on its back."></a>
      </section>
      <section>
        <h2>Cat Lists</h2>
        <h3>Things cats love:</h3>
        <ul>
          <li>catnip</li>
          <li>laser pointers</li>
          <li>lasagna</li>
        </ul>
        <figure>
          <img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/lasagna.jpg" alt="A slice of lasagna on a plate.">
          <figcaption>Cats <em>love</em> lasagna.</figcaption>  
        </figure>
        <h3>Top 3 things cats hate:</h3>
        <ol>
          <li>flea treatment</li>
          <li>thunder</li>
          <li>other cats</li>
        </ol>
        <figure>
          <img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg" alt="Two tabby kittens sleeping together on a couch.">
          <figcaption>Cats <strong>hate</strong> other cats.</figcaption>  
        </figure>
      </section>
    </main>
    <footer>
      <p>
        No Copyright - <a href="https://www.freecodecamp.org">freeCodeCamp.org</a>
      </p>
    </footer>
  </body>
</html>
```

## Bookstorage Page

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>XYZ Bookstore Page</title>
</head>

<body>
  <h1>XYZ Bookstore</h1>
  <p>Browse our collection of amazing books!</p>
  
  <div class="card-container">
    <div class="card" id="sally-adventure-book">
      <h2>Sally's SciFi Adventure</h2>
      <p>This is an epic story of Sally and her dog Rex as they navigate through other worlds.</p>
      <button class="btn">Buy Now</button>
    </div>
    
    <div class="card" id="dave-cooking-book">
      <h2>Dave's Cooking Adventure</h2>
      <p>This is the story of Dave as he learns to cook everything from pancakes to pasta, one recipe at a time.</p>
      <button class="btn">Buy Now</button>
    </div>
  </div>
  
  <p>Review your selections and continue to checkout.</p>
  
  <div class="btn-container">
    <button class="btn" id="view-cart-btn">View Cart</button>   
    <button class="btn" id="checkout-btn">Checkout</button>  
    
  </div>
</body>

</html>
```

## HTML Music Player

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Working with the HTML Audio Element</title>
</head>
<body>

  <h1>freeCodeCamp Tunes</h1>

  <h2>Can't Stay Down</h2>
  <p>Artist: Quincy Larson</p>
  
  <audio src="https://cdn.freecodecamp.org/curriculum/js-music-player/can't-stay-down.mp3" loop controls></audio>

  <h2>Cruising for a Musing</h2>
  <p>Artist: Quincy Larson</p>

  <audio src="https://cdn.freecodecamp.org/curriculum/js-music-player/cruising-for-a-musing.mp3" loop controls></audio>

</body>
</html>
```

## HTML Video Player

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Working with the HTML Video Element</title>
</head>
<body>
  <h1>Working with the HTML Video Element</h1>
  <video
    width="640"
    loop
    controls
    muted
    poster="https://cdn.freecodecamp.org/curriculum/labs/past-event2.jpg"
  >
    <source
      src="https://cdn.freecodecamp.org/curriculum/labs/what-is-the-map-method-and-how-does-it-work.mp4"
      type="video/mp4"
    >
    <source
      src="https://cdn.freecodecamp.org/curriculum/labs/mapmethod.webm"
      type="video/webm"
    >
    <source
      src="https://cdn.freecodecamp.org/curriculum/labs/mapmethod.ogg"
      type="video/ogg"
    >
    <source
      src="https://cdn.freecodecamp.org/curriculum/labs/mapmethod.mov"
      type="video/quicktime"
    >        
  </video>
</body>
</html>
```

## iframe Video Display
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Display Videos in an iframe</title>
  </head>
  <body>
    <h1>iframe Video Display</h1>
    <iframe
      width="560"
      height="315"
      src="https://www.youtube.com/embed/I0_951_MPE0"
      allow="accelerometer autoplay clipboard-write encrypted-media gyroscope web-share"
      referrerpolicy="strict-origin-when-cross-origin"
      allowfullscreen = ""
    >

    </iframe>
  </body>
</html>
```

