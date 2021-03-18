# Walking through your programs

## Question: How are these buttons added to the screen?

> Note-to-self: we are looping through the local button dictionary (different from self.buttons)

**First pass:**

    btnText = 7
    pos = (0, 0)
    self.buttons['7'] = QPushButton('7') # creates entry in self.buttons {'7': QPushButton('7')}
    self.buttons['7'].setFixedSize(40, 40)  # this targets QPushButton and sets the size of the button 
    # add button to QGridLayout using the format layout.addWidget(button_text, row, column)



| buttons | self.buttons |
|---------|--------------|
| 7, (0,0)| 7, QPushButton('7') |
| 8, (0, 1) |	8, QPushButton("8") |
| etc... | |


## Question: So... what happens when we click a button?

1. Click the 7 button
2. This button is connected to partial(self._buildExpression, btnText)
    
    (We need to use the partial function so that the btnText can be sent along with the function)

	**_buildExpression**
 
       expression = '' + '7'
       setDisplayText('7')
3. A 7 appears on the screen!

Let's click another button	

1. Click the + button
2. This button is also connected to partial(self._buildExpression, btnText)

	_buildExpression
		expression = '7' + '+'  --> '7+'
		setDisplayText('7+')
3. 7+ appears on the screen!

## Question: What happens when I click the '=' symbol?

> This one I'll leave to you.




