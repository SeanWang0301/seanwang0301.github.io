# Sean Wang As A FullStack Engineer

I will keep learning and practicing as a real full stack Engineer. Following notes are related to the courses in codecademy. 

## HTML (HyperText Markup Language) Week27 

> Q: What is the correct definition of an HTML element?
> A: An HTML tag and the content that it contains or marks up
> 
> R: HTML supports headings from ranging from `<h1>` (biggest) to `<h6>` (smallest).


- [Mozilla Developer Network](https://developer.mozilla.org/en-US/)

Introducing you to MDN documentation early on provides you with an additional resource for looking up syntax and familiarizes you with one of the most important sources of documentation about web technologies. It also gives you the resources to enrich and extend your knowledge of a topic or subject beyond a beginner-level. So when you're stuck on something, or you just want to learn a little more, try reading the documentation. You might just find what you're looking for!

### Table recap

- The `<table>` element creates a table.
- The `<tr>` element adds rows to a table
- The `<td>`element adds data to a row
- Table headings clarify the meaning of data. Headings are added with the `<th>` element.
- Table data can span columns using the `colspan` attribute.
- Table data can span rows using the `rowspan` attribute.
- Tables can be split into three main sections: a head, a body, and a footer.
  - A table's head is created with the `<thead>` element
  - A table's body is created with the `<tbody>` element
  - A table's footer is created with the `<tfoot>` element

### Semantic HTML

- `<header>`
- `<nav>`
- `<main>`
- `<footer>`
- `<article>`
- `<section>`
- `<aside>`
- `<figure>`
- `<figcaption>`
- `<video>`
- `<audio>`
- `<embed>`

Congrats on completing this lesson on Semantic HTML! Now that you know the benefits of Semantic HTML and how to use it, you can incorporate semantic elements into your website to make it more accessible and to make the code easier to read.

Let’s review some of the topics we covered throughout the lesson:

- Semantic HTML introduces meaning to a page through specific elements that provide context as to what is in between the tags.
- Semantic HTML is a modern standard and makes a website accessible for people who use screen readers to translate the webpage and improves your website’s SEO.
- `<header>`, `<nav>` , `<main>`and `<footer>` create the basic structure of the webpage.
- `<section>` defines elements in a document, such as chapters, headings, or any other area of the document with the same theme.
- `<article>` holds content that makes sense on its own such as articles, blogs, comments, etc.
- `<aside>` contains information that is related to the main content, but not required in order to understand the dominant information.
- `<figure>` encapsulates all types of media.
- `<figcaption>` is used to describe the media in `<figure>`.
- `<video>`, `<embed>`, and `<audio>` elements are used for media files.

Now, apply this knowledge to become a better Web Developer.

## CSS Anatomy

The diagram on the right shows two different methods, or syntaxes, for writing CSS code. The first syntax shows CSS applied as a ruleset, while the second shows it written as an inline style. Two different methods of writing CSS may seem a bit intimidating at first, but it's not as bad as it looks!

Both methods contain common features in their anatomy. Notice how both syntaxes contain a declaration. Declarations are the core of CSS. They apply a style to the selected element.

### Ruleset Terms

- **Selector** - The beginning of the ruleset used to target the element that will be styled
- **Declaration Block** - The code in-between (and including) the curly braces `{ }` that contains the CSS declarations
- **Declaration** - The group name for a property and value pair that applies a style to the selected element
- **Property** - The first part of the declaration that signifies what visual characteristic of the element is to be modified
- **Value** - The second part of the declaration that signifies the value of the property

### Inline Style Terms

- **Opening Tag**-The start of an HTML Element. This is the element that will be styled.
- **Attribute**-The style attribute is used to add CSS inline styles to an HTML element.
- **Declaration**-The group name for a property and value pair that applies a style to the selected element. 
- **Property**-The first part of the declaration that signifies what visual characteristic of the element is to be modified.
- **Value**-The second part of the declaration that signifies the value of the property.

![css-style-declaration](/css/css-style-declaration.png)

You can use the `<link>` element to link HTML and CSS file together. The `<link>` element must be placed within the head of HTML file. It is a self-closing tag and requires the following attributes:

1. `href` - like the anchor element, the value of this attribute must be address, or path, to the CSS file.
2. `rel` - this attribute describes the relationship between the HTML file and CSS file. Because you are linking to a stylesheet, the value should be set to `stylesheet`.

When linking an HTML file and a CSS file together, the `<link>` element will look like the following:

`<link href='https://www.codecademy.com/stylesheets/style.css' rel='stylesheet'>`


To make styles easy to edit, it’s best to style with a type selector, if possible. If not, add a class selector. If that is not specific enough, then consider using an ID selector.

CSS Selector:

- HTML Tag, eg. `h2 { color: yellow }`
- Class, eg. `.destination { color: blue }`
- Chain, eg. `h2.destination { color: black} `
- Id, eg. `#destination-head { color: pink }`
- Style, eg. `style='color: red'`

### Review

- CSS can select HTML elements by type, class, ID, and attribute
- All elements can be selected using the universal selector
- An element can have different states using the pseudo-class selector
- Multiple CSS classes can be applied to one HTML element
- Classes can be reusable, while IDs can only be used once
- IDs are more specific than classes, and classes are more specific than type. That means IDs will override any styles from a class, and classes will override any styles from a type selector
- Multiple selectors can be chained together to select an element. This raises the specificity but can be necessary
- Nested elements can be selected by separating selectors with a space
- Multiple unrelated selectors can receive the same styles by separating the selector names with commas

### Visual Rules

- The `font-family` property defines the typeface of an element
- `font-size` controls the size of text displayed
- `font-weight` defines how thin or thick text is displayed
- The `text-align` property places text in the left, right, or center of its parent container
- Text can have two different color attributes: `color` and `background-color`. `color` defines the color of the text, while `background-color` defines the color behind the text
- CSS can make an element transparent with the `opacity` property
- CSS can also set the background of an element to an image with the `background-image` property
- The `!important` flag will override any style, however it should almost never be used, as it is extremely difficult to override

### Box Model

Box Model is an important concept to understand how elements are positioned and displayed on a website. There are 4 aspects of the box model:

- The dimensions of an element's box.
- The borders of an element's box.
- The paddings of an element's box.
- The margins of an element's box.

1. The box model comprises a set of properties used to create space around and between HTML elements.
2. The height and width of a content area can be set in pixels or percentages.
3. Borders surround the content area and padding of an element. The color, style, and thickness of a border can be set with CSS properties.
4. Padding is the space between the content area and the border. It can be set in pixels or percent.
5. Margin is the amount of spacing outside of an element's border.
6. Horizontal margins add, so the total space between the borders of adjacent elements is equal to the sum of the right margin of one element and the left margin of the adjacent element.
7. Vertical margins collapse, so the space between vertically adjacent elements is equal to the larger margin.
8. `margin: 0 auto` horizontally centers an element inside of its parent content area, if it has a width.
9. The `overflow` property can be set to `display`, `hidden`, or `scroll`, and dictates how HTML will render content that overflows its parent's content area.
10. The `visibility` property can hide or show elements.

[CSS Tools: Reset CSS](https://meyerweb.com/eric/tools/css/reset/)
> *{box-sizing: border-box;}

Using Chrome DevTools allows us see the hidden make up of HTML elements which helps us better understand how our HTML elements are created and why are layout behaves the way it does.
- All HTML elements are rectangular boxes to the browser
- We can use DevTools to view and modify element's boxes
- The browser determines the size o the box unless we override it
- We should reset the box model because it makes it easier for us as developers

### Position and Layout

- The `position` property allows you to specify the position of an element.
- When set to `relative`, an element's position is relative to its closets positioned parent element.
- when set `absolute`, an element's position is relative to its closest positioned parent element. It can be pinned to any part of the web page, but the element will still move with the rest of the document when the page is scrolled.
- when set to `fixed`, an element's position can be pinned to any part of the web page. The element will remain in view no matter what.
- When set to `sticky`, an element can stick to defined offset position when the use scrolls its parent container.
- The `z-index` of an element specifies how far back or how far forward an element appears on the page when it overlaps other elements.
- The `display` property allows you to control how an element flows vertically and horizontally in a document.
- `inline` elements take up as little space as possible, and they cannot have manually adjusted `width` or `height`.
- `block` elements take up the width of their container and can have manually adjusted `height`.
- `inline-block` elements can have set `width` and `height`, but they can also appear next to each other and do not take up their entire container width.
- The `float` property can move elements as far left or as right as possible on a web page.
- You can clear an element's left or right side(or both) using the `clear` property

> The z-index property only applies to elements with a position value of relative, absolute, fixed, or sticky, not elements with a position of static. Setting the position value to static will indeed ignore the z-index property, which is why it is the correct answer in this case.
> 
> Absolute positioning allows an element to be positioned in relation to the nearest parent element that is not static, which differs from relative positioning. This distinction is key in understanding how elements are positioned on a webpage.

## Styling with CSS

Following content discuss about intermediate topics in CSS and navigation design.

### Color

Using a numeric system allows us to take advantage of the whole spectrum of colors that browsers support. Colors in CSS can be described in three different ways:

- Named colors - English words that describe colors, also called keyword colors.
- RGB - numeric values that describe a mix of red, green, anb blue
- HSL - numeric values that describe a mix of hue, saturation, and lightness