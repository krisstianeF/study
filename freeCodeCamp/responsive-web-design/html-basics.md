HTML (HyperText Markup Language) — это не язык программирования, а язык разметки. Это **скелет** любой веб-страницы.

*More on [HTML Review](https://www.freecodecamp.org/learn/responsive-web-design-v9/review-html/review-html)*

- [Template](#template)
- [Text and titles](#text-and-titles)
- [Links](#links)
- [Images](#images)
- [Lists](#lists)
- [Blocks](#blocks)
- [Elements](#elements)
- [Audio And Video](#audio-and-video)
- [SVG](#svg)
- [Scripts](#scripts)
---

## Template

Любой HTML-файл должен начинаться с этой структуры. Без неё браузер не поймет, что вы от него хотите.

```html
<!DOCTYPE html>
<html lang = "en">
    <head>
        <meta charset="UTF-8">
        <title> ... </title>
    </head>
    <body>
        <h1> ... </h1>
    </body>
</html>
```

```html
<!-- Comment text -->
```

## Text and titles
Теги — это команды в угловых скобках `< > ... </ >`  
`<strong> жирный текст </strong>`  
`<em> курсив </em>`

```html
<h1>Header_1</h1>
<h2>Header_2</h2>
<h6>Header_6</h6>
```

```html
<nav> 
    <ul> 
        <li> <a href="#">Home</a> </li> 
        <li> <a href="#about">About</a> </li> 
    </ul> 
</nav>
```
<nav> 
<a href="#">Home</a> 
<a href="#about">About</a> 
</nav>

```html

<p>text</p>
```

```html
<br> <!-- Принудительный перенос на новую строку -->
<hr> <!-- Горизонтальная линия-разделитель -->
```


## Links
```html
<a href="https://github.com">Перейти на GitHub</a>
<!-- Ссылка: href - адрес -->
```
To open links in a new tab, you can use the `target` attribute on the anchor (a) element.
```html
<a href="https://www.freecodecamp.org" target="_blank">freeCodeCamp</a>
```

```html
<head>
    <link href="styles.css" rel="stylesheet" />
</head>

<body>
    <a href="https://freecodecamp.org" target="_blank">Visit freeCodeCamp</a>
</body>
```

```css
a:visited {
  color: brown;
}
```

```css
a:hover {
  color: red;
}
```

```css
a:focus {
  color: green;
}
```

```css
a:active {
  color: black;
}
```
## Images

```html
<img src="cat.png" alt="Тут должен быть котик" width="300">
<!-- Картинка: src - путь к файлу. alt - текст, если картинка не загрузится. width - ширина -->
```

## Lists

```html
<!-- Unordered List -->
<ul>
    <li>first</li>
    <li>second</li>
</ul>
```

```html
<!-- Ordered List -->
<ol start=5>
    <li>first</li>
    <li>second</li>
</ol>
```

```html
<!-- Description List -->
<dl>
  <dt>HTML</dt>
  <dd>HyperText Markup Language</dd>
  <dt>CSS</dt>
  <dd>Cascading Style Sheets</dd>
  <!-- <dt>JS</dt>
  <dd>JavaScript</dd> -->
</dl>
```
<dl>
  <dt>HTML</dt>
  <dd>HyperText Markup Language</dd>
  <dt>CSS</dt>
  <dd>Cascading Style Sheets</dd>
  <!-- <dt>JS</dt>
  <dd>JavaScript</dd> -->
</dl>

## Blocks
Тег `<div>` — это невидимая коробка. Она нужна, чтобы группировать элементы вместе (например, чтобы потом покрасить их в один цвет через CSS).

```html
<div>
    ...
</div>
```
`<div class="class-name" id="id-name"> ... </div>`  
*`<span>` - для выделения маленького кусочка текста внутри строки.*

```html
<main>
    ...
</main>
```

```html
<footer>
  ...
</footer>
```

## Elements

```html
<button>Button_text</button>   
```

```html
<iframe
  title="Title"
  width="300"
  height="200"
  src="link">
</iframe>
```

```html
<input type="image" alt="Descriptive text goes here" src="example-img-url">
```

```html
<code> ... </code>
```

```html
<pre>
  <code>
    ...
  </code>
</pre>
```

| element | description |  |
| -- | -- | -- |
| `<u></u>` | u - unarticulated annotation element | is used to represent inline text that has non-textual annotation applied |
| `<s></s>` | s - strikethrough element | should be used to represent when text is no longer accurate or relevant |
| `<ruby></ruby>` |  |
| `<rp></rp>` |  |
| `<rt></rt>` |  |

## Audio And Video

```html
<audio
  src="link"
  loop
  controls
  muted
></audio>
```

```html
<audio controls>
  <source src="audio.ogg" type="audio/ogg" />
  <source src="audio.wav" type="audio/wav" />
  <source src="audio.mp3" type="audio/mpeg" />
</audio>
```

```html
<video
  src="link"
  loop
  controls
  muted
  poster="link"
  width="400"
></video>
```

```html
<video controls width="400" poster="link">
  <source src="link" type="video/mp4" />
  <source src="link" type="video/webm" />
  Your browser does not support the video tag.
</video>
```

## SVG

```html
<!-- Star Icon -->
<svg width="50" height="50" viewBox="0 0 24 24" fill="gold" xmlns="http://www.w3.org/2000/svg">
  <path d="M12 2L14.9 8.6L22 9.3L17 14.1L18.3 21.2L12 17.8L5.7 21.2L7 14.1L2 9.3L9.1 8.6L12 2Z"/>
</svg>
```
```html
<!-- Heart Icon -->
<svg width="50" height="50" viewBox="0 0 24 24" fill="crimson" xmlns="http://www.w3.org/2000/svg">
  <path d="M12 21.35L10.55 20.03C5.4 15.36 2 12.28 2 8.5C2 6 4 4 6.5 4C8 4 9.5 4.8 10.5 6.09C11.5 4.8 13 4 14.5 4C17 4 19 6 19 8.5C19 12.28 15.6 15.36 10.45 20.04L12 21.35Z"/>
</svg>
```

```html
<!-- Checkmark Icon -->
<svg width="50" height="50" viewBox="0 0 24 24" fill="green" xmlns="http://www.w3.org/2000/svg">
  <path d="M20.29 5.71L9 17L3.71 11.71L5.12 10.29L9 14.17L18.88 4.29L20.29 5.71Z"/>
</svg>
```

## Scripts
```html
<script src="path-to-javascript-file.js"></script>
```