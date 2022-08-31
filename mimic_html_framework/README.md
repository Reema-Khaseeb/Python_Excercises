* Write A class that can create an html element.

- This class will take 3 parameters.
  - name ( html element name)
  - value ( html element value)
    - can be:
      - Html element.
      - string
      - list of ( Html elements ).
  - attrs ( html element attributes).
    - must be a dict.
  - Any invalid name shall cause a custom exception.

- Upon the creation be carefull about the unique html attrs like :id. if there is two or more with the same id must raise an exception.

- This class will have a 4 class level methods.
  - append
    - this will append childern to the current html element.
    - if one of the elements have the same id of another element this will fire a custom exception.  
  - render
    - Will render the html element and its own sub elements like this: ``` <name attr1="attr1_value" ... > value </name> ```and print it to the stdout.
    - render will respect level indentation, see the usecase below to understand.
    - If one of the elements have the same id of another element this will fire a custom exception.  
  - find elements by attrs
    - Will take the element and find an attr value by the attr passed to it in the element itself or in the sub elements.
    - Example `find_elements_by_attr(elem, 'id', 'first')`. this will find the element with id first.
    - If the attr is `id` then it should be special each element, there is no element can have the same id.
    - In the render call if there is two element have the same id you need to raise a custom exception. 
  - find element by tag name
    - Will take the element and find all tags that match the tag pass to it in itself or in the sub elements.
  - render an html file.
    - Will render the element and the sub element into an html file.
    - The file shall have the doc type in the beginning.
  
 
 
 - Use Pdoc3 to generate an html documentation for the code.
 
 - usecase:
   - We have element called div that have two sub element h1 and p should be renderd like this.
    ```
    <div>
      <h1></h1>
      <p></p>
    </div>
    ```
   - We need to render it with indentations, each level with adjust indentation.
  
