# Semantic HTML

| Navigation | usage | description | attributes |
| -- | -- | -- | -- |
| nav | `<nav> <a href="#">Home</a> </nav>` | navigation | `aria-label` |
| header | `<header> </header>` | intro / top of page or section (logo, title, nav) | `role` |
| main | `<main> </main>` | main unique content of page (one per page) | `role` |
| footer | `<footer> </footer>` | bottom of page or section (contacts, copyright) | `role` |
| div | `<div> </div>` | generic block container (no semantics) | `role` `aria-label` |
| section | `<section id=""></section>` | thematic block, usually with a heading | `id` `aria-labelledby` |
| article | `<article> </article>` | self-contained content (post, news, card) | `role` |
| figure | `<figure></figure>` | to contain illustrations and diagrams | `role` |
| figcaption | `<figcaption></figcaption>` | caption for figure | - |
| fieldset | `<fieldset> </fieldset>` | group of related form controls | `disabled` `name` |
| address | `<address> </address>` | address | - |
| span | `<span> </span>` | generic inline container (no semantics) | `id` `class` |
| aside | `<aside> </aside>` | side content (sidebar, related links) | `role` `aria-label` |
| code | `<code></code>` / `<pre> <code></code> </pre>` | code snippet / preformatted block | `class` |

| ARIA roles | `role="ARIA role"` |
| -- | -- |
| Document Structure | `toolbar`, `tooltip`, `feed`, `math`, `presentation`, `none`, `note` |
| Widget | `scrollbar`, `searchbox`, `separator` (when focusable), `slider`, `spinbutton`, `switch`, `tab`, `tabpanel`, `treeitem` |
| Landmark | `banner`, `complementary`, `contentinfo`, `form`, `main`, `navigation`, `region`, `search` |
| Live Region | `alert`, `log`, `marquee`, `status`, `timer` |
| Window | `alertdialog`, `dialog` |
| Abstract | They're only meant to be used internally by the browser, not by developers |

| Area attribute | description |
| -- | -- |
| `aria-label` | text label for element (when no visible label) |
| `aria-labelledby` | id of element that labels this one |
| `aria-hidden` | true/false — hide from screen readers |
| `aria-describedby` | id of element with extra description |

| Text |  |  |
| -- | -- | -- |
| h1 | `<h1> </h1>` | header (h1–h6 = heading levels) |
| p | `<p> </p>` | paragraph |
| br | `<br>` | перенос на новую строку |
| hr | `<hr>` | horizontal line |
| em | `<em></em>` | <em>emphasis</em> (stress, not just italic) |
| i | `<i></i>` | <i>italic</i> (visual only) |
| strong | `<strong></strong>` | <strong>strong</strong> (importance, not just bold) |
| b | `<b></b>` | <b>bold</b> (visual only) |
| u | `<u><u/>` | <u>underline</u> |
| s | `<s></s>` | <s>strike</s> (no longer accurate) |
| blockquote | `<blockquote cite=""> </blockquote>` | quoted section |
| q | `<q></q>` | inline quotation |
| cite | `<cite></cite>` | title of a work (book, film) |
| abbr | `<abbr title="">ABBR</abbr>` | represent an abbreviation or acronym |
| sup | `<sup> </sup>` | superscript i<sup>n</sup> |
| sub | `<sub> </sub>` | subscript n<sub>i</sub> | 

| a |  |  |
| -- | -- | -- |
| link | `<a href=""> ... </a>` | hyperlink to URL |
| internal link | `<a href="#"> ... </a>` | link to top of page |
| internal link | `<a href="#title"> ... </a>` | to `id='title'` |
| tel | `href="tel:2345678912"` | phone number |
| mailto | `href="mailto:e@mail.com"` | email |


| List |  |  |
| -- | -- | -- |
| ul | `<ul></ul>` | Unordered List |
| ol | `<ol></ol>` | Ordered List |
| li (inside ul/ol) | `<li></li>` | list item |
| dl | `<dl></dl>` | Description List |
| dt (inside dl) | `<dt></dt>` | term |
| dd (inside dl) | `<dd></dd>` | description of term |

| Media |  |  |
| -- | -- | -- |
| img | `<img src="" alt="">` | image |
| svg | `<svg></svg>` | svg image (vector) |
| audio | `<audio controls> </audio>` | sound player (`controls` shows buttons) |
| video | `<video controls> </video>` | video player (`controls` shows buttons) |
| iframe | `<iframe src=""> </iframe>` | inline frame - to embed one web page inside another |

| element |  |  |
| -- | -- | -- |
| button | `<button> </button>` | button |
| script | `<script src=""> </script>` | JS code (inline or via `src`) |
| meta | `<meta >` | page metadata (`charset`, `name`, `content`) |
| time | `<time datetime="20:00">20:00 </time>` | standard format is `YYYY-MM-DDThh:mm:ss` |
| -- | -- | -- |
| - | `<!-- -->` | comment |

## Forms

