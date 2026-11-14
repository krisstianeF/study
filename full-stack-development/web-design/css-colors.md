CSS supports **named colors**, **hex**, **rgb/rgba**, **hsl/hsla**, and keywords like `transparent` / `currentColor`.

- [Color formats](#color-formats)
- [Gradients](#gradients)
- [Named colors (148)](#named-colors-148)
  - [Pink / Rose](#pink--rose)
  - [Red](#red)
  - [Orange](#orange)
  - [Yellow](#yellow)
  - [Purple / Violet](#purple--violet)
  - [Green](#green)
  - [Cyan / Teal](#cyan--teal)
  - [Blue](#blue)
  - [Brown / Earth](#brown--earth)
  - [White / Gray / Black](#white--gray--black)

## Color formats

| Format | Example | Description |
| --- | --- | --- |
| Named color | `red` | One of 148 predefined names (below) |
| Hex | `#ff0000`, `#f00` | `#RRGGBB` RGB in hexadecimal |
| `rgb()` / `rgba()` | `rgb(255,0,0)`, `rgba(255,0,0,0.5)` | Red, green, blue (+ alpha) |
| `hsl()` / `hsla()` | `hsl(0,100%,50%)` | Hue, saturation, lightness (+ alpha) |
| `transparent` | `transparent` | Fully transparent (= `rgba(0,0,0,0)`) |
| `currentColor` | `currentColor` | Inherits the element’s `color` |

## Gradients

Gradients are **images**, so use them with `background` or `background-image` — **not** `background-color`.

| Type | Syntax | Description |
| --- | --- | --- |
| `linear-gradient()` | `linear-gradient(angle/to side, color-stop %, ...)` | Gradient along a straight line |
| `radial-gradient()` | `radial-gradient(shape size at position, color-stop...)` | Gradient radiating from a center point |
| `conic-gradient()` | `conic-gradient(from angle at position, color-stop...)` | Gradient rotated around a center point |
| `repeating-linear-gradient()` | same as linear, but repeats | Repeating linear stripes |
| `repeating-radial-gradient()` | same as radial, but repeats | Repeating radial rings |
| `repeating-conic-gradient()` | same as conic, but repeats | Repeating conic sectors |

**Angle in gradients** = direction/starting point  
 Units: `deg`, `grad`, `rad`, `turn`.

| Unit | Meaning | Full circle | Example |
| --- | --- | --- | --- |
| `deg` | Degrees (most common) | `360deg` | `45deg` |
| `grad` | Gradians | `400grad` | `100grad` = `90deg` |
| `rad` | Radians | `2π rad` ≈ `6.283rad` | `1.57rad` ≈ `90deg` |
| `turn` | Full rotations | `1turn` | `0.25turn` = `90deg` |

**Conversion:** `1turn = 360deg = 400grad = 2π rad`  
**Used in CSS:** gradients, `rotate()`, `hue-rotate()`, `conic-gradient(from ...)`, etc.  
**Short rule:** use `deg` normally; use `turn` for simple fractions like `0.25turn`.


## Named colors (148)

### Pink / Rose

| Name | Hex |
| --- | --- |
| `pink` | `#FFC0CB` |
| `lightpink` | `#FFB6C1` |
| `hotpink` | `#FF69B4` |
| `deeppink` | `#FF1493` |
| `palevioletred` | `#DB7093` |
| `mediumvioletred` | `#C71585` |

### Red

| Name | Hex |
| --- | --- |
| `lightcoral` | `#F08080` |
| `indianred` | `#CD5C5C` |
| `crimson` | `#DC143C` |
| `red` | `#FF0000` |
| `firebrick` | `#B22222` |
| `darkred` | `#8B0000` |

### Orange

| Name | Hex |
| --- | --- |
| `coral` | `#FF7F50` |
| `tomato` | `#FF6347` |
| `orangered` | `#FF4500` |
| `darkorange` | `#FF8C00` |
| `orange` | `#FFA500` |

### Yellow

| Name | Hex |
| --- | --- |
| `gold` | `#FFD700` |
| `yellow` | `#FFFF00` |
| `lightyellow` | `#FFFFE0` |
| `lemonchiffon` | `#FFFACD` |
| `lightgoldenrodyellow` | `#FAFAD2` |
| `papayawhip` | `#FFEFD5` |
| `moccasin` | `#FFE4B5` |
| `peachpuff` | `#FFDAB9` |
| `palegoldenrod` | `#EEE8AA` |
| `khaki` | `#F0E68C` |
| `darkkhaki` | `#BDB76B` |

### Purple / Violet

| Name | Hex |
| --- | --- |
| `lavender` | `#E6E6FA` |
| `thistle` | `#D8BFD8` |
| `plum` | `#DDA0DD` |
| `violet` | `#EE82EE` |
| `orchid` | `#DA70D6` |
| `fuchsia` | `#FF00FF` |
| `magenta` | `#FF00FF` |
| `mediumorchid` | `#BA55D3` |
| `mediumpurple` | `#9370DB` |
| `blueviolet` | `#8A2BE2` |
| `darkviolet` | `#9400D3` |
| `darkorchid` | `#9932CC` |
| `darkmagenta` | `#8B008B` |
| `purple` | `#800080` |
| `indigo` | `#4B0082` |
| `slateblue` | `#6A5ACD` |
| `darkslateblue` | `#483D8B` |
| `mediumslateblue` | `#7B68EE` |
| `rebeccapurple` | `#663399` |

### Green

| Name | Hex |
| --- | --- |
| `greenyellow` | `#ADFF2F` |
| `chartreuse` | `#7FFF00` |
| `lawngreen` | `#7CFC00` |
| `lime` | `#00FF00` |
| `limegreen` | `#32CD32` |
| `palegreen` | `#98FB98` |
| `lightgreen` | `#90EE90` |
| `mediumspringgreen` | `#00FA9A` |
| `springgreen` | `#00FF7F` |
| `mediumseagreen` | `#3CB371` |
| `seagreen` | `#2E8B57` |
| `forestgreen` | `#228B22` |
| `green` | `#008000` |
| `darkgreen` | `#006400` |
| `yellowgreen` | `#9ACD32` |
| `olivedrab` | `#6B8E23` |
| `olive` | `#808000` |
| `darkolivegreen` | `#556B2F` |
| `mediumaquamarine` | `#66CDAA` |
| `darkseagreen` | `#8FBC8F` |
| `lightseagreen` | `#20B2AA` |

### Cyan / Teal

| Name | Hex |
| --- | --- |
| `darkcyan` | `#008B8B` |
| `teal` | `#008080` |
| `aqua` | `#00FFFF` |
| `cyan` | `#00FFFF` |
| `lightcyan` | `#E0FFFF` |
| `paleturquoise` | `#AFEEEE` |
| `aquamarine` | `#7FFFD4` |
| `turquoise` | `#40E0D0` |
| `mediumturquoise` | `#48D1CC` |
| `darkturquoise` | `#00CED1` |
| `cadetblue` | `#5F9EA0` |
| `steelblue` | `#4682B4` |

### Blue

| Name | Hex |
| --- | --- |
| `lightsteelblue` | `#B0C4DE` |
| `powderblue` | `#B0E0E6` |
| `lightblue` | `#ADD8E6` |
| `skyblue` | `#87CEEB` |
| `lightskyblue` | `#87CEFA` |
| `deepskyblue` | `#00BFFF` |
| `dodgerblue` | `#1E90FF` |
| `cornflowerblue` | `#6495ED` |
| `royalblue` | `#4169E1` |
| `blue` | `#0000FF` |
| `mediumblue` | `#0000CD` |
| `darkblue` | `#00008B` |
| `navy` | `#000080` |
| `midnightblue` | `#191970` |

### Brown / Earth

| Name | Hex |
| --- | --- |
| `cornsilk` | `#FFF8DC` |
| `blanchedalmond` | `#FFEBCD` |
| `bisque` | `#FFE4C4` |
| `navajowhite` | `#FFDEAD` |
| `wheat` | `#F5DEB3` |
| `burlywood` | `#DEB887` |
| `tan` | `#D2B48C` |
| `rosybrown` | `#BC8F8F` |
| `sandybrown` | `#F4A460` |
| `goldenrod` | `#DAA520` |
| `darkgoldenrod` | `#B8860B` |
| `peru` | `#CD853F` |
| `chocolate` | `#D2691E` |
| `saddlebrown` | `#8B4513` |
| `sienna` | `#A0522D` |
| `brown` | `#A52A2A` |
| `maroon` | `#800000` |

### White / Gray / Black

| Name | Hex |
| --- | --- |
| `white` | `#FFFFFF` |
| `snow` | `#FFFAFA` |
| `honeydew` | `#F0FFF0` |
| `mintcream` | `#F5FFFA` |
| `azure` | `#F0FFFF` |
| `aliceblue` | `#F0F8FF` |
| `ghostwhite` | `#F8F8FF` |
| `whitesmoke` | `#F5F5F5` |
| `seashell` | `#FFF5EE` |
| `beige` | `#F5F5DC` |
| `oldlace` | `#FDF5E6` |
| `floralwhite` | `#FFFAF0` |
| `ivory` | `#FFFFF0` |
| `antiquewhite` | `#FAEBD7` |
| `linen` | `#FAF0E6` |
| `lavenderblush` | `#FFF0F5` |
| `mistyrose` | `#FFE4E1` |
| `gainsboro` | `#DCDCDC` |
| `lightgray` / `lightgrey` | `#D3D3D3` |
| `silver` | `#C0C0C0` |
| `darkgray` / `darkgrey` | `#A9A9A9` |
| `gray` / `grey` | `#808080` |
| `dimgray` / `dimgrey` | `#696969` |
| `lightslategray` / `lightslategrey` | `#778899` |
| `slategray` / `slategrey` | `#708090` |
| `darkslategray` / `darkslategrey` | `#2F4F4F` |
| `black` | `#000000` |

**Notes:**
- `aqua` = `cyan` and `fuchsia` = `magenta` (same colors, different names).
- `gray`/`grey` spelling variants are identical in value.
- `transparent` and `currentColor` are keywords, not named colors.