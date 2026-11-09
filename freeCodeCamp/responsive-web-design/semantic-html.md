# Semantic HTML
## 
| element | base usage | description |
| -- | -- | -- |
| h1 | `<h1> </h1>` | header |
| p | `<p> </p>` | paragraph |
| br | `<br>` | перенос на новую строку |
| hr | `<hr>` | horizontal line |
| em | `<em></em>` | <em>emphasis</em> |
| i | `<i></i>` | <i>italic</i> |
| strong | `<strong></strong>` | <strong>strong</strong> |
| b | `<b></b>` | <b>bold</b> |
| u | `<u><u/>` | <u>underline</u> |
| s | `<s></s>` | <s>strike</s> |
| blockquote | `<blockquote cite=""> </blockquote>` | quoted section |
| q | `<q></q>` | inline quotation |
| cite | `<cite></cite>` |  |
| abbr | `<abbr title="">ABBR</abbr>` | represent an abbreviation or acronym |
| sup | `<sup> </sup>` | superscript i<sup>n</sup> |
| sub | `<sub> </sub>` | subscript n<sub>i</sub>| 


| element | base usage | description |
| -- | -- | -- |
| nav | `<nav> <a href="#">Home</a> </nav>` | navigation |
| header | `<header> </header>` |  |
| main | `<main> </main>` |  |
| footer | `<footer> </footer>` |  |
| section | `<section id=""></section>`
| article | `<article> </article>` |  |
| figure | `<figure></figure>` | to contain illustrations and diagrams |
| figcaption | `<figcaption></figcaption>` | caption for figure |
| address | `<address> </address>` | address |

| a element | base usage | description |
| -- | -- | -- |
| link | `<a href=""> ... </a>` |  |
| internal link | `<a href="#">Home</a>` |  |
| internal link | `<a href="#title">Title</a>` | to `id='title'` |
| tel | `<a href="tel:2345678912">234-567-8912</a>` | phone number |
| mailto | `<a href="mailto:e@mail.com">e@mail.com</a>` | email |


| element | base usage | description |
| -- | -- | -- |
| ul | `<ul></ul>` | Unordered List |
| ol | `<ol></ol>` | Ordered List |
| li (inside ul/ol) | `<li></li>` |  |
| dl | `<dl></dl>` | Description List |
| dt (inside dl) | `<dt></dt>` |  |
| dd (inside dl) | `<dd></dd>` |  |

| element | base usage | description |
| -- | -- | -- |
| img | `<img src="" alt="">` | image |
| svg |  | svg image |
| audio | `<audio> </audio>` |  |
| video | `<video> </video>` |  |
| iframe | `<iframe src=""> </iframe>` | inline frame - to embed one web page inside another |

| element | base usage | description |
| -- | -- | -- |
| button | `<button> </button>` | button |
| script | `<script src=""> </script>` |  |
| meta | `<meta >` |  |
| time | `<time datetime="20:00">20:00 </time>` | standard format is `YYYY-MM-DDThh:mm:ss` |
| -- | -- | -- |
| - | `<!-- -->` | comment |

## Forms and Tables
```html
<form action="">
  <label for="email"> Email Address: </label>
  <input type="email" id="email" placeholder="example@email.com" />
  <button>Ok</button>
</form>
```

| element | base usage |
| -- | -- |
| label | `<label for=""></label>` |
| input | `<input required type="" name="" id=""/>` |
| button | `<button type=""></button>` |