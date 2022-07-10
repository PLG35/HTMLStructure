# HTMLStructure
Tool validating the structure of the HTML code of a web page.

## Dependencies
The code is made to run on Python 3. In python 2.7, urllib.request should be replaced by urllib.

The library libHTMLStructure.py has the following dependencies :
- urllib.request
- html.parser

## Input
The tool requires two arguments :
- the URL of the page to test,
- a list describing the structure to test. Each element of the list must contain :
    - the name of the tag,
    - the name of the attribute of the tag,
    - a list of values for the attribute that are expected in the html.

## Output
The output is a string of data in JSON format. It always contain a key status with a value either passed or failed.

### 'Status':'Passed'
If the status is passed, there is only one additional key : results. It contains an object with two keys:
- found, which contain a list of the keys [tag, attribute, value] that were found.
- missing, which contain a list of the keys [tag, attribute, value] that were missing. It must be empty since the test is passed.

### 'Status':'Failed'
If the status is failed, the JSON always contains a key errorType with a value equal to either HTTPError, URLError or StructureError.

#### 'errorType':'HTTPError'
The JSON contains three keys :
- errorReason,
- errorCode,
- errorHeaders.

#### 'errorType':'URLError'
The JSON contains a key errorReason.

#### 'errorType':'StructureError'
The JSON contains an object with two keys:
- found, which contains a list of the keys [tag, attribute, value] that were found.
- missing, which contains a list of the keys [tag, attribute, value] that were missing.