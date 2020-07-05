from graphics import *

window = GraphWin("Convert Temp", 500, 500)

window.setCoords(0.0, 0.0, 5.0,5.0)

celsiusLabel = Text(Point(2.5, 3), "Celsius Temp")

celsiusLabel.draw(window)

input = Entry(Point(2.5, 2.5), 4)

input.draw(window)

fahrenheitLabel = Text(Point(2.5, 2), "Fahrenheit Temp")
fahrenheitLabel.draw(window)

output = Text(Point(2.5, 1.5), "0.0")
output.draw(window)

buttonText = Text(Point(2.5, 1.0), "Convert")
buttonText.draw(window)

buttonShape = Rectangle(Point(2.0, 0.8), Point(3, 1.2))
buttonShape.draw(window)

window.getMouse()

celsiusValue = int(input.getText())

fahrenheitValue = 9.0/5.0 * celsiusValue + 32

output.setText(fahrenheitValue)

window.getMouse()