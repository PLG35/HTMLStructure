# -*-coding:Latin-1 -*

# Imports
import libHTMLStructure

# Global variables
url = "http://plgdev.fr/index"
testDefinition = ["div", "id", ["'navigationPanel'","'navigationDate'","'style'"]]

# Launch test
testResult = libHTMLStructure.TestURL(url, testDefinition)
print(testResult.output)