| element | base usage | attributes |
| -- | -- | -- |
| `form` | `<form action="" method=""></form>` | `action` `method` |
| `label` | `<label for="id"></label>` | `for` |
| `input` | `<input type="" name="" id="">` | `type` `id` `name` `placeholder` `size` `minlength` `maxlength` `required` `disabled` `value` `checked` `readonly` |
| `select` | `<select id="" name=""><option value=""></option></select>` | `id` `name` `multiple` `required` `disabled` |
| `option` | `<option> </option>` | inside select;  `value=""`, `selected`, `disabled`|
| `textarea` | `<textarea id="" name="" rows="" cols=""></textarea>` | `id` `name` `rows` `cols` `placeholder` `required` `disabled` |
| `button` | `<button type="submit"></button>` | `type` `id` `name` `value` `disabled`; types: `submit`, `reset`, `button` |

### Input types table

| `type="..."` | meaning / usage |
| -- | -- |
| `text` | single-line text field (default) |
| `radio` | radio button — one choice from a group (same `name`); use `checked` to preselect |
| `checkbox` | checkbox — on/off, or several choices; use `checked` to preselect |
| `number` | numeric field with `min`, `max`, `step` |
| `email` | email field, browser validates format |
| `range` | `min="0"` `max="100"` `value="30"` |



<details open> <summary> <b>See Examples</b> </summary>

```html
<form action="" method="">
  <label for="email"> Email Address: </label>
  <input type="email" id="email" placeholder="example@email.com" />
  <button>Ok</button>
</form>
```

<form action="" method="">
  <label for="email"> Email Address: </label>
  <input type="email" id="email" placeholder="example@email.com" />
  <button>Ok</button>
</form>

---

```html
<fieldset>
  <legend>Was this your first time at our hotel?</legend>
  <input id="yes-option" type="radio" name="hotel-stay" value="yes" />
  <label for="yes-option">Yes</label>
  <input id="no-option" type="radio" name="hotel-stay" value="no" />
  <label for="no-option">No</label>
</fieldset>
```

<fieldset>
  <legend>Was this your first time at our hotel?</legend>
  <input id="yes-option" type="radio" name="hotel-stay" value="yes" />
  <label for="yes-option">Yes</label>
  <input id="no-option" type="radio" name="hotel-stay" value="no" />
  <label for="no-option">No</label>
</fieldset>

---

```html
<fieldset>
  <legend>Why did you choose to stay at our hotel? (Check all that apply)</legend>

  <input type="checkbox" id="ads" name="choice" value="ads" />
  <label for="ads">Social Media Ads</label>

  <input type="checkbox" id="recommendation" name="choice" value="recommendation"/>
  <label for="recommendation">Personal Recommendation</label>
  
  <input type="checkbox" id="location" value="location" name="choice"> 
  <label for="location">Location </label>       

  <input type="checkbox" id="reputation" value="reputation" name="choice"> 
  <label for="reputation">Reputation </label>    
</fieldset>
```

<fieldset>
  <legend>Why did you choose to stay at our hotel? (Check all that apply)</legend>

  <input type="checkbox" id="ads" name="choice" value="ads" />
  <label for="ads">Social Media Ads</label>

  <input type="checkbox" id="recommendation" name="choice" value="recommendation"/>
  <label for="recommendation">Personal Recommendation</label>
  
  <input type="checkbox" id="location" value="location" name="choice"> 
  <label for="location">Location </label>       

  <input type="checkbox" id="reputation" value="reputation" name="choice"> 
  <label for="reputation">Reputation </label>    
</fieldset>

---

```html
<fieldset>
  <legend>Ratings</legend>
  <label for="service">How was the service?</label>

  <select name="service" id="service">
    <option value="poor">Poor</option>
    <option value="satisfactory">Satisfactory</option>
    <option value="good">Good</option>
    <option value="very-good">Very Good</option>
    <option selected value="excellent">Excellent</option>
  </select>
</fieldset>
```

<fieldset>
  <legend>Ratings</legend>
  <label for="service">How was the service?</label>

  <select name="service" id="service">
    <option value="poor">Poor</option>
    <option value="satisfactory">Satisfactory</option>
    <option value="good">Good</option>
    <option value="very-good">Very Good</option>
    <option selected value="excellent">Excellent</option>
  </select>
</fieldset>

</details>



## Table

| Element | usage | level | attributes |
| -- | -- | -- | -- |
| `table` | `<table></table>` | 1 | `border` (visual only, better via CSS) |
| `caption` | `<caption>Title</caption>` | 2 | first child of `table` |
| `thead` | `<thead>…</thead>` | 2 | header rows group |
| `tbody` | `<tbody>…</tbody>` | 2 | main rows group; can be several |
| `tfoot` | `<tfoot>…</tfoot>` | 2 | footer rows group |
| `tr` | `<tr>…</tr>` | 3 | table row |
| `th` | `<th>Header</th>` | 4 | header cell `colspan="2"` `rowspan="2"` `scope="col/row"` |
| `td` | `<td>Cell</td>` | 4 | table cell `colspan="2"` `rowspan="2"` |

- **table** - the whole table container; `level` = nesting depth (1 = outermost).
- **caption** - table title, shown above the table; goes right after `<table>`.
- **thead / tbody / tfoot** - group rows into header / body / footer; mainly for structure and styling.
- **tr** - one row; contains only `th`/`td`.
- **th** - header cell (bold + centered by default); `scope` tells screen readers if it heads a column or row.
- **td** - normal data cell.
- `colspan="2"` - cell spans 2 columns; 
- `rowspan="2"` — cell spans 2 rows.